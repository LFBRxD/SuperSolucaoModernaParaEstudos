import { useEffect, useState } from 'react'
import { useSearchParams } from 'react-router-dom'
import { api } from '../api'
import { completeOidcLogin, consumeOidcNextPath } from '../oidc'

export default function OidcCallbackPage() {
  const [params] = useSearchParams()
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    void (async () => {
      try {
        const accessToken = await completeOidcLogin(params)
        api.acceptOidcToken(accessToken)
        window.location.assign(consumeOidcNextPath())
      } catch (e) {
        setError(String((e as Error).message ?? e))
      }
    })()
  }, [params])

  if (error) {
    return (
      <section data-testid="oidc-callback-error">
        <div className="alert error">{error}</div>
      </section>
    )
  }

  return (
    <section data-testid="oidc-callback">
      <p>Concluindo login OIDC…</p>
    </section>
  )
}
