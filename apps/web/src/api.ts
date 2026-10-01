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

const API_BASE = import.meta.env.VITE_API_BASE_URL ?? '/api'

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  const { headers: initHeaders, ...rest } = init ?? {}
  const response = await fetch(`${API_BASE}${path}`, {
    ...rest,
    headers: {
      'Content-Type': 'application/json',
      ...(initHeaders ?? {}),
    },
  })
  if (!response.ok) {
    const text = await response.text()
    throw new Error(text || `HTTP ${response.status}`)
  }
  return response.json() as Promise<T>
}

export const api = {
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
  health: () => request<HealthOverview>('/health'),
}
