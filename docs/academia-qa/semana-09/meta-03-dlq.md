# Meta 9.3 — DLQ e replay

Tempo previsto: **70 min**. Semana 9. Pré-requisito: semana 5 e 7.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 09**. Foco: mensagem que não deve girar para sempre.


## O que é

DLQ (dead letter) é o lugar da mensagem que falhou demais. Sem ela, ou você perde o evento, ou você reprocessa infinito e repete o estrago. Replay é pegar essa mensagem e mandar de novo, de propósito, depois de corrigir a causa.

## Por que existe neste sistema

O oráculo só dá log.error e segue. Não há DLQ. Você constrói no espelho: tópico `lab.dlq` ou coleção.

## O que você faz com a mão

1. Leia `docs/academia-qa/desafios/dlq.md`.
2. Desenhe: consumer falha → tenta N vezes → publica na DLQ com o erro e o orderId.
3. Replay é um comando seu, não automático no primeiro dia.

## O que você deve ver

Desenho com N tentativas e um lugar inspectável.

## O que pode dar errado

Engolir a exceção e commitar o offset. A mensagem some e o pedido fica preso sem rastro.

## Onde ler a fonte oficial

https://kafka.apache.org/documentation/#design_consumerposition

## Como saber que terminou

Você explica por que retry infinito é pior do que DLQ.

## Perguntas para responder sozinho

- O que você guarda junto: payload original ou só o erro?

## Próximo arquivo

[lab-02-dlq.md](lab-02-dlq.md)
