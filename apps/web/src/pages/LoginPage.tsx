import { useEffect, useState } from 'react'
import { Link, useNavigate, useSearchParams } from 'react-router-dom'
import { api, currentAuthMode } from '../api'
import { beginOidcLogin } from '../oidc'
import { isAuthenticated } from '../auth'

export default function LoginPage() {
  const navigate = useNavigate()
  const [params] = useSearchParams()
  const next = params.get('next') || '/'
  const mode = currentAuthMode()
  const [username, setUsername] = useState('qa')
  const [password, setPassword] = useState('qa123')
  const [error, setError] = useState<string | null>(null)
  const [loading, setLoading] = useState(false)

  useEffect(() => {
    if (isAuthenticated()) {
      navigate(next, { replace: true })
    }
  }, [navigate, next])

  async function onSubmit(e: React.FormEvent) {
    e.preventDefault()
    setError(null)
    setLoading(true)
    try {
      await api.login(username, password)
      window.location.assign(next)
    } catch (err) {
      setError(String((err as Error).message ?? err))
    } finally {
      setLoading(false)
    }
  }

  return (
    <section className="login-page" data-testid="login-page">
      <div className="page-head">
        <h1 data-testid="login-title">Entrar</h1>
        <p>
          {mode === 'oidc'
            ? 'Momento 2 — autenticação via Keycloak (OIDC).'
            : 'Momento 1 — JWT local no api-gateway.'}
        </p>
      </div>

      {error && (
        <div className="alert error" data-testid="login-error">
          {error}
        </div>
      )}

      {mode === 'oidc' ? (
        <div className="cart">
          <button
            type="button"
            data-testid="btn-oidc-login"
            onClick={() => void beginOidcLogin(next)}
          >
            Entrar com Keycloak
          </button>
          <p className="muted-note">
            Usuários seed: <code>qa</code> / <code>qa123</code> e <code>admin</code> / <code>admin123</code>
          </p>
        </div>
      ) : (
        <form className="cart" onSubmit={(e) => void onSubmit(e)} data-testid="login-form">
          <label>
            Usuário
            <input
              data-testid="input-username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              autoComplete="username"
            />
          </label>
          <label>
            Senha
            <input
              type="password"
              data-testid="input-password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              autoComplete="current-password"
            />
          </label>
          <button type="submit" data-testid="btn-login" disabled={loading}>
            {loading ? 'Entrando…' : 'Entrar'}
          </button>
          <p className="muted-note">
            Seed: <code>qa</code>/<code>qa123</code> (USER) · <code>admin</code>/<code>admin123</code> (ADMIN)
          </p>
        </form>
      )}

      <p>
        <Link to="/health" data-testid="link-health-public">
          Health (público)
        </Link>
      </p>
    </section>
  )
}
