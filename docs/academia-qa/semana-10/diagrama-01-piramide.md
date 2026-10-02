# Diagrama 10.1 — Pirâmide neste repositório

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 10**. Foco: ferramentas.


## Figura

```mermaid
flowchart TB
  E2E[Playwright poucos fluxos]
  API[Bruno e smoke]
  Int[JUnit com Spring no espelho]
  Unit[regras puras]
  E2E --> API --> Int --> Unit
```

Quanto mais embaixo, mais vezes você roda.

## O que observar

Compare os nomes desta figura com os nomes reais do código e do Compose (`api-gateway`, `orders.events`, portas 11000+). Se um nome divergir, anote: ou o diagrama está velho, ou você está olhando outro ambiente.

## Exercício

Redesenhe esta figura sem olhar, em papel ou Mermaid. Depois abra de novo e marque o que esqueceu.

## Próximo arquivo

[diagrama-02-espera.md](diagrama-02-espera.md)
