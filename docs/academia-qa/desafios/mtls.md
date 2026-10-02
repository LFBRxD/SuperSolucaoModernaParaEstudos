# Desafio — mTLS

## Estado atual do oráculo

Já existe. Tutorial `docs/tutoriais/03-mtls-grpc.md`, overlay `infra/docker-compose.mtls.yml`, certs em `infra/certs`.

## O que você faz

Executa o tutorial, quebra a confiança, restaura. No espelho, mTLS é opcional no capstone. Não é desculpa para pular o lab 8.3 no oráculo.

## Validador

`validate-challenge.ps1 -Name mtls` confere os arquivos do oráculo, não do espelho.
