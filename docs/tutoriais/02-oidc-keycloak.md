# Tutorial 02 — OIDC / Keycloak

Hands-on do **Momento 2**: mesma matriz de roles, tokens emitidos pelo IdP.

## O que muda vs Momento 1

| | Momento 1 | Momento 2 |
|---|-----------|-----------|
| Quem emite o JWT | api-gateway | Keycloak |
| Algoritmo típico | HS256 (secret compartilhado) | RS256 (JWKS) |
| Login | `POST /api/auth/login` | Redirect OIDC + PKCE na web |
| Gateway | `JwtService` local | `oauth2ResourceServer` + `issuer-uri` |

## Subir o overlay

Na pasta `infra/`:

```bash
docker compose -f docker-compose.yml -f docker-compose.oidc.yml up -d --build
```

Aguarde Keycloak em `http://localhost:11015` (admin console: `admin` / `admin`).

Realm importado: `study-shop`.

## Issuer vs JWKS (ponto de aprendizado)

- Tokens trazem `iss=http://localhost:11015/realms/study-shop` (hostname do browser).
- O gateway no Docker busca chaves em `OIDC_JWK_SET_URI=http://keycloak:8080/.../certs`.

Sem esse split, o container tentaria JWKS em `localhost` e falharia.

## Obter token (Resource Owner / Direct Access — lab)

Client público `study-shop-web` tem Direct Access Grants ligado para estudo via curl:

```bash
TOKEN=$(curl -sf -X POST 'http://localhost:11015/realms/study-shop/protocol/openid-connect/token' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'grant_type=password' \
  -d 'client_id=study-shop-web' \
  -d 'username=qa' \
  -d 'password=qa123' | jq -r .access_token)

echo "$TOKEN" | cut -d. -f2 | tr '_-' '/+' | base64 -d 2>/dev/null | jq .
```

Compare o payload com o JWT local (tutorial 01): agora há `realm_access.roles`, `azp`, `iss` do Keycloak.

## Chamada à API

```bash
curl -sf http://localhost:11001/api/products \
  -H "Authorization: Bearer $TOKEN" | jq 'length'
```

Admin no stock:

```bash
ADMIN=$(curl -sf -X POST 'http://localhost:11015/realms/study-shop/protocol/openid-connect/token' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'grant_type=password' \
  -d 'client_id=study-shop-web' \
  -d 'username=admin' \
  -d 'password=admin123' | jq -r .access_token)

curl -sf -X PUT http://localhost:11001/api/products/prod-mouse/stock \
  -H "Authorization: Bearer $ADMIN" \
  -H 'Content-Type: application/json' \
  -d '{"quantity":50}' | jq '{productId,quantity}'
```

## UI

1. Abra `http://localhost:11000/login`.
2. Clique **Entrar com Keycloak**.
3. Login `qa` / `qa123` no Keycloak.
4. Volta ao StudyShop com sessão Bearer.

## Voltar ao Momento 1

```bash
docker compose -f docker-compose.yml up -d --build
```

(sem o overlay oidc; web rebuilda com `VITE_AUTH_MODE=local`).

## O que você dominou

- Resource Server Spring Boot
- Issuer claim vs JWKS URI
- Roles de realm → `ROLE_USER` / `ROLE_ADMIN`
- Authorization Code + PKCE na SPA (lab)

Próximo: [03-mtls-grpc.md](03-mtls-grpc.md).
