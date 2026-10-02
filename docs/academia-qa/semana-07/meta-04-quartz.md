# Meta 7.4 — Quartz: Job, Trigger, JobStore

Tempo previsto: **80 min**. Semana 7. Pré-requisito: meta 7.3.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 07**. Foco: agendamento que dá para inspecionar.


## O que é

Job é o trabalho. Trigger é quando dispara (cron ou daqui a N segundos). JobStore é onde isso fica gravado. RAM some no restart. JDBC (ou o equivalente que você documentar) sobrevive. Misfire é 'deveria ter rodado e não rodou'. Cluster com JobStore compartilhado evita duas instâncias rodarem o mesmo disparo.

## Por que existe neste sistema

Pedido preso em `AWAITING_PAYMENT` não se resolve com Kafka se o evento de pagamento nunca veio. Alguém precisa acordar e cancelar. Esse alguém é um job.

## O que você faz com a mão

1. Leia o tutorial oficial do Quartz, seções de Job e Trigger: https://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/
2. Desenhe Job `ExpireOrders` e Trigger de 20 segundos no lab.
3. Decida o que fica inspecionável: log com jobName e orderId, ou um GET interno de jobs.

## O que você deve ver

Desenho Job + Trigger + onde você vai olhar.

## O que pode dar errado

Cron de produção de madrugada no lab e você esperar horas. Use intervalo curto e documente que em produção o número muda.

## Onde ler a fonte oficial

https://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/tutorial-lesson-01.html

## Como saber que terminou

Você diferencia Job de Trigger sem olhar a página.

## Perguntas para responder sozinho

- O que é misfire, com exemplo de notebook em sleep?

## Próximo arquivo

[lab-02-job-timeout.md](lab-02-job-timeout.md)
