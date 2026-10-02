# Diagrama 10.2 — Espera do estado final

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 10**. Foco: não assertar o meio.


## Figura

```mermaid
flowchart LR
  Post[POST pedido] --> Loop{status final?}
  Loop -->|nao e ainda tem tempo| Get[GET de novo]
  Get --> Loop
  Loop -->|CONFIRMED ou CANCELLED| Ok[assert do cenario]
  Loop -->|timeout| Falha[mostra ultimo status]
```

O loop tem teto. A falha mostra o último status, não só 'timeout'.

## O que observar

Compare os nomes desta figura com os nomes reais do código e do Compose (`api-gateway`, `orders.events`, portas 11000+). Se um nome divergir, anote: ou o diagrama está velho, ou você está olhando outro ambiente.

## Exercício

Redesenhe esta figura sem olhar, em papel ou Mermaid. Depois abra de novo e marque o que esqueceu.

## Próximo arquivo

Semana 11.
