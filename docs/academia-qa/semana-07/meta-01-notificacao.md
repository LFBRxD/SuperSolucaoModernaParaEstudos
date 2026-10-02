# Meta 7.1 — Notificação não é webhook

Tempo previsto: **60 min**. Semana 7. Pré-requisito: semana 6.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 07**. Foco: o que o oráculo faz hoje.


## O que é

O notifications-service lê `OrderConfirmed` e `OrderCancelled`, grava um documento e expõe GET no gateway. Ninguém chama um sistema externo. Não há HTTP de saída. Webhook seria o contrário: o seu sistema chama uma URL de terceiro quando algo acontece.

## Por que existe neste sistema

Quem testa 'se o e-mail saiu' neste oráculo não vai achar e-mail. Vai achar um documento e um GET.

## O que você faz com a mão

1. Crie um pedido até o estado final.
2. GET `http://localhost:11001/api/notifications/order/{orderId}` com Bearer.
3. Veja também o Mongo do database `notifications`.

## O que você deve ver

Pelo menos uma notificação para o orderId.

## O que pode dar errado

Procurar webhook no código do oráculo e achar que você está cego. Ele não existe. Você vai construir no espelho.

## Onde ler a fonte oficial

apps/notifications-service NotificationController

## Como saber que terminou

Você descreve a diferença em duas frases.

## Perguntas para responder sozinho

- A UI mostra notificação? Não. Onde você olha então?

## Próximo arquivo

[lab-01-ver-notificacao.md](lab-01-ver-notificacao.md)
