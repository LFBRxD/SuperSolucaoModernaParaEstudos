# Diagrama 8.1 — Três momentos

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 08**. Foco: quem prova o quê.


## Figura

```mermaid
flowchart TB
  User[usuario qa] -->|JWT ou OIDC| Gw[api-gateway]
  Gw -->|mTLS| Ord[orders]
  Gw -->|mTLS| Inv[inventory]
```

A seta de cima identifica a pessoa. A de baixo identifica o processo.

## O que observar

Compare os nomes desta figura com os nomes reais do código e do Compose (`api-gateway`, `orders.events`, portas 11000+). Se um nome divergir, anote: ou o diagrama está velho, ou você está olhando outro ambiente.

## Exercício

Redesenhe esta figura sem olhar, em papel ou Mermaid. Depois abra de novo e marque o que esqueceu.

## Próximo arquivo

[diagrama-02-matriz.md](diagrama-02-matriz.md)
