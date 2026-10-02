# Meta 1.3 — Container e Docker Compose

Tempo previsto: **75 min**. Semana 1. Pré-requisito: meta 1.2.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 01**. Foco: vários processos sob o Compose.


## O que é

Um container é um processo isolado com seu próprio sistema de arquivos e sua própria rede. O Docker Compose sobe vários containers a partir de um arquivo `infra/docker-compose.yml`. O nome `localhost` dentro de um container não é o seu Windows.

## Por que existe neste sistema

Os serviços se acham por nome (`kafka`, `mongodb`), não por `localhost`. Quando um log diz 'connection refused' em `localhost:11009` dentro do container, o endereço está errado para aquele mundo.

## O que você faz com a mão

1. Abra `infra/docker-compose.yml` e encontre o serviço `api-gateway`.
2. Anote a porta publicada (`11001:11001`) e uma variável `ORDERS_GRPC_ADDRESS`.
3. Rode `docker compose ps` dentro de `infra` e veja a coluna STATUS.

## O que você deve ver

Serviços com status running ou healthy. A porta da esquerda é a do seu computador; a da direita é a de dentro do container.

## O que pode dar errado

Rodar `docker compose` fora da pasta `infra` e o Docker não achar o arquivo. Entre na pasta ou use `-f`.

## Onde ler a fonte oficial

https://docs.docker.com/compose/intro/features-uses/

## Como saber que terminou

Você aponta um `depends_on` e diz qual serviço espera o outro.

## Perguntas para responder sozinho

- Por que o gateway usa `orders-service:11003` e não `localhost:11003`?

## Próximo arquivo

[diagrama-01-stack-e-portas.md](diagrama-01-stack-e-portas.md)
