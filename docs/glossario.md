# Glossário — StudyShop

Termos usados no lab, em português.

## Kafka

**Apache Kafka** é uma plataforma de streaming de eventos. Serviços publicam e consomem **tópicos** de forma assíncrona, desacoplando produtores e consumidores.

No StudyShop: orders publica a criação do pedido; inventory, payments e notifications reagem sem chamada HTTP direta.

- **Broker:** nó que armazena e serve os tópicos.
- **Tópico:** fila lógica de mensagens (ex.: eventos de pedido).
- **Consumer group:** conjunto de consumidores que dividem o processamento.
- **KRaft:** modo do Kafka sem ZooKeeper (usado no Compose com Bitnami).

## gRPC

**gRPC** é um framework RPC sobre HTTP/2 com contratos **Protocol Buffers** (`.proto`). Ideal para comunicação interna tipada e de baixa latência.

No StudyShop: o api-gateway chama `orders-service` (porta 9081) e `inventory-service` (9082) via gRPC; a UI só vê REST.

- **Proto:** definição de mensagens e serviços.
- **Stub/client:** código gerado para chamar o serviço remoto.
- **plaintext:** sem TLS — aceitável só no lab.

## Helm

**Helm** é o gerenciador de pacotes do Kubernetes. Um **chart** descreve Deployments, Services e configs.

No StudyShop: o chart umbrella `study-shop` agrupa subcharts (`mongodb`, `kafka`, microserviços, `web`) e permite `helm install` único.

- **Umbrella chart:** chart pai com `dependencies`.
- **values.yaml:** parâmetros (imagem, env, portas).
- **Release:** instalação nomeada de um chart no cluster.

## MongoDB

**MongoDB** é um banco de documentos (JSON/BSON). Cada microserviço usa um **database lógico** na mesma instância (`orders`, `inventory`, `payments`, `notifications`).

- **URI:** `mongodb://mongodb:27017/<database>`.
- **Coleção:** equivalente aproximado a tabela.
- **Seed:** carga inicial de produtos no inventory.

## OpenTelemetry (OTel)

**OpenTelemetry** é o padrão aberto para **traces**, **métricas** e **logs**.

No lab: agentes/SDK nos serviços enviam traces OTLP para o **OTel Collector**, que encaminha ao **Jaeger**. Prometheus e Grafana cobrem métricas e visualização.

- **Trace:** caminho de uma requisição entre serviços.
- **Span:** unidade de trabalho dentro do trace.
- **OTLP:** protocolo de exportação (aqui HTTP/protobuf na porta 4318).
- **Collector:** intermediário que recebe, processa e exporta telemetria.

## Outros termos úteis

| Termo | Significado |
|-------|-------------|
| **Saga** | Coordenação de transação distribuída via eventos (compensações em falha). |
| **ClusterIP** | Service K8s acessível só dentro do cluster. |
| **NodePort** | Expõe Service em porta alta do nó (ex.: web `30080`). |
| **Actuator** | Endpoints Spring Boot de health/métricas (`/actuator/health`). |
| **Bruno** | Cliente HTTP para coleções de API (alternativa ao Postman). |
| **kind / minikube** | Kubernetes local para estudo. |
