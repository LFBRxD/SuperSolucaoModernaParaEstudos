# Meta 12.1 — O que o CI faz

Tempo previsto: **60 min**. Semana 12. Pré-requisito: semana 10.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 12**. Foco: o mesmo comando fora da sua máquina.


## O que é

CI roda o que você já roda: build, smoke, testes. A diferença é que roda limpo e guarda log quando falha. O arquivo é `.github/workflows/qa-lab.yml`.

## Por que existe neste sistema

Sem CI, só o seu notebook sabe que passou. O workflow é a definição repetível.

## O que você faz com a mão

1. Abra o YAML e liste os jobs.
2. Ache o passo que sobe o Compose e o passo que sempre derruba (if: always).
3. Não desabilite o teardown.

## O que você deve ver

Lista de jobs em cinco linhas suas.

## O que pode dar errado

Workflow que nunca faz down e deixa runner sujo. O deste repo usa always.

## Onde ler a fonte oficial

https://docs.github.com/en/actions/get-started/understand-github-actions

## Como saber que terminou

Você aponta o passo do smoke e o passo do Playwright.

## Perguntas para responder sozinho

- Por que o log é coletado mesmo quando falha?

## Próximo arquivo

[lab-01-ler-pipeline.md](lab-01-ler-pipeline.md)
