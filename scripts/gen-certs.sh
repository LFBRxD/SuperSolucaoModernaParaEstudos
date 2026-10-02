#!/usr/bin/env bash
# Gera CA + certificados PEM (PKCS#8) para mTLS do lab.
# Uso: ./scripts/gen-certs.sh
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CERTS="$ROOT/infra/certs"
mkdir -p "$CERTS"
cd "$CERTS"

if ! command -v openssl >/dev/null 2>&1; then
  echo "openssl é obrigatório"
  exit 1
fi

openssl genrsa -out ca.key 4096
openssl req -x509 -new -nodes -key ca.key -sha256 -days 3650 -out ca.crt -subj "/CN=StudyShop Lab CA"

for name in gateway orders inventory; do
  openssl genrsa -out "${name}.key.tmp" 2048
  openssl req -new -key "${name}.key.tmp" -out "${name}.csr" -subj "/CN=${name}-service"
  cat > "${name}.ext" <<EOF
subjectAltName=DNS:${name}-service,DNS:localhost,IP:127.0.0.1
extendedKeyUsage=serverAuth,clientAuth
EOF
  openssl x509 -req -in "${name}.csr" -CA ca.crt -CAkey ca.key -CAcreateserial \
    -out "${name}.crt" -days 825 -sha256 -extfile "${name}.ext"
  openssl pkcs8 -topk8 -nocrypt -in "${name}.key.tmp" -out "${name}.key"
  rm -f "${name}.key.tmp" "${name}.csr" "${name}.ext"
done

rm -f ca.srl
echo "Certificados em $CERTS"
ls -la
