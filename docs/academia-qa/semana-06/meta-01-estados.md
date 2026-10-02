# Meta 6.1 — Máquina de estados do pedido

Tempo previsto: **70 min**. Semana 6. Pré-requisito: semana 5.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 06**. Foco: status que você asserta.


## O que é

O pedido não pula direto para confirmado. Ele passa por estados. O documento `docs/status-pedido.md` lista a cadeia. Estados intermediários podem durar milissegundos. Seu teste não pode exigir um único GET no meio do caminho.

## Por que existe neste sistema

Flaky test nasce aqui: você lê `AWAITING_STOCK` e falha porque 'não está CONFIRMED', sem esperar.

## O que você faz com a mão

1. Leia `docs/status-pedido.md` e desenhe os estados no papel.
2. Marque os estados finais: `CONFIRMED` e `CANCELLED`.
3. Marque os intermediários.

## O que você deve ver

Desenho com pelo menos os estados do arquivo.

## O que pode dar errado

Tratar `AWAITING_PAYMENT` como erro. Ele é passagem.

## Onde ler a fonte oficial

docs/status-pedido.md

## Como saber que terminou

Você lista dois finais e dois intermediários de memória.

## Perguntas para responder sozinho

- Por que um único GET logo após o POST é fraco?

## Próximo arquivo

[meta-02-eventual.md](meta-02-eventual.md)
