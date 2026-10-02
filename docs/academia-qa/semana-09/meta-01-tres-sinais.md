# Meta 9.1 — Log, métrica e trace

Tempo previsto: **70 min**. Semana 9. Pré-requisito: semana 6.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 09**. Foco: três jeitos de olhar a mesma request.


## O que é

Log é uma linha sobre um fato. Métrica é um número ao longo do tempo (quantas requests, quantos erros). Trace é o caminho de uma request pelos serviços, com um trace id. Os três se completam. Um sozinho mente por omissão.

## Por que existe neste sistema

No lab, o trace vai do serviço ao OpenTelemetry Collector e ao Jaeger (11011). Métrica o Prometheus busca no actuator (11012). Log você lê com `docker compose logs`.

## O que você faz com a mão

1. Faça um pedido feliz.
2. Abra o Jaeger e filtre pelo serviço `api-gateway` no horário do pedido.
3. Abra um log do `orders-service` no mesmo minuto.

## O que você deve ver

Um trace e uma linha de log que você acredita serem do mesmo pedido.

## O que pode dar errado

Procurar o orderId no Prometheus. Lá estão agregados, não o id, a menos que alguém tenha colocado label de alta cardinalidade (não faça isso).

## Onde ler a fonte oficial

https://opentelemetry.io/docs/what-is-opentelemetry/

## Como saber que terminou

Você diz o que cada ferramenta responde: o quê aconteceu, quanto aconteceu, por onde passou.

## Perguntas para responder sozinho

- Qual das três mostra o orderId com mais facilidade hoje?

## Próximo arquivo

[lab-01-jaeger.md](lab-01-jaeger.md)
