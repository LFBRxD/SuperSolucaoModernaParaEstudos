# OpenSSL

## O que ela enxerga

Certificado do mTLS.

## Onde

infra/certs

## Como usar neste lab

openssl x509 -in infra/certs/orders.crt -noout -subject -ext subjectAltName

## Fonte

docs/tutoriais/03-mtls-grpc.md

## Não serve para

Substituir as outras ferramentas da [lista](README.md).
