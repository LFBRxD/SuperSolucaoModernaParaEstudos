# Tutorial 03 — mTLS no gRPC

Hands-on do **Momento 3**: identidade de **serviço** (não substitui JWT de usuário).

## Conceito

| | JWT | mTLS |
|---|-----|------|
| Prova | usuário/cliente HTTP | processo/serviço |
| Onde | browser → gateway | gateway ↔ orders/inventory |
| Material | token Bearer | certificado X.509 + CA |

## Gerar / regenerar certificados

```bash
./scripts/gen-certs.sh
# ou
.\scripts\gen-certs.ps1
```

Saída em `infra/certs/` (já versionada para o lab subir sem regenerar).

## Subir com mTLS

```bash
cd infra
docker compose -f docker-compose.yml -f docker-compose.mtls.yml up -d --build
```

Com OIDC + mTLS:

```bash
GATEWAY_SPRING_PROFILES=oidc,mtls \
  docker compose -f docker-compose.yml -f docker-compose.oidc.yml -f docker-compose.mtls.yml up -d --build
```

No PowerShell:

```powershell
$env:GATEWAY_SPRING_PROFILES = "oidc,mtls"
docker compose -f docker-compose.yml -f docker-compose.oidc.yml -f docker-compose.mtls.yml up -d --build
```

## Validar caminho feliz

1. Login JWT (local ou OIDC) e `GET /api/products` → 200.
2. Health agregado: `inventory-grpc` = UP.

## Quebrar o trust (cenário negativo)

1. Pare o gateway: `docker compose stop api-gateway`
2. Renomeie temporariamente o cert do cliente, ou monte um truststore sem a CA.
3. Mais simples para estudo: edite `docker-compose.mtls.yml` e comente o volume de certs do **gateway** apenas; suba de novo.
4. Health/`GET /api/products` deve falhar no gRPC (502 / inventory-grpc DOWN).

Restaure o volume e `up -d` novamente.

## Inspecionar certificados

```bash
openssl x509 -in infra/certs/orders.crt -noout -subject -ext subjectAltName
openssl verify -CAfile infra/certs/ca.crt infra/certs/gateway.crt
```

## O que você dominou

- CA, cert de servidor e de cliente
- `clientAuth: REQUIRE` no servidor gRPC
- Negociação `TLS` no cliente net.devh
- Separação **authN de usuário** (JWT) vs **authN de serviço** (mTLS)

Voltar à visão geral: [../seguranca.md](../seguranca.md).
