# Meta 9.2 — SLI simples

Tempo previsto: **55 min**. Semana 9. Pré-requisito: meta 9.1.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 09**. Foco: número que vira orçamento.


## O que é

SLI é o indicador: por exemplo, porcentagem de pedidos que chegam a estado final em 60 segundos. SLO é a meta: por exemplo, 99% no lab. Sem o indicador, 'está lento' não é testável.

## Por que existe neste sistema

Na semana 11 você mede. Hoje você escolhe o indicador e escreve como contar.

## O que você faz com a mão

1. Defina um SLI: tempo até CONFIRMED ou CANCELLED.
2. Defina um SLO de lab frouxo o bastante para a sua máquina, e anote a máquina.
3. Não escolha 'CPU baixa'. Isso não é o que o usuário sente.

## O que você deve ver

Uma frase SLI e uma frase SLO.

## O que pode dar errado

SLO de 50 ms copiado de blog, impossível com saga e Docker no notebook.

## Onde ler a fonte oficial

https://sre.google/sre-book/service-level-objectives/

## Como saber que terminou

O SLI cabe numa linha e você sabe de qual timestamp até qual timestamp.

## Perguntas para responder sozinho

- O health UP entra nesse SLI? Não. Por quê?

## Próximo arquivo

[meta-03-dlq.md](meta-03-dlq.md)
