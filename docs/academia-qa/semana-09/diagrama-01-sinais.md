# Diagrama 9.1 — A mesma compra em três sinais

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 09**. Foco: correlação.


## Figura

```mermaid
flowchart TB
  Pedido[orderId]
  Pedido --> Log[log do servico]
  Pedido --> Topic[mensagem Kafka]
  Pedido --> Trace[trace no Jaeger por horario]
  Pedido --> Metric[metrica agregada sem o id]
```

Métrica não substitui o id. Ela diz se o problema é só seu ou de todo mundo.

## O que observar

Compare os nomes desta figura com os nomes reais do código e do Compose (`api-gateway`, `orders.events`, portas 11000+). Se um nome divergir, anote: ou o diagrama está velho, ou você está olhando outro ambiente.

## Exercício

Redesenhe esta figura sem olhar, em papel ou Mermaid. Depois abra de novo e marque o que esqueceu.

## Próximo arquivo

[diagrama-02-dlq.md](diagrama-02-dlq.md)
