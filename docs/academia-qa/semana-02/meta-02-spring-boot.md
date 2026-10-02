# Meta 2.2 — O que o Spring Boot sobe

Tempo previsto: **70 min**. Semana 2. Pré-requisito: meta 2.1.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 02**. Foco: a aplicação que escuta HTTP.


## O que é

Spring Boot sobe um servidor HTTP (Tomcat) e registra seus controllers. A classe com `@SpringBootApplication` é o começo. Uma porta em `application.yml` (`server.port`) é onde ele escuta.

## Por que existe neste sistema

Quando você não sabe 'onde o programa começa', qualquer erro vira mágica. O começo é a classe `main` e o `application.yml`.

## O que você faz com a mão

1. No oráculo, ache `ApiGatewayApplication.java` e a porta em `apps/api-gateway/src/main/resources/application.yml`.
2. Anote `server.port`.
3. Não copie essa classe para o projeto espelho. Só reconheça o formato.

## O que você deve ver

Você encontra a classe `main` e o número da porta no YAML.

## O que pode dar errado

Procurar a porta só no Compose e ignorar o YAML. Os dois precisam concordar.

## Onde ler a fonte oficial

https://spring.io/guides/gs/spring-boot

## Como saber que terminou

Você aponta o arquivo que liga a porta 11001 no gateway do oráculo.

## Perguntas para responder sozinho

- O que acontece se o YAML diz 8080 e o Compose publica 11001:11001?

## Próximo arquivo

[meta-03-controller.md](meta-03-controller.md)
