# Meta 12.4 — Prova dos nove

Tempo previsto: **70 min**. Semana 12. Pré-requisito: checkpoints do espelho.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 12**. Foco: comparar sem copiar.


## O que é

A prova é: o espelho sobe do zero, passa nos validadores dos checkpoints que você implementou, e você explica uma diferença consciente em relação ao oráculo (nome de campo, compensação de estoque, DLQ, job). Igualdade byte a byte não é o objetivo.

## Por que existe neste sistema

O oráculo continua sendo a referência de comportamento público: login, catálogo, pedido que termina, 401/403.

## O que você faz com a mão

1. Liste os checkpoints em `docs/academia-qa/checkpoints`.
2. Marque feito, parcial ou não feito.
3. Para cada parcial, uma frase do que falta.

## O que você deve ver

Lista honesta.

## O que pode dar errado

Copiar o repositório inteiro para a pasta espelho e dizer que reconstruiu.

## Onde ler a fonte oficial

docs/academia-qa/checkpoints/README.md

## Como saber que terminou

Você apresenta a lista sem esconder o que faltou.

## Perguntas para responder sozinho

- Qual diferença do espelho é melhoria e qual é dívida?

## Próximo arquivo

[lab-03-apresentar.md](lab-03-apresentar.md)
