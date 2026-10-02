# Diagrama 7.2 — Job, Trigger, JobStore

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 07**. Foco: peças do Quartz.


## Figura

```mermaid
flowchart LR
  Trigger[Trigger cron ou intervalo] --> Job[Job expirar pedido]
  Job --> Store[JobStore]
  Job --> Pedido[(pedido)]
  Job --> Log[log jobName fireTime orderId]
```

Você inspeciona o log e o status do pedido. Se usar JDBC, as tabelas QRTZ_ também contam.

## O que observar

Compare os nomes desta figura com os nomes reais do código e do Compose (`api-gateway`, `orders.events`, portas 11000+). Se um nome divergir, anote: ou o diagrama está velho, ou você está olhando outro ambiente.

## Exercício

Redesenhe esta figura sem olhar, em papel ou Mermaid. Depois abra de novo e marque o que esqueceu.

## Próximo arquivo

Semana 8.
