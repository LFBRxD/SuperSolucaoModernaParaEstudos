# Diagrama 5.1 — Tópico, partição, offset

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 05**. Foco: anatomia.


## Figura

```mermaid
flowchart TB
  Topic[orders.events]
  Topic --> P0[particao 0]
  Topic --> P1[particao 1]
  Topic --> P2[particao 2]
  P0 --> O0["offset 0 OrderCreated"]
  P0 --> O1["offset 1 OrderConfirmed"]
```

A ordem é garantida dentro da partição, não entre partições.

## O que observar

Compare os nomes desta figura com os nomes reais do código e do Compose (`api-gateway`, `orders.events`, portas 11000+). Se um nome divergir, anote: ou o diagrama está velho, ou você está olhando outro ambiente.

## Exercício

Redesenhe esta figura sem olhar, em papel ou Mermaid. Depois abra de novo e marque o que esqueceu.

## Próximo arquivo

[diagrama-02-groups.md](diagrama-02-groups.md)
