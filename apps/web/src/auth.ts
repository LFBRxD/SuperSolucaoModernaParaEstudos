const TOKEN_KEY = 'studyshop.accessToken'
const ROLES_KEY = 'studyshop.roles'
const USER_KEY = 'studyshop.username'

export type AuthMode = 'local' | 'oidc'

export function authMode(): AuthMode {
  const mode = (import.meta.env.VITE_AUTH_MODE as string | undefined) ?? 'local'
  return mode === 'oidc' ? 'oidc' : 'local'
}

export function getAccessToken(): string | null {
  return localStorage.getItem(TOKEN_KEY)
}

export function getRoles(): string[] {
  try {
    const raw = localStorage.getItem(ROLES_KEY)
    if (!raw) return []
    const parsed = JSON.parse(raw) as unknown
    return Array.isArray(parsed) ? parsed.map(String) : []
  } catch {
    return []
  }
}

export function getUsername(): string | null {
  return localStorage.getItem(USER_KEY)
}

export function isAuthenticated(): boolean {
  return Boolean(getAccessToken())
}

export function hasRole(role: string): boolean {
  const roles = getRoles()
  return roles.includes(role) || roles.includes(`ROLE_${role}`)
}

export function setSession(accessToken: string, roles: string[], username: string) {
  localStorage.setItem(TOKEN_KEY, accessToken)
  localStorage.setItem(ROLES_KEY, JSON.stringify(roles))
  localStorage.setItem(USER_KEY, username)
}

export function clearSession() {
  localStorage.removeItem(TOKEN_KEY)
  localStorage.removeItem(ROLES_KEY)
  localStorage.removeItem(USER_KEY)
}

export function decodeJwtPayload(token: string): Record<string, unknown> | null {
  try {
    const part = token.split('.')[1]
    if (!part) return null
    const json = atob(part.replace(/-/g, '+').replace(/_/g, '/'))
    return JSON.parse(json) as Record<string, unknown>
  } catch {
    return null
  }
}

export function rolesFromJwt(token: string): string[] {
  const payload = decodeJwtPayload(token)
  if (!payload) return []
  if (Array.isArray(payload.roles)) {
    return payload.roles.map(String)
  }
  const realmAccess = payload.realm_access as { roles?: unknown } | undefined
  if (realmAccess && Array.isArray(realmAccess.roles)) {
    return realmAccess.roles.map(String)
  }
  return []
}
