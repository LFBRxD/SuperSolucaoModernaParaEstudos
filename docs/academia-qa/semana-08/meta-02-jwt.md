# Meta 8.2 — JWT local

Tempo previsto: **70 min**. Semana 8. Pré-requisito: meta 8.1.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 08**. Foco: o token do momento 1.


## O que é

JWT é um token assinado em três partes. No momento 1 o gateway assina com segredo compartilhado (HS256). O payload traz `sub`, `roles`, `iss`, `exp`. Quem tem o segredo forja token. Por isso o segredo do lab não serve em produção.

## Por que existe neste sistema

Você precisa ler o payload para ver se a role que a UI mostra é a role que a API acredita.

## O que você faz com a mão

1. Siga `docs/tutoriais/01-jwt-local.md`.
2. Cole o token no jwt.io só na sua máquina, em rede fechada. Não use token real de empresa.
3. Anote `iss` e `roles`.

## O que você deve ver

Payload lido e uma frase sobre expiração.

## O que pode dar errado

Achar que o token está criptografado. Ele está assinado. Dá para ler. Não dá para alterar sem invalidar a assinatura.

## Onde ler a fonte oficial

https://jwt.io/introduction

## Como saber que terminou

Você aponta a claim de role.

## Perguntas para responder sozinho

- O que muda quando o exp passa?

## Próximo arquivo

[meta-03-oidc.md](meta-03-oidc.md)
