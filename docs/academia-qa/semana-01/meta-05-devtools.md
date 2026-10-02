# Meta 1.5 — DevTools do navegador

Tempo previsto: **70 min**. Semana 1. Pré-requisito: meta 1.4.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 01**. Foco: ver a request que a tela fez.


## O que é

O DevTools é o inspetor do navegador. A aba Network mostra cada pedido HTTP: URL, método, status, cabeçalhos e corpo. A aba Application mostra o que ficou gravado no navegador (neste lab, o token em localStorage).

## Por que existe neste sistema

A tela pode mentir por cache ou por estado velho. A aba Network mostra o que realmente foi para o gateway.

## O que você faz com a mão

1. Abra http://localhost:11000, F12, aba Network, marque Preserve log.
2. Faça login `qa` / `qa123`.
3. Clique no pedido `login` e leia o status e o JSON (não copie o token para lugar público).

## O que você deve ver

Um POST `/api/auth/login` com 200 e, nas chamadas seguintes, o cabeçalho `Authorization: Bearer ...`.

## O que pode dar errado

Filtrar só por Img e achar que a API não foi chamada. Filtre por Fetch/XHR.

## Onde ler a fonte oficial

https://developer.chrome.com/docs/devtools/network

## Como saber que terminou

Você acha o login na Network e diz se a próxima chamada de produtos levou o token.

## Perguntas para responder sozinho

- Onde o browser guarda o token neste lab?
- O que acontece se você apagar o localStorage e atualizar a página?

## Próximo arquivo

[lab-04-desenhar-o-caminho.md](lab-04-desenhar-o-caminho.md)
