# Diagrama 1.1 — Stack e portas

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 01**. Foco: portas do host.


## Figura

```mermaid
flowchart TB
  subgraph host [Seu computador]
    Web["web :11000"]
    Gw["api-gateway :11001"]
    Ord["orders :11002 HTTP :11003 gRPC"]
    Inv["inventory :11004 HTTP :11005 gRPC"]
    Pay["payments :11006"]
    Noti["notifications :11007"]
    Mongo["mongodb :11008"]
    Kafka["kafka :11009"]
    Graf["grafana :11010"]
    Jaeger["jaeger :11011"]
    Prom["prometheus :11012"]
    Kui["kafka-ui :11016"]
  end
  Web --> Gw
  Gw --> Ord
  Gw --> Inv
  Gw --> Noti
```

A porta da esquerda na publicação Docker é a que você digita no browser. Kafka UI entra na semana 5; a porta 11016 já fica reservada.

## O que observar

Compare os nomes desta figura com os nomes reais do código e do Compose (`api-gateway`, `orders.events`, portas 11000+). Se um nome divergir, anote: ou o diagrama está velho, ou você está olhando outro ambiente.

## Exercício

Redesenhe esta figura sem olhar, em papel ou Mermaid. Depois abra de novo e marque o que esqueceu.

## Próximo arquivo

[diagrama-02-health.md](diagrama-02-health.md)
