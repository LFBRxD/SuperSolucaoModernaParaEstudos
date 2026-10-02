# Diagrama 7.1 — Kafka, webhook e job

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 07**. Foco: qual caminho para qual problema.


## Figura

```mermaid
flowchart TB
  Fato[algo aconteceu]
  Fato --> K[Kafka para servicos internos]
  Fato --> W[Webhook para sistema externo]
  Relogio[tempo passou] --> J[Quartz ou Scheduled]
```

Evento não espera relógio. Relógio não substitui o evento rápido.

## O que observar

Compare os nomes desta figura com os nomes reais do código e do Compose (`api-gateway`, `orders.events`, portas 11000+). Se um nome divergir, anote: ou o diagrama está velho, ou você está olhando outro ambiente.

## Exercício

Redesenhe esta figura sem olhar, em papel ou Mermaid. Depois abra de novo e marque o que esqueceu.

## Próximo arquivo

[diagrama-02-quartz.md](diagrama-02-quartz.md)
