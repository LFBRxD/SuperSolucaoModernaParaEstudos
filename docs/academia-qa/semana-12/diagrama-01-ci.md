# Diagrama 12.1 — Pipeline

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 12**. Foco: sempre derruba.


## Figura

```mermaid
flowchart TB
  Build[build] --> Up[compose up]
  Up --> Wait[espera health]
  Wait --> Smoke[smoke]
  Smoke --> E2E[playwright]
  E2E --> Down[down]
  Smoke -.-> Logs[logs se falhar]
  E2E -.-> Logs
```

A seta pontilhada acontece na falha. O down acontece sempre.

## O que observar

Compare os nomes desta figura com os nomes reais do código e do Compose (`api-gateway`, `orders.events`, portas 11000+). Se um nome divergir, anote: ou o diagrama está velho, ou você está olhando outro ambiente.

## Exercício

Redesenhe esta figura sem olhar, em papel ou Mermaid. Depois abra de novo e marque o que esqueceu.

## Próximo arquivo

[diagrama-02-cronjob.md](diagrama-02-cronjob.md)
