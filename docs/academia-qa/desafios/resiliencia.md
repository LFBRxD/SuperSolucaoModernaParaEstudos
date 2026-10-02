# Desafio — resiliência

## O que observar no oráculo

Pare `payments-service`, crie um pedido, veja em que status ele fica, suba o serviço de novo.

## O que construir no espelho

- Deadline na chamada interna
- Job de expiração (desafio Quartz)
- Idempotência (desafio DLQ)

Não use ferramenta de ataque. `docker compose stop` no seu Compose basta.
