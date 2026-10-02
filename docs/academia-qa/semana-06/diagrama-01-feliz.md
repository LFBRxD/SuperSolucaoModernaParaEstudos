# Diagrama 6.1 — Sequência feliz

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 06**. Foco: eventos em ordem.


## Figura

```mermaid
sequenceDiagram
  participant O as orders
  participant I as inventory
  participant P as payments
  participant N as notifications
  O->>I: OrderCreated
  I->>O: StockReserved
  I->>P: StockReserved
  P->>O: PaymentApproved
  O->>N: OrderConfirmed
```

Notifications não entra no meio. Ela reage ao confirmado ou ao cancelado.

## O que observar

Compare os nomes desta figura com os nomes reais do código e do Compose (`api-gateway`, `orders.events`, portas 11000+). Se um nome divergir, anote: ou o diagrama está velho, ou você está olhando outro ambiente.

## Exercício

Redesenhe esta figura sem olhar, em papel ou Mermaid. Depois abra de novo e marque o que esqueceu.

## Próximo arquivo

[diagrama-02-falhas.md](diagrama-02-falhas.md)
