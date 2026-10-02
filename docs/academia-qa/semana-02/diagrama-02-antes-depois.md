# Diagrama 2.2 — Espelho vazio e com catálogo

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 02**. Foco: checkpoint catalog-api.


## Figura

```mermaid
flowchart TB
  subgraph antes [Antes do lab 2.2]
    A1[processo na 11101]
    A2[sem rota de produtos]
  end
  subgraph depois [Depois do lab 2.2]
    B1[GET /api/products 200]
    B2[GET id ausente 404]
    B3[teste MockMvc verde]
  end
  antes --> depois
```

Este é o primeiro antes/depois do projeto espelho. Os próximos checkpoints seguem o mesmo desenho.

## O que observar

Compare os nomes desta figura com os nomes reais do código e do Compose (`api-gateway`, `orders.events`, portas 11000+). Se um nome divergir, anote: ou o diagrama está velho, ou você está olhando outro ambiente.

## Exercício

Redesenhe esta figura sem olhar, em papel ou Mermaid. Depois abra de novo e marque o que esqueceu.

## Próximo arquivo

Semana 3.
