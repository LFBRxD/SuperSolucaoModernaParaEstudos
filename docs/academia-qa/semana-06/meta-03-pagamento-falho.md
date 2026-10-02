# Meta 6.3 — Cancelar por pagamento

Tempo previsto: **60 min**. Semana 6. Pré-requisito: meta 6.2.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 06**. Foco: caminho negativo injetável.


## O que é

O lab deixa você forçar falha de pagamento com `forcePaymentFailure: true` ou o header `X-Force-Payment-Failure: true`. O estado final é `CANCELLED`. O estoque, nesta versão, permanece decrementado. Isso está escrito de propósito. Não 'corrija' o oráculo achando que é distração.

## Por que existe neste sistema

Você precisa reconhecer limitação de produto versus bug acidental. Aqui a limitação é didática e vira requisito do espelho na semana 7 (compensar).

## O que você faz com a mão

1. Crie um pedido com a flag.
2. Espere `CANCELLED`.
3. Olhe a quantidade do produto antes e depois.

## O que você deve ver

Status CANCELLED e estoque que não voltou, anotado.

## O que pode dar errado

Reportar bug sem ler o cenário 4 de `docs/cenarios-qa.md`.

## Onde ler a fonte oficial

docs/cenarios-qa.md cenário 4

## Como saber que terminou

Você descreve o comportamento sem chamar de surpresa.

## Perguntas para responder sozinho

- No seu espelho, você vai compensar. O que precisa acontecer com o estoque?

## Próximo arquivo

[lab-02-falhas.md](lab-02-falhas.md)
