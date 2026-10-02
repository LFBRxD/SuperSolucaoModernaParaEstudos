# Diagrama 5.2 — Dois groups, um tópico

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 05**. Foco: fan-out.


## Figura

```mermaid
flowchart LR
  T[orders.events] --> G1[group inventory-service]
  T --> G2[group notifications-service]
```

Os dois leem. Notifications só age em alguns `eventType`. Inventory só age em `OrderCreated`.

## O que observar

Compare os nomes desta figura com os nomes reais do código e do Compose (`api-gateway`, `orders.events`, portas 11000+). Se um nome divergir, anote: ou o diagrama está velho, ou você está olhando outro ambiente.

## Exercício

Redesenhe esta figura sem olhar, em papel ou Mermaid. Depois abra de novo e marque o que esqueceu.

## Próximo arquivo

Semana 6.
