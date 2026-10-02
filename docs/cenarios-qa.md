# Cenários de QA — StudyShop

Roteiro manual para validar o lab. Base URL do gateway: `http://localhost:11001`. Web: `http://localhost:11000`.

Estudo longo, com uma meta por arquivo: [academia-qa/README.md](academia-qa/README.md). Matriz do que está automatizado: [academia-qa/matriz-rastreabilidade.md](academia-qa/matriz-rastreabilidade.md).

`scripts/smoke.ps1` e `scripts/smoke.sh` cobrem health, 401, login, pedido até `CONFIRMED`, 403/200 de estoque, cancelamento por pagamento, cancelamento por estoque e notificação.

## Pré-condição

- Stack no ar (`scripts/up.ps1` ou Compose em `infra/`).
- Health agregado UP: `GET /api/health` (público).
- Produtos seed carregados (inventory na primeira subida).
- Login Momento 1: `qa`/`qa123` (USER) ou `admin`/`admin123` (ADMIN). Ver [seguranca.md](seguranca.md).

---

## Cenário 0 — Auth JWT (401 / 403 / login)

**Objetivo:** validar borda de segurança.

1. `GET /api/products` sem header → **401**.
2. `POST /api/auth/login` com `qa`/`qa123` → `accessToken` + roles `USER`.
3. `GET /api/products` com `Authorization: Bearer …` → **200**.
4. `PUT /api/products/prod-mouse/stock` com token `qa` → **403**.
5. Login `admin` e mesmo PUT → **200**.
6. Na web: `/login` → entrar como `qa`; menu Estoque oculto; sair e entrar como `admin`.

**Smoke:** `./scripts/smoke.sh` ou `.\scripts\smoke.ps1`.

---

## Cenário 1 — Health dos serviços

**Objetivo:** garantir que todos os backends respondem.

1. Abrir `/health` na web ou `GET http://localhost:11001/api/health`.
2. Verificar status geral `UP` e cada serviço `UP`.

**Esperado:** `api-gateway`, `orders-service`, `inventory-service`, `payments-service`, `notifications-service`, `inventory-grpc` = UP.

---

## Cenário 2 — Listar catálogo

1. Fazer login na web.
2. Abrir página Catálogo (`/`).
3. Confirmar cards dos 5 produtos seed.

**Esperado:** produtos `prod-notebook`, `prod-mouse`, `prod-headset`, `prod-teclado`, `prod-raro` visíveis com preço e estoque.

**API:** `GET /api/products` + Bearer.

---

## Cenário 3 — Criar pedido feliz

1. No catálogo (já autenticado), adicionar 1× `prod-mouse`.
2. Informar e-mail em `input-customer-email`.
3. Clicar `btn-create-order`.
4. Seguir o link do pedido criado e aguardar status final (atualizar se necessário).

**Esperado:** pedido criado; status evolui até `CONFIRMED`; estoque do mouse decrementa.

**API:**

```http
POST /api/orders
Authorization: Bearer <token>
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
Authorization: Bearer <token>
{
  "customerEmail": "qa@studyshop.local",
  "items": [{ "productId": "prod-raro", "quantity": 2 }]
}
```

**Esperado:** pedido é criado e a saga publica `StockRejected`; status final `CANCELLED` com motivo de estoque insuficiente.

---

## Cenário 6 — Atualizar estoque (admin)

1. Login como `admin`.
2. Ir em Estoque (`/admin/stock`).
3. Alterar quantidade de um produto e salvar.
4. Voltar ao catálogo e conferir estoque.

**API:** `PUT /api/products/{productId}/stock` com Bearer ADMIN, body `{ "quantity": 20 }`

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
| `nav-admin-stock` | Link estoque (só ADMIN) |
| `nav-health` | Link health |
| `nav-login` | Link entrar |
| `btn-logout` | Sair |

### Login

| testid | Uso |
|--------|-----|
| `login-page` / `login-title` | Página |
| `login-form` | Form JWT local |
| `input-username` / `input-password` | Credenciais |
| `btn-login` | Submit local |
| `btn-oidc-login` | Keycloak (Momento 2) |
| `login-error` | Erro |
| `forbidden-page` | Sem role ADMIN |

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
