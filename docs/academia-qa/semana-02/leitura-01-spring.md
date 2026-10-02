# Leitura 2 — Spring Boot só até o primeiro REST

Tempo de leitura: **45 min**. Não substitua o lab. Leia, feche, e só então faça o lab.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 02**. Foco: depois dos labs da semana 2.


## Por que esta leitura agora

Fixar o vocabulário que você acabou de usar no projeto espelho.

### Stereotypes

`@RestController` marca a classe HTTP. `@Service` marca a regra. `@Repository` marca o acesso a dados. São anotações. O Spring cria os objetos e liga um no outro (injeção).

### Configuração

`application.yml` guarda porta, URL de banco e flags. O que muda entre máquinas fica aqui, não espalhado no Java.

### Teste de fatia

MockMvc chama o controller sem abrir porta de verdade. Serve para status e JSON. Não serve para provar Docker.

## Fontes

- https://spring.io/guides/gs/rest-service
- https://docs.spring.io/spring-boot/reference/testing/spring-boot-applications.html

## Perguntas de revisão

- Quem pode lançar 404: o controller ou o repositório?
- Por que o teste desta semana não sobe Kafka?

## Próximo arquivo

Semana 3.
