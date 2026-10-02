const OIDC_AUTHORITY = import.meta.env.VITE_OIDC_AUTHORITY ?? 'http://localhost:11015/realms/study-shop'
const OIDC_CLIENT_ID = import.meta.env.VITE_OIDC_CLIENT_ID ?? 'study-shop-web'
const OIDC_REDIRECT_URI = import.meta.env.VITE_OIDC_REDIRECT_URI ?? `${window.location.origin}/login/callback`
const PKCE_VERIFIER_KEY = 'studyshop.pkce.verifier'
const OIDC_STATE_KEY = 'studyshop.oidc.state'
const OIDC_NEXT_KEY = 'studyshop.oidc.next'

function toBase64Url(bytes: ArrayBuffer | Uint8Array): string {
  const arr = bytes instanceof Uint8Array ? bytes : new Uint8Array(bytes)
  let str = ''
  arr.forEach((b) => {
    str += String.fromCharCode(b)
  })
  return btoa(str).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '')
}

function randomString(length = 64): string {
  const bytes = new Uint8Array(length)
  crypto.getRandomValues(bytes)
  return toBase64Url(bytes)
}

async function sha256Base64Url(input: string): Promise<string> {
  const data = new TextEncoder().encode(input)
  const digest = await crypto.subtle.digest('SHA-256', data)
  return toBase64Url(digest)
}

export async function beginOidcLogin(nextPath = '/'): Promise<void> {
  const verifier = randomString(64)
  const challenge = await sha256Base64Url(verifier)
  const state = randomString(24)
  sessionStorage.setItem(PKCE_VERIFIER_KEY, verifier)
  sessionStorage.setItem(OIDC_STATE_KEY, state)
  sessionStorage.setItem(OIDC_NEXT_KEY, nextPath)

  const url = new URL(`${OIDC_AUTHORITY}/protocol/openid-connect/auth`)
  url.searchParams.set('client_id', OIDC_CLIENT_ID)
  url.searchParams.set('redirect_uri', OIDC_REDIRECT_URI)
  url.searchParams.set('response_type', 'code')
  url.searchParams.set('scope', 'openid profile')
  url.searchParams.set('state', state)
  url.searchParams.set('code_challenge', challenge)
  url.searchParams.set('code_challenge_method', 'S256')
  window.location.assign(url.toString())
}

export async function completeOidcLogin(searchParams: URLSearchParams): Promise<string> {
  const error = searchParams.get('error')
  if (error) {
    throw new Error(searchParams.get('error_description') || error)
  }
  const code = searchParams.get('code')
  const state = searchParams.get('state')
  const expectedState = sessionStorage.getItem(OIDC_STATE_KEY)
  const verifier = sessionStorage.getItem(PKCE_VERIFIER_KEY)
  if (!code || !state || !verifier || state !== expectedState) {
    throw new Error('Callback OIDC inválido (state/code/PKCE)')
  }

  const body = new URLSearchParams({
    grant_type: 'authorization_code',
    client_id: OIDC_CLIENT_ID,
    code,
    redirect_uri: OIDC_REDIRECT_URI,
    code_verifier: verifier,
  })

  const response = await fetch(`${OIDC_AUTHORITY}/protocol/openid-connect/token`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body,
  })
  if (!response.ok) {
    throw new Error(await response.text())
  }
  const json = (await response.json()) as { access_token: string }
  sessionStorage.removeItem(PKCE_VERIFIER_KEY)
  sessionStorage.removeItem(OIDC_STATE_KEY)
  return json.access_token
}

export function consumeOidcNextPath(): string {
  const next = sessionStorage.getItem(OIDC_NEXT_KEY) || '/'
  sessionStorage.removeItem(OIDC_NEXT_KEY)
  return next
}
