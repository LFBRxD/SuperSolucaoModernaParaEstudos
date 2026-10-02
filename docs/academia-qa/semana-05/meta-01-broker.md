# Meta 5.1 — O que é o broker Kafka

Tempo previsto: **70 min**. Semana 5. Pré-requisito: semana 4.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 05**. Foco: fila durável de eventos.


## O que é

Kafka guarda mensagens em tópicos. Quem publica não chama quem consome. O processo que publica pode cair depois de gravar a mensagem. Quem consome lê no próprio ritmo. Isso é diferente de uma chamada gRPC, que espera a resposta na hora.

## Por que existe neste sistema

A saga do pedido só anda porque existem tópicos. Se você só olha o HTTP, o status muda 'sozinho' e você não sabe por quê.

## O que você faz com a mão

1. No Compose, ache o serviço `kafka` e a porta do host `11009`.
2. Dentro da rede, os serviços usam `kafka:9092`. Do seu PC, a porta é `11009`.
3. Abra a Kafka UI em http://localhost:11016 depois que o Compose subir com o serviço `kafka-ui`.

## O que você deve ver

A UI lista o cluster `studyshop` ou mostra os tópicos `orders.events`, `inventory.events`, `payments.events` depois de um pedido.

## O que pode dar errado

Conectar a UI em `localhost:11009` de dentro do container da UI. A UI está na rede Docker e deve usar `kafka:9092`.

## Onde ler a fonte oficial

https://kafka.apache.org/documentation/#gettingStarted

## Como saber que terminou

Você explica broker, tópico e por que a porta do host não é a porta interna.

## Perguntas para responder sozinho

- gRPC espera resposta. Kafka espera o quê do produtor?

## Próximo arquivo

[lab-01-kafka-ui.md](lab-01-kafka-ui.md)
