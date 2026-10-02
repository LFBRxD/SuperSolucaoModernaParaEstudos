# StudyShop Helm Chart

Chart umbrella educacional para o laboratório QA StudyShop. Empacota MongoDB, Kafka e os microserviços em um único `helm install`.

> **Aviso:** charts de estudo (single-replica). Não use em produção.

## Pré-requisitos

- Kubernetes local: [kind](https://kind.sigs.k8s.io/) ou [minikube](https://minikube.sigs.k8s.io/)
- Helm 3.14+
- Imagens Docker disponíveis no cluster (`studyshop/*`)

## Build e load das imagens (kind)

Na raiz do repositório:

```bash
docker build -t studyshop/orders-service:1.0.0 -f apps/orders-service/Dockerfile .
docker build -t studyshop/inventory-service:1.0.0 -f apps/inventory-service/Dockerfile .
docker build -t studyshop/payments-service:1.0.0 -f apps/payments-service/Dockerfile .
docker build -t studyshop/notifications-service:1.0.0 -f apps/notifications-service/Dockerfile .
docker build -t studyshop/api-gateway:1.0.0 -f apps/api-gateway/Dockerfile .
docker build -t studyshop/web:1.0.0 -f apps/web/Dockerfile .

kind load docker-image studyshop/orders-service:1.0.0
kind load docker-image studyshop/inventory-service:1.0.0
kind load docker-image studyshop/payments-service:1.0.0
kind load docker-image studyshop/notifications-service:1.0.0
kind load docker-image studyshop/api-gateway:1.0.0
kind load docker-image studyshop/web:1.0.0
```

Com minikube, use `minikube image load <image>` ou o Docker daemon do minikube (`eval $(minikube docker-env)`).

## Instalar

```bash
cd infra/helm/study-shop
helm dependency update
helm install study-shop . -n study-shop --create-namespace
```

Verificar:

```bash
kubectl get pods -n study-shop
kubectl get svc -n study-shop
```

## Port-forward

API Gateway (REST):

```bash
kubectl port-forward -n study-shop svc/api-gateway 11001:11001
```

Frontend:

```bash
kubectl port-forward -n study-shop svc/web 11000:80
```

Acesse:

- Web: http://localhost:11000
- Gateway health: http://localhost:11001/api/health
- Swagger: http://localhost:11001/swagger-ui.html

Se o Service `web` estiver como NodePort (`30080`), em kind/minikube também é possível mapear o node:

```bash
# minikube
minikube service web -n study-shop --url
```

## Desinstalar

```bash
helm uninstall study-shop -n study-shop
kubectl delete namespace study-shop
```

## Estrutura

```
study-shop/
  Chart.yaml          # umbrella + dependencies file://./charts/*
  values.yaml         # defaults (portas alinhadas ao docker-compose)
  charts/
    mongodb/
    kafka/
    orders-service/
    inventory-service/
    payments-service/
    notifications-service/
    api-gateway/
    web/
```

## DNS interno (K8s)

Com `fullnameOverride`, os Services usam nomes estáveis:

| Serviço | DNS | Portas |
|---------|-----|--------|
| mongodb | `mongodb:27017` | 27017 |
| kafka | `kafka:9092` | 9092 |
| orders-service | `orders-service` | 11002 / 11003 |
| inventory-service | `inventory-service` | 11004 / 11005 |
| payments-service | `payments-service` | 11006 |
| notifications-service | `notifications-service` | 11007 |
| api-gateway | `api-gateway` | 11001 |
| web | `web` | 80 |
| web | `web` | 80 |

## Observabilidade no cluster

O chart **não** inclui OTel/Grafana/Prometheus nem CronJob. Para o lab completo de telemetria, use o Docker Compose em `infra/docker-compose.yml`. Agendamento de plataforma é estudo da semana 12 da academia, não um recurso já instalado por este chart.

## Segurança (lab)

O subchart `api-gateway` inclui `STUDYSHOP_AUTH_MODE=local` e `JWT_SECRET` (Momento 1).

Overlays Compose (local, fora do Helm):

- `infra/docker-compose.oidc.yml` — Keycloak / OIDC
- `infra/docker-compose.mtls.yml` — mTLS gRPC

Trilha completa: [docs/seguranca.md](../../../docs/seguranca.md).
