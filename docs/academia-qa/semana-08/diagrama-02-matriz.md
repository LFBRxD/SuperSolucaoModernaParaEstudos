# Diagrama 8.2 — 401, 403, 200

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 08**. Foco: estoque.


## Figura

```mermaid
flowchart LR
  A[sem Authorization] --> R401[401]
  B[Bearer USER] --> R403[403 PUT stock]
  C[Bearer ADMIN] --> R200[200 PUT stock]
```

Produtos e pedidos aceitam USER. Stock não.

## O que observar

Compare os nomes desta figura com os nomes reais do código e do Compose (`api-gateway`, `orders.events`, portas 11000+). Se um nome divergir, anote: ou o diagrama está velho, ou você está olhando outro ambiente.

## Exercício

Redesenhe esta figura sem olhar, em papel ou Mermaid. Depois abra de novo e marque o que esqueceu.

## Próximo arquivo

Semana 9.
