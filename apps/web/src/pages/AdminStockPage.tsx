import { useEffect, useState } from 'react'
import { api, type Product } from '../api'

export default function AdminStockPage() {
  const [products, setProducts] = useState<Product[]>([])
  const [drafts, setDrafts] = useState<Record<string, number>>({})
  const [message, setMessage] = useState<string | null>(null)
  const [error, setError] = useState<string | null>(null)

  async function load() {
    const list = await api.listProducts()
    setProducts(list)
    const next: Record<string, number> = {}
    list.forEach((p) => {
      next[p.productId] = p.quantity
    })
    setDrafts(next)
  }

  useEffect(() => {
    void load().catch((e) => setError(String(e.message ?? e)))
  }, [])

  async function save(productId: string) {
    setError(null)
    setMessage(null)
    try {
      await api.updateStock(productId, drafts[productId] ?? 0)
      setMessage(`Estoque atualizado: ${productId}`)
      await load()
    } catch (e) {
      setError(String((e as Error).message ?? e))
    }
  }

  return (
    <section>
      <div className="page-head">
        <h1 data-testid="admin-stock-title">Admin — Estoque</h1>
        <p>Ajuste quantidades para forçar StockRejected nos testes.</p>
      </div>

      {message && <div className="alert ok" data-testid="stock-ok">{message}</div>}
      {error && <div className="alert error" data-testid="stock-error">{error}</div>}

      <table className="table" data-testid="stock-table">
        <thead>
          <tr>
            <th>Produto</th>
            <th>SKU</th>
            <th>Quantidade</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {products.map((p) => (
            <tr key={p.productId} data-testid={`stock-row-${p.productId}`}>
              <td>{p.name}</td>
              <td>{p.sku}</td>
              <td>
                <input
                  type="number"
                  min={0}
                  data-testid={`input-stock-${p.productId}`}
                  value={drafts[p.productId] ?? 0}
                  onChange={(e) =>
                    setDrafts((prev) => ({ ...prev, [p.productId]: Number(e.target.value) }))
                  }
                />
              </td>
              <td>
                <button
                  type="button"
                  data-testid={`btn-save-stock-${p.productId}`}
                  onClick={() => void save(p.productId)}
                >
                  Salvar
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </section>
  )
}
