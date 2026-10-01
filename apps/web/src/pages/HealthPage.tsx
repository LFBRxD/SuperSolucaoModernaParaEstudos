import { useEffect, useState } from 'react'
import { api, type HealthOverview } from '../api'

export default function HealthPage() {
  const [health, setHealth] = useState<HealthOverview | null>(null)
  const [error, setError] = useState<string | null>(null)

  async function load() {
    try {
      setError(null)
      setHealth(await api.health())
    } catch (e) {
      setError(String((e as Error).message ?? e))
    }
  }

  useEffect(() => {
    void load()
    const timer = setInterval(() => void load(), 5000)
    return () => clearInterval(timer)
  }, [])

  return (
    <section>
      <div className="page-head">
        <h1 data-testid="health-title">Health / Status</h1>
        <p>Visão agregada de readiness dos serviços (estudo de observabilidade).</p>
      </div>

      <button type="button" data-testid="btn-refresh-health" onClick={() => void load()}>
        Atualizar
      </button>

      {error && <div className="alert error" data-testid="health-error">{error}</div>}

      {health && (
        <div className="detail-card" data-testid="health-overview">
          <p>
            Overall:{' '}
            <span className="status-pill" data-testid="health-overall">
              {health.overall}
            </span>
          </p>
          <ul data-testid="health-services">
            {health.services.map((s) => (
              <li key={s.service} data-testid={`health-${s.service}`}>
                <strong>{s.service}</strong>: {s.status} — {s.detail}
              </li>
            ))}
          </ul>
        </div>
      )}
    </section>
  )
}
