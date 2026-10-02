# Diagrama 9.2 — Retry, DLQ, replay

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 09**. Foco: fim do loop.


## Figura

```mermaid
flowchart LR
  A[tentativa 1] --> B[tentativa 2]
  B --> C[tentativa 3]
  C --> D[DLQ]
  D --> E[replay manual]
  E --> F[efeito idempotente]
```

A seta de replay não volta para o retry automático.

## O que observar

Compare os nomes desta figura com os nomes reais do código e do Compose (`api-gateway`, `orders.events`, portas 11000+). Se um nome divergir, anote: ou o diagrama está velho, ou você está olhando outro ambiente.

## Exercício

Redesenhe esta figura sem olhar, em papel ou Mermaid. Depois abra de novo e marque o que esqueceu.

## Próximo arquivo

Semana 10.
