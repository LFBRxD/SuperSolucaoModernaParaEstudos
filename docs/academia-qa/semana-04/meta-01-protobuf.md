# Meta 4.1 — O que é um .proto

Tempo previsto: **70 min**. Semana 4. Pré-requisito: semana 3.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 04**. Foco: contrato entre processos.


## O que é

Protobuf é um formato de contrato. O arquivo `.proto` descreve mensagens e métodos. O compilador gera código Java. Quem chama e quem atende precisam usar o mesmo contrato, senão a chamada nem deserializa.

## Por que existe neste sistema

No oráculo, o browser não fala protobuf. O gateway traduz REST para gRPC. O contrato está em `libs/proto/src/main/proto/`.

## O que você faz com a mão

1. Abra `inventory.proto` e `orders.proto`.
2. Anote um método de cada (`ListProducts` ou equivalente, `CreateOrder`).
3. Não gere código ainda. Só leia os nomes dos campos.

## O que você deve ver

Uma lista de métodos RPC que você consegue ler em voz alta.

## O que pode dar errado

Achar que o JSON do Swagger é o contrato interno. Ele é o contrato da borda. O `.proto` é o contrato entre gateway e serviço.

## Onde ler a fonte oficial

https://protobuf.dev/getting-started/javatutorial/

## Como saber que terminou

Você aponta o arquivo .proto de estoque sem procurar mais de um minuto.

## Perguntas para responder sozinho

- Quem edita o .proto: o frontend ou o time dos dois serviços?

## Próximo arquivo

[meta-02-grpc.md](meta-02-grpc.md)
