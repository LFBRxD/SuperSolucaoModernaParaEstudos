# Meta 4.4 — Mapear status gRPC para HTTP

Tempo previsto: **65 min**. Semana 4. Pré-requisito: meta 4.3.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 04**. Foco: o QA vê HTTP, a causa pode ser gRPC.


## O que é

Uma tabela de mapeamento evita discussão. `NOT_FOUND` → 404. `INVALID_ARGUMENT` → 400. `UNAVAILABLE` → 502. `DEADLINE_EXCEEDED` → 504. O corpo deve dizer qual serviço falhou, senão você só vê 'erro'.

## Por que existe neste sistema

No espelho você vai separar catálogo e um segundo processo. Sem essa tabela, o teste de contrato fica instável.

## O que você faz com a mão

1. Escreva a tabela acima no README do espelho antes de codar.
2. No oráculo, force um caso: pare o inventory (`docker compose stop inventory-service`) e chame produtos autenticado. Anote o HTTP. Suba de novo.
3. Não deixe o serviço parado.

## O que você deve ver

Um status anotado com o inventory parado, e a stack saudável de novo no final.

## O que pode dar errado

Esquecer de `docker compose start inventory-service` e achar que 'o lab quebrou' no dia seguinte.

## Onde ler a fonte oficial

https://grpc.io/docs/guides/status-codes/

## Como saber que terminou

A tabela está escrita e você viu pelo menos um erro de verdade.

## Perguntas para responder sozinho

- 504 e 502. Qual sugere timeout e qual sugere serviço inalcançável?

## Próximo arquivo

[lab-03-contrato.md](lab-03-contrato.md)
