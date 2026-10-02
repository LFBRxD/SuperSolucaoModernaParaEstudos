# Diagrama 1.2 — Health agregado

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 01**. Foco: quem o gateway consulta.


## Figura

```mermaid
sequenceDiagram
  participant Q as QA
  participant G as api-gateway
  participant O as orders
  participant I as inventory
  participant P as payments
  participant N as notifications
  Q->>G: GET /api/health
  G->>O: actuator/health
  G->>I: actuator/health e gRPC health
  G->>P: actuator/health
  G->>N: actuator/health
  G-->>Q: overall UP ou não
```

Uma seta falha e o overall deixa de ser UP. Anote qual seta quebrou quando isso acontecer.

## O que observar

Compare os nomes desta figura com os nomes reais do código e do Compose (`api-gateway`, `orders.events`, portas 11000+). Se um nome divergir, anote: ou o diagrama está velho, ou você está olhando outro ambiente.

## Exercício

Redesenhe esta figura sem olhar, em papel ou Mermaid. Depois abra de novo e marque o que esqueceu.

## Próximo arquivo

Semana 2.
