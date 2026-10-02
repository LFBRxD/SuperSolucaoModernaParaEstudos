# Meta 11.2 — Acessibilidade automatizada

Tempo previsto: **50 min**. Semana 11. Pré-requisito: semana 10.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 11**. Foco: a UI não é só o caminho feliz visual.


## O que é

axe procura problemas objetivos: botão sem nome, contraste ruim, input sem label. Não substitui usar a tela com teclado, mas pega o que você não vê.

## Por que existe neste sistema

O spec `a11y.spec.ts` roda axe na tela de login e no catálogo depois do login.

## O que você faz com a mão

1. Leia o spec.
2. Rode só ele.
3. Se falhar, leia a regra do axe. Não dê disable na regra sem anotar o motivo.

## O que você deve ver

Relatório do axe lido, verde ou com uma violação explicada.

## O que pode dar errado

Desligar todas as regras para ficar verde.

## Onde ler a fonte oficial

https://github.com/dequelabs/axe-core/blob/develop/doc/rule-descriptions.md

## Como saber que terminou

Você cita uma regra pelo nome.

## Perguntas para responder sozinho

- O que o axe não testa? (fluxo de pedido, saga)

## Próximo arquivo

[lab-02-seguranca-passiva.md](lab-02-seguranca-passiva.md)
