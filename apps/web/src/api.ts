import {
  authMode,
  clearSession,
  decodeJwtPayload,
  getAccessToken,
  rolesFromJwt,
  setSession,
} from './auth'

const API_BASE = import.meta.env.VITE_API_BASE_URL ?? '/api'

export type Product = {
  productId: string
  sku: string
  name: string
  description: string
  price: number
  quantity: number
}

export type OrderItem = {
  productId: string
  productName: string
  quantity: number
  unitPrice: number
}

export type Order = {
  orderId: string
  status: string
  total: number
  customerEmail: string
  forcePaymentFailure: boolean
  createdAt: string
  updatedAt: string
  statusReason: string
  items: OrderItem[]
}

export type ServiceHealth = {
  service: string
  status: string
  detail: string
}

export type HealthOverview = {
  overall: string
  services: ServiceHealth[]
}

export type TokenResponse = {
  accessToken: string
  tokenType: string
  expiresIn: number
  roles: string[]
}

export class ApiError extends Error {
  status: number

  constructor(status: number, message: string) {
    super(message)
    this.status = status
  }
}

async function request<T>(path: string, init?: RequestInit, auth = true): Promise<T> {
  const { headers: initHeaders, ...rest } = init ?? {}
  const headers: Record<string, string> = {
    'Content-Type': 'application/json',
    ...(initHeaders as Record<string, string> | undefined),
  }
  if (auth) {
    const token = getAccessToken()
    if (token) {
      headers.Authorization = `Bearer ${token}`
    }
  }

  const response = await fetch(`${API_BASE}${path}`, {
    ...rest,
    headers,
  })

  if (response.status === 401 && auth) {
    clearSession()
    if (!window.location.pathname.startsWith('/login')) {
      window.location.assign(`/login?next=${encodeURIComponent(window.location.pathname)}`)
    }
  }

  if (!response.ok) {
    const text = await response.text()
    throw new ApiError(response.status, text || `HTTP ${response.status}`)
  }
  if (response.status === 204) {
    return undefined as T
  }
  return response.json() as Promise<T>
}

export const api = {
  login: async (username: string, password: string) => {
    const token = await request<TokenResponse>(
      '/auth/login',
      {
        method: 'POST',
        body: JSON.stringify({ username, password }),
      },
      false,
    )
    setSession(token.accessToken, token.roles, username)
    return token
  },
  listProducts: () => request<Product[]>('/products'),
  updateStock: (productId: string, quantity: number) =>
    request<Product>(`/products/${productId}/stock`, {
      method: 'PUT',
      body: JSON.stringify({ quantity }),
    }),
  createOrder: (body: {
    items: { productId: string; quantity: number }[]
    customerEmail?: string
    forcePaymentFailure?: boolean
  }) =>
    request<Order>('/orders', {
      method: 'POST',
      body: JSON.stringify(body),
      headers: {
        ...(body.forcePaymentFailure ? { 'X-Force-Payment-Failure': 'true' } : {}),
      },
    }),
  listOrders: (status?: string) =>
    request<Order[]>(status ? `/orders?status=${encodeURIComponent(status)}` : '/orders'),
  getOrder: (orderId: string) => request<Order>(`/orders/${orderId}`),
  health: () => request<HealthOverview>('/health', undefined, false),
  acceptOidcToken: (accessToken: string) => {
    const roles = rolesFromJwt(accessToken)
    const payload = decodeJwtPayload(accessToken)
    const username =
      (payload?.preferred_username as string | undefined) ??
      (payload?.sub as string | undefined) ??
      'oidc-user'
    setSession(accessToken, roles, username)
  },
}

export function currentAuthMode() {
  return authMode()
}
