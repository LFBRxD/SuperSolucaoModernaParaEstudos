# Arquitetura — StudyShop QA Lab

Visão geral da solução educacional **StudyShop**: e-commerce de estudo focado em microserviços, eventos, gRPC e observabilidade para prática de QA.

## Contexto

O monorepo simula um fluxo de compra completo:

1. Catálogo e estoque (inventory)
2. Criação de pedido (orders)
3. Reserva de estoque e pagamento via saga/eventos (Kafka)
4. Notificações persistidas
5. API HTTP unificada (api-gateway)
6. UI React (web)

Tudo roda localmente via **Docker Compose** (lab completo) ou **Helm** em kind/minikube (deploy K8s educativo).

## Diagrama lógico

```
                    ┌─────────────┐
                    │    web      │
                    │  (React)    │
                    └──────┬──────┘
                           │ HTTP
                    ┌──────▼──────┐
                    │ api-gateway │  REST → gRPC / HTTP
                    │   :8080     │
                    └───┬────┬────┘
           gRPC :9081   │    │   gRPC :9082
         ┌──────────────┘    └──────────────┐
         ▼                                  ▼
┌─────────────────┐               ┌──────────────────┐
│ orders-service  │               │ inventory-service│
│  :8081 / :9081  │               │  :8082 / :9082   │
└────────┬────────┘               └────────┬─────────┘
         │                                 │
         │         Kafka topics            │
         └─────────────┬───────────────────┘
                       │
         ┌─────────────┼─────────────┐
         ▼             ▼             ▼
┌──────────────┐ ┌───────────┐ ┌────────────────────┐
│payments-svc  │ │inventory  │ │notifications-svc   │
│   :8083      │ │ (reserve) │ │   :8084            │
└──────────────┘ └───────────┘ └────────────────────┘
         │             │             │
         └─────────────┴─────────────┘
                       │
                       ▼
                 ┌──────────┐
                 │ MongoDB  │  (DBs lógicos por serviço)
                 │  :27017  │
                 └──────────┘
```

## Componentes

| Componente | Responsabilidade | Protocolo |
|------------|------------------|-----------|
| **web** | Catálogo, carrinho, pedidos, admin de estoque, health | HTTP → gateway |
| **api-gateway** | Fachada REST, health agregado, proxy de notificações | REST + gRPC client |
| **orders-service** | CRUD de pedidos, publica `OrderCreated` | HTTP + gRPC + Kafka |
| **inventory-service** | Produtos/estoque, reserva em evento | HTTP + gRPC + Kafka |
| **payments-service** | Consome pedido, simula pagamento | Kafka + Mongo |
| **notifications-service** | Persiste notificações de status | Kafka + REST |
| **mongodb** | Persistência por database lógico | Wire protocol |
| **kafka** | Barramento de eventos (KRaft) | Kafka protocol |

## Fluxo de pedido (saga educacional)

1. Cliente cria pedido via `POST /api/orders` no gateway.
2. Gateway consulta produtos no inventory (gRPC) e chama orders (gRPC).
3. Orders persiste o pedido e publica evento **OrderCreated** no Kafka.
4. Inventory reserva estoque; Payments processa (ou falha se `forcePaymentFailure`).
5. Orders atualiza status a partir dos eventos da saga e publica mudança de status.
6. Notifications grava mensagem; UI/API listam notificações e status do pedido.

Estados típicos: `PENDING` → `RESERVED` / `PAYMENT_*` → `COMPLETED` ou `FAILED` / `CANCELLED` (conforme implementação dos listeners).

## Comunicação

- **Síncrona:** REST (browser ↔ gateway) e gRPC (gateway ↔ orders/inventory).
- **Assíncrona:** Kafka entre orders, inventory, payments e notifications.
- **Health:** gateway agrega Actuator HTTP + checagem gRPC do inventory.

## Dados seed (inventory)

| productId | Nome | Estoque inicial |
|-----------|------|-----------------|
| `prod-notebook` | Notebook Study Pro | 10 |
| `prod-mouse` | Mouse Ergonômico | 50 |
| `prod-headset` | Headset QA Focus | 25 |
| `prod-teclado` | Teclado Mecânico | 15 |
| `prod-raro` | Item Escasso | 1 |

## Observabilidade

No Compose: OTel Collector → Jaeger (traces) + Prometheus (métricas) + Grafana (dashboards).

Variáveis `OTEL_*` nos serviços exportam traces OTLP HTTP para `otel-collector:4318`.

## Portas (Compose)

| Serviço | Host |
|---------|------|
| web | 3000 → 80 |
| api-gateway | 8080 |
| orders | 8081, 9081 |
| inventory | 8082, 9082 |
| payments | 8083 |
| notifications | 8084 |
| mongodb | 27017 |
| kafka | 9092 |
| jaeger UI | 16686 |
| prometheus | 9090 |
| grafana | 3001 |

## Limitações do lab

- Mongo/Kafka single-node, sem TLS/auth.
- Sem API gateway de produção (Spring Cloud Gateway avançado, rate limit, etc.).
- Pagamento simulado (flag de falha forçada para QA negativo).
- Charts Helm espelham o Compose de forma didática, não HA.
