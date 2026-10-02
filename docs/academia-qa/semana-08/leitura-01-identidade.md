# Leitura 8 — Três provas diferentes

Tempo de leitura: **35 min**. Não substitua o lab. Leia, feche, e só então faça o lab.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 08**. Foco: semana 8.


## Por que esta leitura agora

Não misturar usuário, provedor de login e serviço.

### JWT local

O próprio gateway emite e valida com segredo.

### OIDC

O Keycloak emite. O gateway confere a assinatura pela chave pública.

### mTLS

Certificado do processo na chamada gRPC. O usuário nem aparece nesse handshake.

## Fontes

- docs/seguranca.md
- https://oauth.net/2/pkce/

## Perguntas de revisão

- Qual prova o browser apresenta?
- Qual prova o inventory exige no momento 3?

## Próximo arquivo

Semana 9.
