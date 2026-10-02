# Meta 2.5 — O primeiro teste automatizado

Tempo previsto: **70 min**. Semana 2. Pré-requisito: meta 2.4.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 02**. Foco: repetir o que a mão já viu.


## O que é

JUnit roda métodos de teste. `spring-boot-starter-test` sobe o suficiente para chamar o controller sem Docker. Assert é a frase 'o status tem que ser 200' escrita em código.

## Por que existe neste sistema

Automatizar antes de ver com a mão gera teste que você não sabe depurar. Você já vai ter visto o curl. O teste só congela esse curl.

## O que você faz com a mão

1. Escreva em português o assert: GET /api/products devolve 200 e uma lista não vazia.
2. Só depois procure `@SpringBootTest` ou `MockMvc` no guia do Spring.
3. Um teste. Não uma suíte.

## O que você deve ver

Um teste verde no `mvn test` do projeto espelho.

## O que pode dar errado

Teste que sobe Mongo sem você ter Mongo. Nesta semana o repositório é memória, então o teste não precisa de Docker.

## Onde ler a fonte oficial

https://docs.spring.io/spring-boot/reference/testing/spring-boot-applications.html

## Como saber que terminou

`mvn test` passa e você sabe qual request ele faz.

## Perguntas para responder sozinho

- O que o teste não cobre ainda? (resposta esperada: banco, gRPC, Kafka)

## Próximo arquivo

[lab-03-ver-no-swagger.md](lab-03-ver-no-swagger.md)
