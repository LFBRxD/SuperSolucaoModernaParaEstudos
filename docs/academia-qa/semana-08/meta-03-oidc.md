# Meta 8.3 — OIDC e PKCE

Tempo previsto: **75 min**. Semana 8. Pré-requisito: meta 8.2.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 08**. Foco: momento 2.


## O que é

OIDC é login delegado. O Keycloak autentica e emite o token. PKCE impede que um código de autorização roubado no caminho seja trocado por token sem o verificador que ficou no browser. A UI redireciona; o gateway passa a validar pela chave pública (JWKS), não pelo segredo HS256.

## Por que existe neste sistema

O mesmo RBAC (USER/ADMIN) continua. Muda quem emite o token.

## O que você faz com a mão

1. Leia `docs/tutoriais/02-oidc-keycloak.md` até a metade.
2. Suba o overlay só quando o lab mandar, para não misturar com o momento 1 no meio de outro teste.
3. Anote a URL 11015.

## O que você deve ver

Você sabe qual porta é o Keycloak e qual claim a UI lê (`realm_access`).

## O que pode dar errado

Deixar o overlay ligado e o Bruno antigo chamar `/api/auth/login`, que não existe no modo OIDC.

## Onde ler a fonte oficial

https://oauth.net/2/pkce/

## Como saber que terminou

Você explica PKCE em uma frase: segredo temporário criado pelo próprio browser.

## Perguntas para responder sozinho

- Logout na UI apaga o token no Keycloak? Não neste lab. O que isso significa?

## Próximo arquivo

[lab-02-keycloak.md](lab-02-keycloak.md)
