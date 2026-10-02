# Meta 6.4 — Seguir o orderId

Tempo previsto: **70 min**. Semana 6. Pré-requisito: meta 6.3.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 06**. Foco: uma chave em todos os lugares.


## O que é

O `orderId` liga API, documento no Mongo `orders`, mensagens nos três tópicos, pagamento e notificação. Sem ele você está olhando eventos de outra pessoa no lab.

## Por que existe neste sistema

Investigação distribuída começa pela correlação, não pelo log inteiro.

## O que você faz com a mão

1. Pegue um orderId finalizado.
2. Ache-o na API, no mongosh do database `orders`, e em uma mensagem Kafka.
3. Escreva os três lugares.

## O que você deve ver

Três evidências com o mesmo id.

## O que pode dar errado

Filtrar Kafka por e-mail e misturar pedidos.

## Onde ler a fonte oficial

docs/academia-qa/ferramentas/kafka-ui.md

## Como saber que terminou

Os três lugares estão no relatório.

## Perguntas para responder sozinho

- Qual lugar você olha primeiro quando o status não muda?

## Próximo arquivo

[lab-03-redesenhar.md](lab-03-redesenhar.md)
