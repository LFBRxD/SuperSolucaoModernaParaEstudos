import { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import { api, type Order } from '../api'

export default function OrderDetailPage() {
  const { orderId = '' } = useParams()
  const [order, setOrder] = useState<Order | null>(null)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    let active = true
    async function load() {
      try {
        const data = await api.getOrder(orderId)
        if (active) {
          setOrder(data)
          setError(null)
        }
      } catch (e) {
        if (active) setError(String((e as Error).message ?? e))
      }
    }
    void load()
    const timer = setInterval(() => void load(), 2000)
    return () => {
      active = false
      clearInterval(timer)
    }
  }, [orderId])

  return (
    <section>
      <div className="page-head">
        <h1 data-testid="order-detail-title">Detalhe do pedido</h1>
        <p>Polling a cada 2s para acompanhar status assíncrono.</p>
      </div>

      {error && <div className="alert error" data-testid="order-detail-error">{error}</div>}

      {order && (
        <div className="detail-card" data-testid="order-detail">
          <p>
            <strong>ID:</strong> <span data-testid="order-id">{order.orderId}</span>
          </p>
          <p>
            <strong>Status:</strong>{' '}
            <span className="status-pill" data-testid="order-status">
              {order.status}
            </span>
          </p>
          <p>
            <strong>Motivo:</strong> <span data-testid="order-status-reason">{order.statusReason}</span>
          </p>
          <p>
            <strong>Total:</strong> <span data-testid="order-total">R$ {order.total.toFixed(2)}</span>
          </p>
          <p>
            <strong>E-mail:</strong> <span data-testid="order-email">{order.customerEmail}</span>
          </p>
          <p>
            <strong>Force payment failure:</strong>{' '}
            <span data-testid="order-force-fail">{String(order.forcePaymentFailure)}</span>
          </p>
          <h2>Itens</h2>
          <ul data-testid="order-items">
            {order.items.map((item) => (
              <li key={item.productId}>
                {item.productName} × {item.quantity} — R$ {item.unitPrice.toFixed(2)}
              </li>
            ))}
          </ul>
        </div>
      )}
    </section>
  )
}
