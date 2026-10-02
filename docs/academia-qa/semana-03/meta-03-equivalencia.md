# Meta 3.3 — Classes de equivalência e limites

Tempo previsto: **70 min**. Semana 3. Pré-requisito: meta 3.2.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 03**. Foco: escolher poucos testes que representam muitos.


## O que é

Classe de equivalência é um grupo de entradas que o sistema trata igual. Limite é a borda: estoque 1 com quantidade 1 passa; quantidade 2 não. Testar 3, 4 e 5 não ensina mais se a regra é 'maior que o estoque'.

## Por que existe neste sistema

`prod-raro` existe para o limite. Quantidade 2 é o caso de estoque insuficiente. Quantidade 1 é o feliz. Zero e negativo são inválidos se a API validar.

## O que você faz com a mão

1. Escreva uma tabela: quantidade 1, 2, 0, -1 para `prod-raro`.
2. Marque o resultado que você espera (ainda pode chutar o 0 e o -1).
3. Não dispare os pedidos da saga ainda; isso é semana 6. Aqui o foco é o desenho dos casos.

## O que você deve ver

Tabela com quatro linhas e uma coluna 'já executei? não'.

## O que pode dar errado

Testar só o caminho feliz e achar que cobriu o estoque.

## Onde ler a fonte oficial

https://en.wikipedia.org/wiki/Equivalence_partitioning

## Como saber que terminou

A tabela existe no relatório antes de você automatizar.

## Perguntas para responder sozinho

- Por que quantidade 3 no `prod-raro` não é um caso novo se 2 já rejeita?

## Próximo arquivo

[lab-02-persistir-no-espello.md](lab-02-persistir-no-espello.md)
