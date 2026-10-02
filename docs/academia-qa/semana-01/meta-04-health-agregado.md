# Meta 1.4 — Health agregado

Tempo previsto: **60 min**. Semana 1. Pré-requisito: meta 1.3.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 01**. Foco: saber se o sistema está no ar.


## O que é

Health é uma resposta curta que diz se o processo consegue trabalhar. O gateway junta o health de orders, inventory, payments, notifications e ainda pergunta o gRPC do estoque. O campo `overall` só fica `UP` se as partes importantes responderem.

## Por que existe neste sistema

Antes de testar pedido, você prova que a base está viva. Um pedido que falha com a stack caída não ensina saga.

## O que você faz com a mão

1. Abra http://localhost:11000/health (pode pedir login em algumas rotas; health da API é público).
2. Chame `GET http://localhost:11001/api/health` sem token.
3. Compare a lista de serviços com o Compose.

## O que você deve ver

`overall` igual a `UP` e cada serviço listado como `UP`, incluindo `inventory-grpc`.

## O que pode dar errado

Subir o Compose e testar em 5 segundos. Java ainda está iniciando. Espere e repita.

## Onde ler a fonte oficial

https://docs.spring.io/spring-boot/reference/actuator/endpoints.html

## Como saber que terminou

Você sabe qual URL é pública e qual tela da web mostra o mesmo dado.

## Perguntas para responder sozinho

- Health 200 prova que um pedido vai confirmar?
- Não. Por quê?

## Próximo arquivo

[lab-03-devtools.md](lab-03-devtools.md)
