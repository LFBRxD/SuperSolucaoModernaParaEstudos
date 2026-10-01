import { useEffect, useMemo, useState } from 'react'
import { Link } from 'react-router-dom'
import { api, type Product } from '../api'

type CartItem = { productId: string; quantity: number }

export default function CatalogPage() {
  const [products, setProducts] = useState<Product[]>([])
  const [cart, setCart] = useState<CartItem[]>([])
  const [email, setEmail] = useState('aluno@studyshop.local')
  const [forceFail, setForceFail] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [createdOrderId, setCreatedOrderId] = useState<string | null>(null)
  const [loading, setLoading] = useState(false)

  useEffect(() => {
    api.listProducts().then(setProducts).catch((e) => setError(String(e.message ?? e)))
  }, [])

  const totalItems = useMemo(() => cart.reduce((acc, i) => acc + i.quantity, 0), [cart])

  function addToCart(productId: string) {
    setCart((prev) => {
      const existing = prev.find((i) => i.productId === productId)
      if (existing) {
        return prev.map((i) =>
          i.productId === productId ? { ...i, quantity: i.quantity + 1 } : i,
        )
      }
      return [...prev, { productId, quantity: 1 }]
    })
  }

  async function createOrder() {
    setLoading(true)
    setError(null)
    setCreatedOrderId(null)
    try {
      const order = await api.createOrder({
        items: cart,
        customerEmail: email,
        forcePaymentFailure: forceFail,
      })
      setCreatedOrderId(order.orderId)
      setCart([])
    } catch (e) {
      setError(String((e as Error).message ?? e))
    } finally {
      setLoading(false)
    }
  }

  return (
    <section>
      <div className="page-head">
        <h1 data-testid="catalog-title">Catálogo</h1>
        <p>Selecione produtos e crie um pedido para exercitar a saga Kafka.</p>
      </div>

      {error && <div className="alert error" data-testid="catalog-error">{error}</div>}
      {createdOrderId && (
        <div className="alert ok" data-testid="order-created-alert">
          Pedido criado: <Link to={`/orders/${createdOrderId}`} data-testid="link-created-order">{createdOrderId}</Link>
        </div>
      )}

      <div className="grid products" data-testid="product-list">
        {products.map((p) => (
          <article key={p.productId} className="product-card" data-testid={`product-${p.productId}`}>
            <h2 data-testid={`product-name-${p.productId}`}>{p.name}</h2>
            <p>{p.description}</p>
            <div className="meta">
              <span data-testid={`product-price-${p.productId}`}>R$ {p.price.toFixed(2)}</span>
              <span data-testid={`product-stock-${p.productId}`}>Estoque: {p.quantity}</span>
            </div>
            <button
              type="button"
              data-testid={`btn-add-${p.productId}`}
              onClick={() => addToCart(p.productId)}
              disabled={p.quantity <= 0}
            >
              Adicionar
            </button>
          </article>
        ))}
      </div>

      <aside className="cart" data-testid="cart-panel">
        <h2>Carrinho ({totalItems})</h2>
        <label>
          E-mail
          <input
            data-testid="input-customer-email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </label>
        <label className="checkbox">
          <input
            type="checkbox"
            data-testid="chk-force-payment-failure"
            checked={forceFail}
            onChange={(e) => setForceFail(e.target.checked)}
          />
          Forçar falha de pagamento (QA)
        </label>
        <ul data-testid="cart-items">
          {cart.map((item) => {
            const product = products.find((p) => p.productId === item.productId)
            return (
              <li key={item.productId} data-testid={`cart-item-${item.productId}`}>
                {product?.name ?? item.productId} × {item.quantity}
              </li>
            )
          })}
        </ul>
        <button
          type="button"
          data-testid="btn-create-order"
          disabled={cart.length === 0 || loading}
          onClick={createOrder}
        >
          {loading ? 'Criando...' : 'Criar pedido'}
        </button>
      </aside>
    </section>
  )
}
