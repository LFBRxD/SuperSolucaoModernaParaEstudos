# Leitura 4 — gRPC em uma página

Tempo de leitura: **40 min**. Não substitua o lab. Leia, feche, e só então faça o lab.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 04**. Foco: semana 4.


## Por que esta leitura agora

Dar nome a stub, status e deadline depois de você ter visto a chamada quebrar.

### Stub

Classe gerada que parece um método local e esconde o socket.

### Status

O erro semântico do RPC. O gateway é quem decide o HTTP.

### Deadline

Tempo máximo que o cliente espera. Sem deadline, uma chamada presa segura a thread do gateway.

## Fontes

- https://grpc.io/docs/what-is-grpc/core-concepts/
- https://grpc.io/docs/guides/status-codes/

## Perguntas de revisão

- Por que o browser não chama gRPC neste lab?
- Qual status gRPC você mapearia para HTTP 404?

## Próximo arquivo

Semana 5.
