# Desafio — webhook

## Estado atual do oráculo

Não há HTTP de saída. Notificação é documento + GET.

## Contrato mínimo do espelho

- POST para `http://127.0.0.1:11180/hooks/orders`
- Corpo JSON com `eventId`, `eventType`, `orderId`
- Header `X-Signature`: hex de HMAC-SHA256 do corpo cru, segredo no YAML de lab
- Timeout de 2 segundos
- No máximo 3 tentativas
- Receptor devolve 401 se a assinatura não bater
- O mesmo `eventId` não aplica efeito duas vezes

## Onde ler

Semana 7, meta 7.2 e lab 7.3. RFC de HMAC: https://datatracker.ietf.org/doc/html/rfc2104

## Validador

Procura as strings `X-Signature` e `11180` no projeto espelho (`checkpoint` não cobre sozinho; veja `scripts/academy/validate-challenge.ps1 -Name webhook`).
