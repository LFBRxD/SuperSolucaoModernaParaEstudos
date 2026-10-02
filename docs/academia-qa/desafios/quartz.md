# Desafio — Quartz

## Estado atual do oráculo

Não há scheduler. Pedido intermediário pode ficar parado.

## Contrato mínimo do espelho

- Um job Quartz que cancela pedido em espera depois de um prazo curto de lab
- Um `@Scheduled` diferente, documentado como mais fraco
- Log com `jobName`, `fireTime`, `orderId`
- Segunda execução não altera de novo um pedido já cancelado
- Intervalo de lab em segundos, com nota do valor que você usaria em produção

## Onde ler

https://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/tutorial-lesson-01.html

Semana 7.

## Validador

`validate-challenge.ps1 -Name quartz` procura dependência quartz e `@Scheduled`.
