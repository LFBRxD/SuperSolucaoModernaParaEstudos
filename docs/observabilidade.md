# Observabilidade — StudyShop

Como usar Grafana, Jaeger e Prometheus no lab (Docker Compose em `infra/`).

## URLs locais

| Ferramenta | URL | Credenciais |
|------------|-----|-------------|
| Grafana | http://localhost:10010 | `admin` / `admin` |
| Jaeger UI | http://localhost:10011 | — |
| Prometheus | http://localhost:10012 | — |
| OTel Collector (host) | `10013` (gRPC), `10014` (HTTP OTLP) | — |

Subir a stack:

```powershell
.\scripts\up.ps1
```

## Fluxo de telemetria

```
Serviços Spring (OTEL_*)
        │  OTLP HTTP :4318 (rede interna)
        ▼
  otel-collector
     ├──► Jaeger   (traces)
     └──► Prometheus (métricas / scrape conforme config)
              │
              ▼
           Grafana
```

Variáveis típicas nos serviços:

- `OTEL_SERVICE_NAME` — nome no Jaeger
- `OTEL_EXPORTER_OTLP_ENDPOINT=http://otel-collector:4318`
- `OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf`

## Jaeger — traces

1. Abra http://localhost:10011
2. Em **Service**, selecione `api-gateway`, `orders-service`, etc.
3. **Find Traces** após criar um pedido pela UI ou pelo smoke script.
4. Abra um trace e confira spans HTTP/gRPC/Kafka (conforme instrumentação).

**Exercício QA:** compare um pedido feliz vs. `forcePaymentFailure=true` e anote diferenças de spans/erros.

## Prometheus — métricas

1. Abra http://localhost:10012
2. Em **Graph**, consulte por exemplo:
   - `up` — alvos scrapeados
   - métricas Spring (`http_server_requests_*`, se expostas e scrapeadas)
3. Confira **Status → Targets** para ver quem está UP.

O arquivo de scrape está em `infra/observability/prometheus/prometheus.yml`.

## Grafana — dashboards

1. Abra http://localhost:10010 (`admin`/`admin`)
2. Datasources são provisionados em `infra/observability/grafana/provisioning/datasources/`
3. Dashboards em `infra/observability/grafana/provisioning/dashboards/`
4. Abra o dashboard **StudyShop** (JSON `studyshop.json`) com painel básico de `up{}`

**Dicas:**

- Explore → Prometheus → query `up`
- Adicione painéis de latência/taxa de erro quando as métricas Actuator estiverem no scrape
- Linke Jaeger como datasource de traces no Grafana (se configurado no provisioning)

## Checklist rápido

1. `curl http://localhost:10001/api/health` → UP  
2. Criar pedido (UI ou smoke)  
3. Jaeger mostra trace do `api-gateway`  
4. Prometheus `up` retorna séries  
5. Grafana carrega dashboard StudyShop  

## Limitações do lab

- Logs OTel desligados (`OTEL_LOGS_EXPORTER=none`)
- Métricas OTel desligadas nos serviços (`OTEL_METRICS_EXPORTER=none`); Prometheus depende do scrape HTTP Actuator/config
- Sem sampling reduzido (probabilidade alta no lab) — volume de traces é aceitável só localmente
