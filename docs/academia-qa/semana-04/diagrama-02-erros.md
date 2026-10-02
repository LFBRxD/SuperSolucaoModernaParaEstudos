# Diagrama 4.2 — Onde o erro nasce

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 04**. Foco: mapa de falhas da chamada síncrona.


## Figura

```mermaid
flowchart TB
  A[sem token] --> H401[HTTP 401]
  B[produto ausente] --> H404[HTTP 404]
  C[inventory parado] --> H502[HTTP 502]
  D[deadline estourou] --> H504[HTTP 504]
```

Cada caixa da esquerda é uma causa diferente. Não as trate como 'deu erro'.

## O que observar

Compare os nomes desta figura com os nomes reais do código e do Compose (`api-gateway`, `orders.events`, portas 11000+). Se um nome divergir, anote: ou o diagrama está velho, ou você está olhando outro ambiente.

## Exercício

Redesenhe esta figura sem olhar, em papel ou Mermaid. Depois abra de novo e marque o que esqueceu.

## Próximo arquivo

Semana 5.
