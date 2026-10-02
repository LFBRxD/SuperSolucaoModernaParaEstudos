# Meta 7.3 — @Scheduled

Tempo previsto: **60 min**. Semana 7. Pré-requisito: meta 7.2.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 07**. Foco: o cron mais simples.


## O que é

`@Scheduled` no Spring dispara um método de tempos em tempos dentro do mesmo processo. Serve para um lab de um processo só. Não lembra a última execução se o processo cai no meio, e dois processos disparam duas vezes.

## Por que existe neste sistema

É o primeiro degrau. Você usa para um job óbvio e sente a limitação antes de ir ao Quartz.

## O que você faz com a mão

1. Leia https://docs.spring.io/spring-framework/reference/integration/scheduling.html só a parte de @Scheduled e cron.
2. Escreva um cron de laboratório de 15 segundos (não use isso em produção).
3. Liste dois limites: sem cluster e difícil de inspecionar.

## O que você deve ver

Um cron escrito e dois limites no papel.

## O que pode dar errado

Colocar regra de pedido dentro de `Thread.sleep` no request HTTP. Isso segura o usuário e não é agendamento.

## Onde ler a fonte oficial

https://docs.spring.io/spring-framework/reference/integration/scheduling.html

## Como saber que terminou

Você recusa sleep no request com uma frase.

## Perguntas para responder sozinho

- Dois processos com o mesmo @Scheduled fazem o quê?

## Próximo arquivo

[meta-04-quartz.md](meta-04-quartz.md)
