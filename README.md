# StudyShop — Lab QA de Microserviços

Monorepo educacional para praticar **QA em arquitetura moderna**: Spring Boot, gRPC, Kafka, MongoDB, React, Docker Compose, Helm, OpenTelemetry, Jaeger, Prometheus e Grafana.

> Ambiente de estudo. Não é produção.

## O que tem no lab

| Área | Tecnologia |
|------|------------|
| Backend | Java / Spring Boot |
| Contratos internos | gRPC (Protobuf) |
| Eventos | Apache Kafka (KRaft) |
| Dados | MongoDB 7 |
| API HTTP | api-gateway (REST + health) |
| Frontend | React + Vite |
| Local | Docker Compose |
| Kubernetes | Helm umbrella `study-shop` |
| Observabilidade | OTel → Jaeger / Prometheus / Grafana |
| API client | Bruno (`bruno/study-shop`) |

## Documentação

- [Arquitetura](docs/arquitetura.md)
- [Glossário](docs/glossario.md)
- [Status do pedido (saga)](docs/status-pedido.md)
- [Cenários de QA + data-testid](docs/cenarios-qa.md)
- [Observabilidade](docs/observabilidade.md)
- [Helm chart](infra/helm/study-shop/README.md)

## Pré-requisitos

- Docker Desktop (ou Engine + Compose v2)
- PowerShell 7+ (scripts)
- (Opcional) JDK 21+, Maven, Node 20+ para build local
- (Opcional) kind/minikube + Helm 3 para K8s

## Subir com Docker Compose

Na raiz do repositório:

```powershell
.\scripts\up.ps1
```

Equivale a `docker compose up -d --build` em `infra/`.

### URLs

| Serviço | URL |
|---------|-----|
| Web | http://localhost:3000 |
| API Gateway | http://localhost:8080 |
| Health | http://localhost:8080/api/health |
| Swagger UI | http://localhost:8080/swagger-ui.html |
| Grafana | http://localhost:3001 (`admin` / `admin`) |
| Jaeger | http://localhost:16686 |
| Prometheus | http://localhost:9090 |

### Smoke test

```powershell
.\scripts\smoke.ps1
```

Valida health, lista produtos e cria um pedido de exemplo.

### Parar

```powershell
.\scripts\down.ps1
.\scripts\down.ps1 -Volumes   # também apaga volumes
```

## API rápida

```http
GET  /api/health
GET  /api/products
POST /api/orders
GET  /api/orders/{orderId}
PUT  /api/products/{productId}/stock
```

Exemplo de pedido:

```json
{
  "customerEmail": "qa@studyshop.local",
  "forcePaymentFailure": false,
  "items": [{ "productId": "prod-mouse", "quantity": 1 }]
}
```

Coleção Bruno: pasta `bruno/study-shop/` (abra no cliente Bruno).

## Helm (kind / minikube)

```powershell
cd infra/helm/study-shop
helm dependency update
helm install study-shop . -n study-shop --create-namespace

kubectl port-forward -n study-shop svc/api-gateway 8080:8080
kubectl port-forward -n study-shop svc/web 3000:80
```

Build/load das imagens: ver [infra/helm/study-shop/README.md](infra/helm/study-shop/README.md).

## Estrutura do repositório

```
apps/
  api-gateway/
  orders-service/
  inventory-service/
  payments-service/
  notifications-service/
  web/
libs/
  proto/
infra/
  docker-compose.yml
  helm/study-shop/
  observability/
docs/
bruno/study-shop/
scripts/
  up.ps1
  down.ps1
  smoke.ps1
```

## Fluxo de estudo sugerido

1. Subir Compose e abrir a web.
2. Percorrer [cenários de QA](docs/cenarios-qa.md).
3. Criar pedido e inspecionar traces no Jaeger.
4. Rodar `smoke.ps1` e requests Bruno.
5. Instalar o chart Helm em kind e repetir port-forward.

## Licença / uso

Material para estudos e laboratório de QA. Ajuste imagens, senhas e hardening antes de qualquer uso real.
