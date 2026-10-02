# Meta 8.4 — CORS

Tempo previsto: **50 min**. Semana 8. Pré-requisito: meta 8.1.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 08**. Foco: o browser e outra origem.


## O que é

CORS é uma regra do browser. O browser pergunta com OPTIONS se pode chamar a API de outra origem. `curl` não faz essa pergunta. Por isso a API 'funciona no curl' e falha no browser de outra porta.

## Por que existe neste sistema

O lab libera origem ampla de propósito. É risco, não modelo de produção.

## O que você faz com a mão

1. Leia `CorsConfig` no gateway.
2. No DevTools, ache um OPTIONS se você chamar a API de uma origem diferente. Se a web é same-origin via proxy, pode não haver preflight.
3. Anote: same-origin no lab Docker (a web proxia `/api`).

## O que você deve ver

Uma frase: de onde o browser chama e se houve OPTIONS.

## O que pode dar errado

Concluir que a API está sem CORS porque o curl funcionou.

## Onde ler a fonte oficial

https://developer.mozilla.org/pt-BR/docs/Web/HTTP/CORS

## Como saber que terminou

Você distingue erro de CORS de 401.

## Perguntas para responder sozinho

- Quem bloqueia CORS: o browser ou o curl?

## Próximo arquivo

[meta-05-mtls.md](meta-05-mtls.md)
