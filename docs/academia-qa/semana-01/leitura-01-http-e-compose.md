# Leitura 1 — HTTP e Compose, só o que o lab usa

Tempo de leitura: **50 min**. Não substitua o lab. Leia, feche, e só então faça o lab.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 01**. Foco: fechar a semana 1.


## Por que esta leitura agora

Você já operou. Esta leitura dá nome ao que você viu, para a semana 2 não começar no escuro.

### HTTP

Método diz a intenção. `GET` lê. `POST` cria. `PUT` substitui. O status diz o resultado: 200 ok, 401 não autenticado, 403 autenticado porém sem permissão, 404 não achei, 500 o servidor quebrou. Cabeçalho `Authorization` carrega o token. Corpo JSON carrega os dados.

### Compose

O arquivo declara serviços, imagens, portas, variáveis e volumes. `up -d` sobe em segundo plano. `ps` lista. `logs` mostra a saída do processo. `down` para. `down -v` apaga também os dados do Mongo.

### O que ainda não é sua função

Não decore gRPC nem Kafka nesta leitura. Só saiba que o gateway esconde esses detalhes da tela.

## Fontes

- https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status
- https://docs.docker.com/compose/intro/compose-application-model/

## Perguntas de revisão

- Qual status você espera sem token em `/api/products`? Você ainda não testou; chute e anote para a semana 8.
- O que `down -v` apaga que `down` não apaga?

## Próximo arquivo

Semana 2, [meta-01-jvm-e-maven.md](../semana-02/meta-01-jvm-e-maven.md)
