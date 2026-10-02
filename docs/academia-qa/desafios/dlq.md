# Desafio — DLQ e idempotência

## Estado atual do oráculo

Listener registra erro e não há fila morta.

## Contrato mínimo do espelho

- Após 3 falhas, a mensagem vai para tópico `lab.dlq` ou coleção `dead_letters`
- O registro tem orderId, erro e payload
- Replay é comando explícito
- Segunda aplicação do mesmo efeito não muda o estoque

## Onde ler

Semana 9. https://kafka.apache.org/documentation/#semantics

## Validador

`validate-challenge.ps1 -Name dlq` procura `dlq` ou `dead_letter` no espelho.
