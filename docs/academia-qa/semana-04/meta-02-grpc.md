# Meta 4.2 — Chamada gRPC

Tempo previsto: **70 min**. Semana 4. Pré-requisito: meta 4.1.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 04**. Foco: RPC com deadline e status.


## O que é

gRPC é uma chamada de função pela rede. O cliente tem um stub (objeto gerado). O servidor implementa o método. Status não é HTTP: `NOT_FOUND`, `INVALID_ARGUMENT`, `DEADLINE_EXCEEDED`, `UNAVAILABLE`. O gateway transforma isso em 404, 400, 504, 502.

## Por que existe neste sistema

Quando a tela mostra 502, o browser não chegou no estoque. O gateway não conseguiu completar a chamada interna. Você precisa saber em qual trecho olhar.

## O que você faz com a mão

1. No oráculo, ache `GrpcClients.java` e veja os endereços.
2. No Compose, confirme `ORDERS_GRPC_ADDRESS` e `INVENTORY_GRPC_ADDRESS`.
3. Leia um método do `ApiController` que chama o stub.

## O que você deve ver

Você descreve: HTTP entra no gateway, gRPC sai para o inventory.

## O que pode dar errado

Tratar 502 como 'estoque vazio'. 502 é falha de chamar o serviço, não regra de negócio.

## Onde ler a fonte oficial

https://grpc.io/docs/what-is-grpc/core-concepts/

## Como saber que terminou

Você diferencia 404 de produto e 502 de serviço caído.

## Perguntas para responder sozinho

- O que é deadline?
- O que o cliente deve fazer se o prazo estoura?

## Próximo arquivo

[lab-01-ler-o-proto.md](lab-01-ler-o-proto.md)
