# Cenários de QA — StudyShop

Roteiro manual para validar o lab. Base URL do gateway: `http://localhost:8080`. Web: `http://localhost:3000`.

## Pré-condição

- Stack no ar (`scripts/up.ps1` ou Compose em `infra/`).
- Health agregado UP: `GET /api/health`.
- Produtos seed carregados (inventory na primeira subida).

---

## Cenário 1 — Health dos serviços

**Objetivo:** garantir que todos os backends respondem.

1. Abrir `/health` na web ou `GET http://localhost:8080/api/health`.
2. Verificar status geral `UP` e cada serviço `UP`.

**Esperado:** `api-gateway`, `orders-service`, `inventory-service`, `payments-service`, `notifications-service`, `inventory-grpc` = UP.

---

## Cenário 2 — Listar catálogo

1. Abrir página Catálogo (`/`).
2. Confirmar cards dos 5 produtos seed.

**Esperado:** produtos `prod-notebook`, `prod-mouse`, `prod-headset`, `prod-teclado`, `prod-raro` visíveis com preço e estoque.

**API:** `GET /api/products`

---

## Cenário 3 — Criar pedido feliz

1. No catálogo, adicionar 1× `prod-mouse`.
2. Informar e-mail em `input-customer-email`.
3. Clicar `btn-create-order`.
4. Seguir o link do pedido criado e aguardar status final (atualizar se necessário).

**Esperado:** pedido criado; status evolui até `CONFIRMED`; estoque do mouse decrementa.

**API:**

```http
POST /api/orders
Content-Type: application/json

{
  "customerEmail": "qa@studyshop.local",
  "forcePaymentFailure": false,
  "items": [{ "productId": "prod-mouse", "quantity": 1 }]
}
```

---

## Cenário 4 — Falha forçada de pagamento

1. Adicionar item ao carrinho.
2. Marcar `chk-force-payment-failure`.
3. Criar pedido.
4. Abrir detalhe e observar status/motivo.

**Esperado:** status final `CANCELLED` com motivo de pagamento (após `PAYMENT_FAILED`); estoque permanece reservado nesta versão simplificada (sem compensating transaction — ponto de estudo).

**API:** mesmo body com `"forcePaymentFailure": true` ou header `X-Force-Payment-Failure: true`.

---

## Cenário 5 — Estoque insuficiente

1. Usar `prod-raro` (estoque 1) e tentar quantidade 2 via API.

```http
POST /api/orders
{
  "customerEmail": "qa@studyshop.local",
  "items": [{ "productId": "prod-raro", "quantity": 2 }]
}
```

**Esperado:** pedido é criado e a saga publica `StockRejected`; status final `CANCELLED` com motivo de estoque insuficiente.

---

## Cenário 6 — Atualizar estoque (admin)

1. Ir em Estoque (`/admin/stock`).
2. Alterar quantidade de um produto e salvar.
3. Voltar ao catálogo e conferir estoque.

**API:** `PUT /api/products/{productId}/stock` body `{ "quantity": 20 }`

---

## Cenário 7 — Consultar pedido

1. Com um `orderId` válido, abrir `/orders/{id}` ou `GET /api/orders/{orderId}`.

**Esperado:** itens, total, e-mail, status e motivo preenchidos.

---

## Cenário 8 — Lista e filtro de pedidos

1. Em Pedidos, filtrar por status e atualizar.

**Esperado:** tabela reflete filtro; links abrem detalhe.

---

## Mapa `data-testid`

### Shell / navegação

| testid | Uso |
|--------|-----|
| `app-header` | Header |
| `brand-name` | Marca StudyShop |
| `nav-catalog` | Link catálogo |
| `nav-orders` | Link pedidos |
| `nav-admin-stock` | Link estoque |
| `nav-health` | Link health |

### Catálogo

| testid | Uso |
|--------|-----|
| `catalog-title` | Título |
| `catalog-error` | Erro |
| `product-list` | Grid |
| `product-{id}` | Card |
| `product-name-{id}` | Nome |
| `product-price-{id}` | Preço |
| `product-stock-{id}` | Estoque |
| `btn-add-{id}` | Adicionar ao carrinho |
| `cart-panel` | Carrinho |
| `input-customer-email` | E-mail |
| `chk-force-payment-failure` | Forçar falha |
| `cart-items` / `cart-item-{id}` | Itens |
| `btn-create-order` | Criar pedido |
| `order-created-alert` | Alerta sucesso |
| `link-created-order` | Link do pedido |

### Pedidos

| testid | Uso |
|--------|-----|
| `orders-title` | Título |
| `filter-order-status` | Select status |
| `btn-filter-orders` / `btn-refresh-orders` | Ações |
| `orders-error` | Erro |
| `orders-table` | Tabela |
| `order-row-{id}` | Linha |
| `link-order-{id}` | Link detalhe |
| `order-status-{id}` | Status na lista |

### Detalhe do pedido

| testid | Uso |
|--------|-----|
| `order-detail-title` | Título |
| `order-detail-error` | Erro |
| `order-detail` | Card |
| `order-id` | ID |
| `order-status` | Status |
| `order-status-reason` | Motivo |
| `order-total` | Total |
| `order-email` | E-mail |
| `order-force-fail` | Flag falha |
| `order-items` | Lista itens |

### Admin estoque

| testid | Uso |
|--------|-----|
| `admin-stock-title` | Título |
| `stock-ok` / `stock-error` | Feedback |
| `stock-table` | Tabela |
| `stock-row-{id}` | Linha |
| `input-stock-{id}` | Input quantidade |
| `btn-save-stock-{id}` | Salvar |

### Health

| testid | Uso |
|--------|-----|
| `health-title` | Título |
| `btn-refresh-health` | Atualizar |
| `health-error` | Erro |
| `health-overview` | Card |
| `health-overall` | Status geral |
| `health-services` | Lista |
| `health-{service}` | Item por serviço |

---

## Automação sugerida

- API: coleção Bruno em `bruno/study-shop/` + `scripts/smoke.ps1`.
- UI: Playwright/Cypress usando os `data-testid` acima.
