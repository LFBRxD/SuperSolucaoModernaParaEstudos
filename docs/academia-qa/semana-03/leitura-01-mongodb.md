# Leitura 3 — MongoDB para quem testa API

Tempo de leitura: **40 min**. Não substitua o lab. Leia, feche, e só então faça o lab.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 03**. Foco: semana 3.


## Por que esta leitura agora

Você já viu um documento. A leitura evita confundir coleção, database e o JSON da API.

### Database e coleção

O servidor tem databases. Cada database tem coleções. Cada coleção tem documentos. No oráculo o servidor é um só e os databases separam os serviços. Um serviço não deve ler o database do outro.

### O que o QA confere

Id, quantidade, status do pedido, e-mail. Não precisa virar administrador de índice nesta semana.

### Cuidado

Atualizar documento na mão muda o que a API mostra e esconde bug. Use só para investigar e desfaça ou resete.

## Fontes

- https://www.mongodb.com/docs/manual/core/databases-and-collections/
- https://www.mongodb.com/docs/mongodb-shell/

## Perguntas de revisão

- Por que orders e inventory não compartilham a mesma coleção?
- O que `down -v` faz com o seed?

## Próximo arquivo

Semana 4.
