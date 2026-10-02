# Meta 1.2 — Processo, porta e HTTP

Tempo previsto: **70 min**. Semana 1. Pré-requisito: meta 1.1.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 01**. Foco: uma requisição HTTP.


## O que é

Um processo é um programa em execução. Uma porta é o número da porta de entrada desse processo na máquina (ou no container). HTTP é o texto do pedido e da resposta: método (`GET`, `POST`), caminho (`/api/health`), cabeçalhos e corpo.

## Por que existe neste sistema

Quase todo bug de 'não abre' neste lab é porta errada, processo morto ou HTTP 401 porque faltou o token. Se você não distingue isso, vai culpar o código.

## O que você faz com a mão

1. No PowerShell: `curl.exe -i http://localhost:11001/api/health`.
2. Leia a primeira linha da resposta (código HTTP) e o corpo JSON.
3. Repita com a porta 11000 e anote que a resposta é HTML, não JSON.

## O que você deve ver

Status HTTP 200 no health e um JSON com `overall`. Na porta 11000, HTML da web.

## O que pode dar errado

Usar `curl` do PowerShell sem `.exe` pode ser um alias que esconde o código HTTP. Prefira `curl.exe -i`.

## Onde ler a fonte oficial

https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Overview

## Como saber que terminou

Você explica a diferença entre porta 11000 e 11001 sem olhar a tabela.

## Perguntas para responder sozinho

- O que é um código 200?
- Por que health e a página web não são a mesma porta?

## Próximo arquivo

[lab-02-health-web-e-api.md](lab-02-health-web-e-api.md)
