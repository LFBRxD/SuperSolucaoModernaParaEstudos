import { BrowserRouter, NavLink, Route, Routes } from 'react-router-dom'
import CatalogPage from './pages/CatalogPage'
import OrdersPage from './pages/OrdersPage'
import OrderDetailPage from './pages/OrderDetailPage'
import AdminStockPage from './pages/AdminStockPage'
import HealthPage from './pages/HealthPage'
import './App.css'

export default function App() {
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
            <NavLink to="/" data-testid="nav-catalog" end>Catálogo</NavLink>
            <NavLink to="/orders" data-testid="nav-orders">Pedidos</NavLink>
            <NavLink to="/admin/stock" data-testid="nav-admin-stock">Estoque</NavLink>
            <NavLink to="/health" data-testid="nav-health">Health</NavLink>
          </nav>
        </header>
        <main className="content">
          <Routes>
            <Route path="/" element={<CatalogPage />} />
            <Route path="/orders" element={<OrdersPage />} />
            <Route path="/orders/:orderId" element={<OrderDetailPage />} />
            <Route path="/admin/stock" element={<AdminStockPage />} />
            <Route path="/health" element={<HealthPage />} />
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  )
}
