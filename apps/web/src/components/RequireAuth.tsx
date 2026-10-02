import { Navigate, useLocation } from 'react-router-dom'
import { hasRole, isAuthenticated } from '../auth'

type Props = {
  children: React.ReactNode
  role?: string
}

export default function RequireAuth({ children, role }: Props) {
  const location = useLocation()
  if (!isAuthenticated()) {
    return <Navigate to={`/login?next=${encodeURIComponent(location.pathname)}`} replace />
  }
  if (role && !hasRole(role)) {
    return (
      <section data-testid="forbidden-page">
        <div className="alert error">
          Acesso negado — role <code>{role}</code> necessária.
        </div>
      </section>
    )
  }
  return <>{children}</>
}
