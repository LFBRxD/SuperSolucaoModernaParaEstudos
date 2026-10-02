# Meta 3.1 — Documento e coleção

Tempo previsto: **70 min**. Semana 3. Pré-requisito: semana 2.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 03**. Foco: dado que sobrevive ao restart.


## O que é

MongoDB guarda documentos JSON em coleções. Não há tabela rígida como em SQL, mas o seu código precisa de um formato estável. No oráculo, cada serviço tem um database: `orders`, `inventory`, `payments`, `notifications`, todos no mesmo servidor (porta 11008 no host).

## Por que existe neste sistema

A lista em memória da semana 2 morre quando o processo cai. Pedido de verdade precisa continuar lá depois do restart. QA precisa olhar o banco para ver se a API mentiu.

## O que você faz com a mão

1. Com a stack no ar: `docker compose exec mongodb mongosh --eval "show dbs"` a partir de `infra`.
2. Entre no database `inventory` e rode `db.products.find().limit(2)` ou `db.product.find()` se o nome da coleção vier no plural da entidade.
3. Anote um produto seed: id e quantidade.

## O que você deve ver

Pelo menos um documento de produto com quantidade numérica.

## O que pode dar errado

O nome da coleção pode ser `product` (classe) e não `products`. Se `find` voltar vazio, rode `show collections`.

## Onde ler a fonte oficial

https://www.mongodb.com/docs/manual/core/document/

## Como saber que terminou

Você mostra um documento real, não o JSON da API.

## Perguntas para responder sozinho

- Qual a diferença entre o JSON da API e o documento no Mongo?

## Próximo arquivo

[lab-01-mongosh.md](lab-01-mongosh.md)
