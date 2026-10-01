# Comandos Linux / WSL — StudyShop

Guia para **aprender os comandos reais**. Os scripts em `scripts/*.sh` só encapsulam o que está aqui.

> No WSL, clone e rode o repo dentro do filesystem Linux (`~/projetos/...`), não em `/mnt/c/...`.

## 1. Pré-requisitos

```bash
# Docker Compose v2
docker version
docker compose version

# Úteis para smoke/API
sudo apt update
sudo apt install -y curl jq
```

Opcional (build local sem Docker):

```bash
java -version          # 21+
mvn -version
node -v                # 20+
npm -v
```

Opcional (Kubernetes):

```bash
kubectl version --client
helm version
kind version           # ou minikube
```

---

## 2. Subir a stack (Compose)

Na **raiz** do repositório:

```bash
cd infra
docker compose up -d --build
```

O que cada flag faz:

| Parte | Significado |
|-------|-------------|
| `docker compose` | CLI do Compose (arquivo `docker-compose.yml` no diretório atual) |
| `up` | Cria e inicia containers |
| `-d` | Detached (background) |
| `--build` | Reconstrói imagens antes de subir |

Atalho equivalente:

```bash
chmod +x scripts/*.sh   # só na primeira vez
./scripts/up.sh
```

### Ver o que está rodando

```bash
cd infra
docker compose ps
docker compose logs -f api-gateway
docker compose logs -f orders-service
# Ctrl+C sai do follow; containers continuam no ar
```

### Health e UI

```bash
curl -s http://localhost:10001/api/health | jq
# Web:        http://localhost:10000
# Swagger:    http://localhost:10001/swagger-ui.html
# Grafana:    http://localhost:10010  (admin/admin)
# Jaeger:     http://localhost:10011
# Prometheus: http://localhost:10012
```

Portas completas: [README](../README.md) e [arquitetura](arquitetura.md).

---

## 3. Smoke / API com curl (aprender QA de API)

### Health

```bash
curl -s http://localhost:10001/api/health | jq
```

### Listar produtos

```bash
curl -s http://localhost:10001/api/products | jq
```

### Criar pedido (caminho feliz)

```bash
curl -s -X POST http://localhost:10001/api/orders \
  -H "Content-Type: application/json" \
  -d '{
    "customerEmail": "aluno@studyshop.local",
    "forcePaymentFailure": false,
    "items": [{ "productId": "prod-mouse", "quantity": 1 }]
  }' | jq
```

Guarde o `orderId` da resposta.

### Consultar pedido (status da saga)

```bash
ORDER_ID="cole-o-uuid-aqui"
curl -s "http://localhost:10001/api/orders/$ORDER_ID" | jq

# polling simples a cada 2s
watch -n 2 "curl -s http://localhost:10001/api/orders/$ORDER_ID | jq '{status,statusReason}'"
```

### Falha forçada de pagamento (cenário negativo)

```bash
curl -s -X POST http://localhost:10001/api/orders \
  -H "Content-Type: application/json" \
  -H "X-Force-Payment-Failure: true" \
  -d '{
    "customerEmail": "qa-fail@studyshop.local",
    "forcePaymentFailure": true,
    "items": [{ "productId": "prod-mouse", "quantity": 1 }]
  }' | jq
```

### Ajustar estoque (admin)

```bash
curl -s -X PUT http://localhost:10001/api/products/prod-raro/stock \
  -H "Content-Type: application/json" \
  -d '{"quantity": 0}' | jq
```

Atalho:

```bash
./scripts/smoke.sh
# ou
BASE_URL=http://localhost:10001 ./scripts/smoke.sh
```

Mais cenários: [cenarios-qa.md](cenarios-qa.md).

---

## 4. Parar a stack

```bash
cd infra
docker compose down          # para e remove containers
docker compose down -v       # também apaga volumes (Mongo/Grafana)
```

Atalho:

```bash
./scripts/down.sh
./scripts/down.sh --volumes
```

---

## 5. Build local (sem Compose dos apps)

Útil para debugar um serviço isolado (Mongo/Kafka ainda via Compose).

### Só infra

```bash
cd infra
docker compose up -d mongodb kafka
```

### Backend Maven

```bash
# na raiz
mvn -DskipTests package
mvn -pl apps/api-gateway -am spring-boot:run
# outros módulos: apps/orders-service, inventory-service, ...
```

### Frontend Vite

```bash
cd apps/web
npm install
npm run dev
# sobe em http://localhost:10000 e faz proxy /api -> :10001
```

---

## 6. Observabilidade (comandos úteis)

```bash
# Targets do Prometheus
curl -s http://localhost:10012/api/v1/targets | jq '.data.activeTargets[] | {job:.labels.job, health}'

# Abrir UIs no browser (WSL + Windows)
# http://localhost:10010  Grafana
# http://localhost:10011  Jaeger
# http://localhost:10012  Prometheus
```

Detalhes: [observabilidade.md](observabilidade.md).

---

## 7. Kubernetes + Helm (visão de aprendizado)

Pré: cluster local (`kind` ou `minikube`) e imagens carregadas — ver [infra/helm/study-shop/README.md](../infra/helm/study-shop/README.md).

```bash
cd infra/helm/study-shop

# Empacota/atualiza subcharts locais
helm dependency update

# Instala no namespace study-shop
helm install study-shop . -n study-shop --create-namespace

# Observa pods/services
kubectl get pods -n study-shop
kubectl get svc -n study-shop
kubectl logs -n study-shop deploy/api-gateway -f

# Expõe no localhost (mesma faixa de portas do lab)
kubectl port-forward -n study-shop svc/api-gateway 10001:10001
# em outro terminal:
kubectl port-forward -n study-shop svc/web 10000:80

# Remover
helm uninstall study-shop -n study-shop
kubectl delete namespace study-shop
```

---

## 8. Troubleshooting rápido

```bash
cd infra

# Status e healthchecks
docker compose ps

# Logs de um serviço com erro
docker compose logs --tail=100 orders-service
docker compose logs --tail=100 kafka

# Rebuild forçado de um serviço
docker compose up -d --build api-gateway

# Entrar no container (shell)
docker compose exec api-gateway sh
```

Porta em uso no host:

```bash
ss -lptn 'sport = :10001'    # Linux
# ou
sudo lsof -i :10001
```

---

## Mapa mental

```
aprender Compose  →  docker compose up/ps/logs/down
aprender API/QA   →  curl + jq (+ Bruno)
aprender eventos  →  criar pedido e ver status mudar
aprender obs      →  Jaeger / Prometheus / Grafana
aprender K8s      →  helm install + kubectl get/logs/port-forward
```
