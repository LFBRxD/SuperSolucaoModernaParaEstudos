import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { api, type Order } from '../api'

export default function OrdersPage() {
  const [orders, setOrders] = useState<Order[]>([])
  const [status, setStatus] = useState('')
  const [error, setError] = useState<string | null>(null)

  async function load(filter?: string) {
    try {
      setError(null)
      setOrders(await api.listOrders(filter || undefined))
    } catch (e) {
      setError(String((e as Error).message ?? e))
    }
  }

  useEffect(() => {
    void load()
  }, [])

  return (
    <section>
      <div className="page-head">
        <h1 data-testid="orders-title">Pedidos</h1>
        <p>Filtre por status para validar a evolução da saga.</p>
      </div>

      <div className="toolbar">
        <select
          data-testid="filter-order-status"
          value={status}
          onChange={(e) => setStatus(e.target.value)}
        >
          <option value="">Todos</option>
          <option value="CREATED">CREATED</option>
          <option value="AWAITING_STOCK">AWAITING_STOCK</option>
          <option value="AWAITING_PAYMENT">AWAITING_PAYMENT</option>
          <option value="CONFIRMED">CONFIRMED</option>
          <option value="CANCELLED">CANCELLED</option>
        </select>
        <button type="button" data-testid="btn-filter-orders" onClick={() => void load(status)}>
          Filtrar
        </button>
        <button type="button" data-testid="btn-refresh-orders" onClick={() => void load(status)}>
          Atualizar
        </button>
      </div>

      {error && <div className="alert error" data-testid="orders-error">{error}</div>}

      <table className="table" data-testid="orders-table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Status</th>
            <th>Total</th>
            <th>Atualizado</th>
          </tr>
        </thead>
        <tbody>
          {orders.map((o) => (
            <tr key={o.orderId} data-testid={`order-row-${o.orderId}`}>
              <td>
                <Link to={`/orders/${o.orderId}`} data-testid={`link-order-${o.orderId}`}>
                  {o.orderId}
                </Link>
              </td>
              <td data-testid={`order-status-${o.orderId}`}>{o.status}</td>
              <td>R$ {o.total.toFixed(2)}</td>
              <td>{o.updatedAt}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </section>
  )
}
