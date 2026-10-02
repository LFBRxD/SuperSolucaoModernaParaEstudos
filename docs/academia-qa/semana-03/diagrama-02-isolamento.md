# Diagrama 3.2 — Dois Mongos

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 03**. Foco: não misturar oráculo e espelho.


## Figura

```mermaid
flowchart TB
  Oraculo[apps do oraculo] --> P11008["Mongo host 11008"]
  Espelho[catalogo do espelho] --> P11108["Mongo host 11108"]
```

Seta cruzada é bug de configuração. Se o espelho gravar no 11008, você contaminou o lab.

## O que observar

Compare os nomes desta figura com os nomes reais do código e do Compose (`api-gateway`, `orders.events`, portas 11000+). Se um nome divergir, anote: ou o diagrama está velho, ou você está olhando outro ambiente.

## Exercício

Redesenhe esta figura sem olhar, em papel ou Mermaid. Depois abra de novo e marque o que esqueceu.

## Próximo arquivo

Semana 4.
