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

- [Comandos Linux/WSL (aprender na prática)](docs/comandos-linux-wsl.md)
- [Arquitetura](docs/arquitetura.md)
- [Glossário](docs/glossario.md)
- [Status do pedido (saga)](docs/status-pedido.md)
- [Cenários de QA + data-testid](docs/cenarios-qa.md)
- [Observabilidade](docs/observabilidade.md)
- [Helm chart](infra/helm/study-shop/README.md)

## Pré-requisitos

- Docker Engine + Compose v2 (Linux/WSL) ou Docker Desktop (Windows/Mac)
- `curl` e, de preferência, `jq` (smoke/API)
- (Opcional) scripts: Bash **ou** PowerShell 7+
- (Opcional) JDK 21+, Maven, Node 20+ para build local
- (Opcional) kind/minikube + Helm 3 para K8s

## Subir com Docker Compose

### Linux / WSL (recomendado para aprender os comandos)

Leia e pratique: **[docs/comandos-linux-wsl.md](docs/comandos-linux-wsl.md)**.

Comando principal:

```bash
cd infra
docker compose up -d --build
```

Atalhos:

```bash
chmod +x scripts/*.sh
./scripts/up.sh
./scripts/smoke.sh
./scripts/down.sh
./scripts/down.sh --volumes
```

### Windows (PowerShell)

```powershell
.\scripts\up.ps1
.\scripts\smoke.ps1
.\scripts\down.ps1
.\scripts\down.ps1 -Volumes
```

### URLs

Portas sequenciais a partir de **11000** (evita conflito com outros projetos locais).

| Serviço | URL / porta |
|---------|-------------|
| Web | http://localhost:11000 |
| API Gateway | http://localhost:11001 |
| Health | http://localhost:11001/api/health |
| Swagger UI | http://localhost:11001/swagger-ui.html |
| Orders HTTP / gRPC | 11002 / 11003 |
| Inventory HTTP / gRPC | 11004 / 11005 |
| Payments | 11006 |
| Notifications | 11007 |
| MongoDB (host) | 11008 |
| Kafka (host) | 11009 |
| Grafana | http://localhost:11010 (`admin` / `admin`) |
| Jaeger | http://localhost:11011 |
| Prometheus | http://localhost:11012 |
| OTel gRPC / HTTP | 11013 / 11014 |

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

kubectl port-forward -n study-shop svc/api-gateway 11001:11001
kubectl port-forward -n study-shop svc/web 11000:80
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
  up.sh / down.sh / smoke.sh
  up.ps1 / down.ps1 / smoke.ps1
```

## Fluxo de estudo sugerido

1. Ler [comandos Linux/WSL](docs/comandos-linux-wsl.md) e subir o Compose.
2. Abrir a web e percorrer [cenários de QA](docs/cenarios-qa.md).
3. Criar pedido e inspecionar traces no Jaeger.
4. Repetir com `curl`/`./scripts/smoke.sh` e Bruno.
5. Instalar o chart Helm em kind e repetir port-forward.

## Licença / uso

Material para estudos e laboratório de QA. Ajuste imagens, senhas e hardening antes de qualquer uso real.
