# Leitura 9 — Onde olhar primeiro

Tempo de leitura: **35 min**. Não substitua o lab. Leia, feche, e só então faça o lab.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 09**. Foco: semana 9.


## Por que esta leitura agora

Ordem de investigação para não abrir dez ferramentas sem pergunta.

### Ordem

1) status HTTP e corpo. 2) orderId no log. 3) mensagem no tópico. 4) trace no horário. 5) lag e métrica `up`.

### DLQ

Sem rastro, o retry vira achismo.

### Idempotência

Replay só é seguro com chave de efeito.

## Fontes

- https://opentelemetry.io/docs/what-is-opentelemetry/
- docs/observabilidade.md

## Perguntas de revisão

- O que o Prometheus não guarda neste lab?
- Qual o N de tentativas que você escolheu?

## Próximo arquivo

Semana 10.
