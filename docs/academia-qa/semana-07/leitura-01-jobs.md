# Leitura 7 — @Scheduled, Quartz e CronJob

Tempo de leitura: **40 min**. Não substitua o lab. Leia, feche, e só então faça o lab.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 07**. Foco: semana 7.


## Por que esta leitura agora

Comparar as três ferramentas depois de ter um job rodando.

### @Scheduled

Dentro da JVM, simples, sem memória de cluster.

### Quartz

Job, Trigger, JobStore, misfire, cluster se o store for compartilhado.

### CronJob do Kubernetes

A plataforma dispara um processo e mata. Você não segura thread. Entra na semana 12. Não substitui um trigger de segundos dentro da saga sem cuidado com sobreposição.

## Fontes

- https://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/tutorial-lesson-01.html
- https://docs.spring.io/spring-framework/reference/integration/scheduling.html

## Perguntas de revisão

- Onde o misfire fica registrado no seu lab?
- Por que o oráculo precisa de um job que ele ainda não tem?

## Próximo arquivo

Semana 8.
