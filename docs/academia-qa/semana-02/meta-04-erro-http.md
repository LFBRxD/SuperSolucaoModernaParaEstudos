# Meta 2.4 — Erro HTTP de propósito

Tempo previsto: **60 min**. Semana 2. Pré-requisito: meta 2.3.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 02**. Foco: 404 e 400 que você controla.


## O que é

Um erro bom diz o que faltou sem despejar stack trace no cliente. Produto inexistente vira 404. Quantidade negativa vira 400. Erro inesperado vira 500 e deve aparecer no log, não como texto cru na API se você tratar.

## Por que existe neste sistema

QA vive de casos negativos. Se a API só tem caminho feliz, você não tem o que assertar.

## O que você faz com a mão

1. Defina dois casos no papel: id que não existe; quantidade menor que zero.
2. Escreva o status esperado ao lado de cada caso.
3. No oráculo, um produto inexistente no gateway tende a virar erro gRPC mapeado. Você ainda não precisa reproduzir gRPC.

## O que você deve ver

Tabela de três linhas: caso, status, corpo mínimo (`message` ou vazio documentado).

## O que pode dar errado

Devolver 200 com `{ "error": true }`. Isso esconde a falha de quem automatiza pelo status.

## Onde ler a fonte oficial

https://datatracker.ietf.org/doc/html/rfc9110#name-status-codes

## Como saber que terminou

Sua API de catálogo em memória tem pelo menos um 404 testado à mão.

## Perguntas para responder sozinho

- 400 e 404 respondem problemas diferentes. Qual é qual?

## Próximo arquivo

[lab-02-endpoint-catalogo.md](lab-02-endpoint-catalogo.md)
