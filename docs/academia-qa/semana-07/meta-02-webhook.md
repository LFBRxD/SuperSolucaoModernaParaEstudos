# Meta 7.2 — Webhook com assinatura e retry

Tempo previsto: **75 min**. Semana 7. Pré-requisito: meta 7.1.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 07**. Foco: HTTP de saída.


## O que é

Webhook é um POST seu para a URL do cliente, com corpo do evento e uma assinatura (HMAC) para o cliente saber que foi você. Timeout curto. Se falhar, tenta de novo poucas vezes. Sem assinatura, qualquer um forja o evento.

## Por que existe neste sistema

Kafka não avisa um sistema que não é consumidor seu. Webhook avisa. Os dois podem coexistir.

## O que você faz com a mão

1. Leia o desafio `docs/academia-qa/desafios/webhook.md` até a seção de contrato, sem implementar ainda.
2. Desenhe: orders confirma → notificador → POST no receptor local.
3. Anote o header de assinatura que você vai exigir.

## O que você deve ver

Desenho com timeout e número máximo de tentativas.

## O que pode dar errado

Retry infinito. Isso derruba o receptor e o seu serviço.

## Onde ler a fonte oficial

https://hookdeck.com/webhooks/guides/what-are-webhooks (conceito; ignore o produto)

## Como saber que terminou

Você explica por que HMAC existe.

## Perguntas para responder sozinho

- O que o receptor deve fazer se a assinatura não bater?

## Próximo arquivo

[meta-03-scheduled.md](meta-03-scheduled.md)
