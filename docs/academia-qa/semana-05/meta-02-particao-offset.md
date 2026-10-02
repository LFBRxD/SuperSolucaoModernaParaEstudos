# Meta 5.2 — Partição, offset e chave

Tempo previsto: **70 min**. Semana 5. Pré-requisito: meta 5.1.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 05**. Foco: ordem e posição da mensagem.


## O que é

Um tópico é dividido em partições. Cada mensagem numa partição tem um offset (um número crescente). A chave (no lab, em geral `orderId`) escolhe a partição. Mensagens da mesma chave tendem a ficar na mesma partição e, portanto, em ordem.

## Por que existe neste sistema

Se dois eventos do mesmo pedido trocarem de ordem entre partições diferentes, a saga pode confirmar antes de reservar. A chave existe para reduzir essa chance.

## O que você faz com a mão

1. Na Kafka UI, abra `orders.events` e veja o número de partições (o serviço declara 3).
2. Depois de um pedido, abra uma mensagem e ache `eventType` e a chave.
3. Anote o offset.

## O que você deve ver

Uma mensagem com `eventType` igual a `OrderCreated` e chave igual ao `orderId` da API.

## O que pode dar errado

Achar que offset é o id do pedido. Offset é a posição na partição.

## Onde ler a fonte oficial

https://kafka.apache.org/documentation/#intro_topics

## Como saber que terminou

Você desenha tópico → partição → offset com um exemplo real.

## Perguntas para responder sozinho

- Por que a chave é o orderId e não o e-mail?

## Próximo arquivo

[meta-03-consumer-group.md](meta-03-consumer-group.md)
