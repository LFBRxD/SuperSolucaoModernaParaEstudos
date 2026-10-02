# Meta 11.1 — Latência e percentil

Tempo previsto: **55 min**. Semana 11. Pré-requisito: semana 9 SLI.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 11**. Foco: não usar só a média.


## O que é

A média esconde a cauda. p95 é o tempo abaixo do qual 95% das chamadas ficaram. Se o p95 do POST de pedido passa do orçamento, o usuário lento sofre mesmo com média bonita.

## Por que existe neste sistema

k6 mede isso. O script do repo está em `tests/k6`. O orçamento do lab é largo porque a máquina é um notebook com Docker.

## O que você faz com a mão

1. Leia o script `tests/k6/pedido-baseline.js` e ache o threshold.
2. Não rode carga contra ambiente que não é seu.
3. Anote a diferença entre baseline (pouca carga) e pico.

## O que você deve ver

Você define p95 com suas palavras e aponta o threshold do script.

## O que pode dar errado

Comemorar média de 100 ms com p95 de 10 s.

## Onde ler a fonte oficial

https://grafana.com/docs/k6/latest/using-k6/thresholds/

## Como saber que terminou

Uma frase: o que acontece se o threshold falha (o processo do k6 sai com erro).

## Perguntas para responder sozinho

- Health check entra na meta de latência do pedido?

## Próximo arquivo

[lab-01-k6.md](lab-01-k6.md)
