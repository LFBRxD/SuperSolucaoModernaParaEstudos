import { BrowserRouter, NavLink, Route, Routes } from 'react-router-dom'
import CatalogPage from './pages/CatalogPage'
import OrdersPage from './pages/OrdersPage'
import OrderDetailPage from './pages/OrderDetailPage'
import AdminStockPage from './pages/AdminStockPage'
import HealthPage from './pages/HealthPage'
import LoginPage from './pages/LoginPage'
import OidcCallbackPage from './pages/OidcCallbackPage'
import RequireAuth from './components/RequireAuth'
import { clearSession, getUsername, hasRole, isAuthenticated } from './auth'
import './App.css'

export default function App() {
  const loggedIn = isAuthenticated()
  const username = getUsername()
  const isAdmin = hasRole('ADMIN')

  return (
    <BrowserRouter>
      <div className="app-shell">
        <header className="topbar" data-testid="app-header">
          <div className="brand">
            <span className="brand-mark">SS</span>
            <div>
              <strong data-testid="brand-name">StudyShop</strong>
              <p>Laboratório QA — stack moderna</p>
            </div>
          </div>
          <nav className="nav">
            <NavLink to="/" data-testid="nav-catalog" end>
              Catálogo
            </NavLink>
            <NavLink to="/orders" data-testid="nav-orders">
              Pedidos
            </NavLink>
            {isAdmin && (
              <NavLink to="/admin/stock" data-testid="nav-admin-stock">
                Estoque
              </NavLink>
            )}
            <NavLink to="/health" data-testid="nav-health">
              Health
            </NavLink>
            {loggedIn ? (
              <button
                type="button"
                className="nav-logout"
                data-testid="btn-logout"
                onClick={() => {
                  clearSession()
                  window.location.assign('/login')
                }}
              >
                Sair ({username})
              </button>
            ) : (
              <NavLink to="/login" data-testid="nav-login">
                Entrar
              </NavLink>
            )}
          </nav>
        </header>
        <main className="content">
          <Routes>
            <Route path="/login" element={<LoginPage />} />
            <Route path="/login/callback" element={<OidcCallbackPage />} />
            <Route path="/health" element={<HealthPage />} />
            <Route
              path="/"
              element={
                <RequireAuth>
                  <CatalogPage />
                </RequireAuth>
              }
            />
            <Route
              path="/orders"
              element={
                <RequireAuth>
                  <OrdersPage />
                </RequireAuth>
              }
            />
            <Route
              path="/orders/:orderId"
              element={
                <RequireAuth>
                  <OrderDetailPage />
                </RequireAuth>
              }
            />
            <Route
              path="/admin/stock"
              element={
                <RequireAuth role="ADMIN">
                  <AdminStockPage />
                </RequireAuth>
              }
            />
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  )
}
