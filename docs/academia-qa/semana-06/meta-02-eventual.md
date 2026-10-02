# Meta 6.2 — Consistência eventual

Tempo previsto: **60 min**. Semana 6. Pré-requisito: meta 6.1.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 06**. Foco: agora não é o estado final.


## O que é

Consistência eventual significa: se nada der errado, em algum momento o estado esperado aparece. Não é instantâneo. O QA espera com timeout (por exemplo 60 segundos) e intervalo (por exemplo 1 segundo).

## Por que existe neste sistema

A web faz polling de 2 segundos na tela de detalhe. A API não empurra websocket. Você repete o GET.

## O que você faz com a mão

1. Abra um pedido e atualize até o status parar de mudar.
2. Anote quantos segundos levou.
3. Escreva o timeout que você usaria num script.

## O que você deve ver

Um pedido que chegou em estado final e o tempo anotado.

## O que pode dar errado

Timeout de 1 segundo em máquina lenta e concluir que a saga está quebrada.

## Onde ler a fonte oficial

https://martinfowler.com/articles/patterns-of-distributed-systems/ (visão geral; não leia o livro inteiro)

## Como saber que terminou

Você tem um número de timeout justificado pelo que viu.

## Perguntas para responder sozinho

- O que o teste deve dizer se o timeout estourar?

## Próximo arquivo

[lab-01-feliz.md](lab-01-feliz.md)
