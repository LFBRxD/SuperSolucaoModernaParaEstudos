# Leitura 6 — Saga em linguagem de teste

Tempo de leitura: **40 min**. Não substitua o lab. Leia, feche, e só então faça o lab.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 06**. Foco: semana 6.


## Por que esta leitura agora

Nomear o que você já executou.

### Saga

Sequência de passos locais em serviços diferentes, ligada por eventos, com caminho de desfazer ou de desistir.

### Por que não é uma transação só

Mongo de orders e Mongo de inventory não compartilham uma transação. Ou cada um grava o seu, ou ninguém grava. O meio do caminho existe.

### Compensação

Desfazer a reserva se o pagamento falha. O oráculo não faz. O espelho deve fazer na semana 7.

## Fontes

- docs/status-pedido.md
- docs/arquitetura.md

## Perguntas de revisão

- Qual estado é final?
- O que o teste faz se ficar em AWAITING_PAYMENT até o timeout?

## Próximo arquivo

Semana 7.
