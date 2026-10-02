# Meta 10.2 — Bruno como suíte

Tempo previsto: **55 min**. Semana 10. Pré-requisito: meta 10.1.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 10**. Foco: a coleção que roda sozinha.


## O que é

Bruno guarda requests em arquivo. A CLI roda a pasta e falha se o assert falhar. Variável `accessToken` passa do login para o próximo request. Sem ordem e sem assert, a coleção é só favorito.

## Por que existe neste sistema

A pasta `bruno/study-shop` é a suíte de API do oráculo. Você completa o que faltava: 401, falha de pagamento, estoque, polling, notificação.

## O que você faz com a mão

1. Abra a coleção no Bruno ou leia os `.bru`.
2. Veja `environments/local.bru`.
3. Leia o README da pasta.

## O que você deve ver

Você sabe qual request grava o token.

## O que pode dar errado

Rodar create-order sem ter rodado login e culpar a API.

## Onde ler a fonte oficial

https://docs.usebruno.com/bru-cli/overview

## Como saber que terminou

Um comando de CLI está copiado no seu caderno.

## Perguntas para responder sozinho

- O que o assert de status 200 não prova sobre a saga?

## Próximo arquivo

[lab-02-playwright-login.md](lab-02-playwright-login.md)
