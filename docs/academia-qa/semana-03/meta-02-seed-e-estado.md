# Meta 3.2 — Seed e estado do lab

Tempo previsto: **60 min**. Semana 3. Pré-requisito: meta 3.1.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 03**. Foco: dados iniciais conhecidos.


## O que é

Seed é a carga inicial. O inventory cria cinco produtos na primeira subida, entre eles `prod-mouse` e `prod-raro` (estoque baixo). Sem seed, o catálogo abre vazio e os cenários de QA não têm massa.

## Por que existe neste sistema

Teste que depende de 'o que estava ontem' falha no dia seguinte. Você precisa saber resetar.

## O que você faz com a mão

1. Leia `docs/cenarios-qa.md` cenário 2 e liste os cinco ids.
2. Veja no Mongo se `prod-raro` tem quantidade 1.
3. Leia o que `scripts/down.ps1 -Volumes` faz: apaga o volume e o seed roda de novo na próxima subida.

## O que você deve ver

Os cinco ids no banco ou na API autenticada.

## O que pode dar errado

Resetar volume no meio de um teste e achar que o estoque 'voltou sozinho' por bug.

## Onde ler a fonte oficial

Código `SeedConfig` do inventory no oráculo.

## Como saber que terminou

Você explica como voltar ao estoque inicial de propósito.

## Perguntas para responder sozinho

- Quando você NÃO deve apagar o volume?

## Próximo arquivo

[meta-03-equivalencia.md](meta-03-equivalencia.md)
