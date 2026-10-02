# Certificados do lab (mTLS gRPC)

Gerados por `scripts/gen-certs.sh` ou `scripts/gen-certs.ps1`.

Arquivos:

- `ca.crt` / `ca.key` — CA do lab
- `gateway.crt` / `gateway.key` — cliente gRPC (api-gateway)
- `orders.crt` / `orders.key` — servidor gRPC orders
- `inventory.crt` / `inventory.key` — servidor gRPC inventory

Chaves são **apenas para estudo**. Não use em produção.
