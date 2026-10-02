# Meta 5.3 — Consumer group e lag

Tempo previsto: **70 min**. Semana 5. Pré-requisito: meta 5.2.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 05**. Foco: quem já leu a mensagem.


## O que é

Consumer group é o nome do grupo de leitores que dividem as partições. Cada grupo tem o próprio offset. `inventory-service` e `notifications-service` leem o mesmo tópico `orders.events` em grupos diferentes. Os dois recebem as mensagens. Lag é quantas mensagens o grupo ainda não processou.

## Por que existe neste sistema

Lag alto significa que o consumidor está atrasado. O HTTP do pedido pode já ter respondido `CREATED` enquanto o estoque ainda não correu.

## O que você faz com a mão

1. Na UI, abra Consumer Groups.
2. Ache `inventory-service`, `orders-service`, `payments-service`, `notifications-service`.
3. Anote o lag de um grupo depois de um pedido parado no meio, se conseguir.

## O que você deve ver

Pelo menos dois groups no tópico `orders.events`.

## O que pode dar errado

Um único group para dois serviços: um 'rouba' a mensagem do outro e a saga perde um passo.

## Onde ler a fonte oficial

https://kafka.apache.org/documentation/#intro_consumers

## Como saber que terminou

Você explica por que notifications e inventory podem ler o mesmo evento.

## Perguntas para responder sozinho

- Lag zero prova que a regra de negócio passou? Não. Por quê?

## Próximo arquivo

[lab-02-console-consumer.md](lab-02-console-consumer.md)
