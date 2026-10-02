# Bruno — StudyShop

Coleção da API do oráculo (porta 11001, JWT local).

## Ordem

1. `auth 401 products` — sem token, espera 401. Pode rodar sozinho.
2. `login` — grava `accessToken`.
3. `list products`
4. `create order` — grava `orderId`.
5. `poll order` — repete até `CONFIRMED` ou `CANCELLED`, no máximo ~30 segundos.
6. `get order`
7. `notifications by order`
8. `login admin` antes de `update stock`.
9. `create order payment fail` e `create order stock fail` — o estado final ainda é assíncrono; use o smoke para o assert do status final ou rode `poll order` trocando o id.

Ambiente: `environments/local.bru`.

## CLI

Na raiz do repositório, com a stack no ar e a CLI do Bruno instalada:

```bash
bru run bruno/study-shop --env local
```

O smoke em `scripts/smoke.ps1` / `scripts/smoke.sh` é a suíte que espera o estado final sem depender da CLI.

Modo OIDC: `POST /api/auth/login` não existe. Pegue o token no Keycloak e coloque em `accessToken`. Ver `docs/tutoriais/02-oidc-keycloak.md`.
