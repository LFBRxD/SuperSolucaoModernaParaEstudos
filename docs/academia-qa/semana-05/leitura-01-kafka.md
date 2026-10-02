# Leitura 5 — Kafka para QA

Tempo de leitura: **45 min**. Não substitua o lab. Leia, feche, e só então faça o lab.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 05**. Foco: semana 5.


## Por que esta leitura agora

Fixar o vocabulário que a UI mostrou.

### Tópico

Nome lógico. No lab: `orders.events`, `inventory.events`, `payments.events`.

### Group

Quem acompanha o próprio progresso. Dois groups leem tudo. Dois membros do mesmo group dividem partições.

### Lag

Atraso. Útil, mas não substitui olhar o status do pedido.

## Fontes

- https://kafka.apache.org/documentation/#gettingStarted

## Perguntas de revisão

- Qual group lê `OrderCreated` para baixar estoque?
- O que você não deve passar em `--group` num consumer de estudo?

## Próximo arquivo

Semana 6.
