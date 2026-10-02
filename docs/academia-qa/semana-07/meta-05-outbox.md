# Meta 7.5 — Outbox e quando não usar job

Tempo previsto: **60 min**. Semana 7. Pré-requisito: meta 7.4.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 07**. Foco: não substituir Kafka por cron.


## O que é

Outbox é gravar o evento na mesma transação do pedido e um poller publicar no Kafka. Job periódico varre o que ficou preso. Kafka continua sendo o caminho rápido. O job é a rede de segurança e o relógio (expirar, reconciliar, limpar).

## Por que existe neste sistema

Quem troca a saga inteira por um cron de 1 minuto deixa o sistema lento e ainda perde ordem. Você precisa dos dois papéis claros.

## O que você faz com a mão

1. Escreva três linhas: isto é evento, isto é job, isto é os dois.
2. Exemplos do plano: OrderCreated é evento. Expirar pagamento é job. Retry de webhook pode ser job lendo uma tabela de tentativas.
3. Não implemente outbox completo se o tempo estourar; implemente o job de expiração e deixe outbox como nota.

## O que você deve ver

Tabela de três linhas no relatório.

## O que pode dar errado

Publicar no Kafka só de minuto em minuto 'para simplificar' e chamar de tempo real.

## Onde ler a fonte oficial

https://microservices.io/patterns/data/transactional-outbox.html

## Como saber que terminou

A tabela existe e o job de expiração está separado do evento de criação.

## Perguntas para responder sozinho

- Retry de webhook é evento ou job? Defenda em uma frase.

## Próximo arquivo

[lab-03-idempotencia-do-job.md](lab-03-idempotencia-do-job.md)
