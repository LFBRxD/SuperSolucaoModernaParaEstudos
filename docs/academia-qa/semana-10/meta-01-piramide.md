# Meta 10.1 — Pirâmide de testes

Tempo previsto: **55 min**. Semana 10. Pré-requisito: semanas 2 a 9.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 10**. Foco: o que cada teste aguenta.


## O que é

Teste de unidade é rápido e estreito. Teste de API olha HTTP. Teste de UI olha o browser e é o mais lento e frágil. A pirâmide pede muitos testes baratos e poucos de ponta. Subir Docker para testar uma soma é desperdício. Não ter nenhum teste de ponta deixa a saga sem rede.

## Por que existe neste sistema

Você já tem JUnit do espelho, smoke do oráculo, Bruno e, nesta semana, Playwright.

## O que você faz com a mão

1. Desenhe a pirâmide e coloque um teste seu em cada faixa.
2. Marque qual faixa falta.
3. Não mova tudo para Playwright.

## O que você deve ver

Desenho com três faixas e um exemplo em cada.

## O que pode dar errado

Só E2E, porque 'é o que o usuário vê', e a suíte leva 40 minutos e falha por animação.

## Onde ler a fonte oficial

https://martinfowler.com/articles/practical-test-pyramid.html

## Como saber que terminou

Você justifica um teste que NÃO é de UI.

## Perguntas para responder sozinho

- O polling da saga fica em qual faixa?

## Próximo arquivo

[lab-01-smoke-full.md](lab-01-smoke-full.md)
