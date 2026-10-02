# Tutorial 01 — JWT local (HS256)

Hands-on do **Momento 1**: login no api-gateway, Bearer token, roles, 401 e 403.

## Pré-requisito

Stack no ar (`./scripts/up.sh` ou Compose em `infra/`).

## 1. Health continua público

```bash
curl -s http://localhost:11001/api/health | jq .overall
```

Esperado: `UP` (ou `DEGRADED` se algo cair — mas **sem** 401).

## 2. Sem token → 401

```bash
curl -s -o /tmp/out.json -w "%{http_code}" http://localhost:11001/api/products
cat /tmp/out.json
```

Esperado: HTTP `401` e JSON `{"status":401,"error":"Unauthorized"}`.

## 3. Login e inspeção do JWT

```bash
TOKEN=$(curl -sf -X POST http://localhost:11001/api/auth/login \
  -H 'Content-Type: application/json' \
  -d '{"username":"qa","password":"qa123"}' | jq -r .accessToken)
echo "$TOKEN"
```

Cole o token em [jwt.io](https://jwt.io) (só payload — é lab). Observe:

- `iss`: `studyshop-local`
- `sub`: `qa`
- `roles`: `["USER"]`

## 4. Chamada autenticada

```bash
curl -sf http://localhost:11001/api/products \
  -H "Authorization: Bearer $TOKEN" | jq 'length'
```

Esperado: número ≥ 1.

## 5. USER no stock → 403

```bash
curl -s -o /tmp/out.json -w "%{http_code}" -X PUT \
  http://localhost:11001/api/products/prod-mouse/stock \
  -H "Authorization: Bearer $TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"quantity":10}'
echo
cat /tmp/out.json
```

Esperado: `403`.

## 6. ADMIN no stock → 200

```bash
ADMIN=$(curl -sf -X POST http://localhost:11001/api/auth/login \
  -H 'Content-Type: application/json' \
  -d '{"username":"admin","password":"admin123"}' | jq -r .accessToken)

curl -sf -X PUT http://localhost:11001/api/products/prod-mouse/stock \
  -H "Authorization: Bearer $ADMIN" \
  -H 'Content-Type: application/json' \
  -d '{"quantity":50}' | jq '{productId,quantity}'
```

## 7. UI e Bruno

1. Web `http://localhost:11000/login` — entrar como `qa`.
2. Menu **Estoque** não aparece para `qa`; aparece para `admin`.
3. Bruno: rode `login` (ou `login admin`) antes das demais requests (grava `accessToken`).

## 8. Smoke

```bash
./scripts/smoke.sh
# ou
.\scripts\smoke.ps1
```

## O que você dominou

- Bearer JWT na borda HTTP
- Claims `sub` / `roles` / `iss`
- Diferença **401** (não autenticado) vs **403** (autenticado sem permissão)
- Filtro Spring Security + HS256 local (sem IdP)

Próximo: [02-oidc-keycloak.md](02-oidc-keycloak.md).
