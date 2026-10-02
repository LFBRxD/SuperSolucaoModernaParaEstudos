# Meta 3.4 — Isolar a massa de teste

Tempo previsto: **60 min**. Semana 3. Pré-requisito: meta 3.3.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 03**. Foco: um teste não suja o outro.


## O que é

Isolamento significa que o teste N começa de um estado conhecido, não do lixo do teste N-1. No lab, ou você reseta o volume, ou você usa dados que o teste cria e apaga, ou você aceita que o estoque só cai (o oráculo não devolve estoque se o pagamento falha — isso é um risco conhecido).

## Por que existe neste sistema

Sem isolamento, o smoke fica verde na segunda-feira e vermelho na terça porque o mouse acabou.

## O que você faz com a mão

1. Leia o risco em `docs/academia-qa/riscos-conhecidos.md` quando ele existir, ou em `docs/cenarios-qa.md` cenário 4: estoque não volta após falha de pagamento.
2. No espelho, decida: cada teste sobe um Mongo descartável ou limpa a coleção no `@BeforeEach`.
3. Escreva a decisão em uma frase.

## O que você deve ver

Uma frase de estratégia de limpeza no README do espelho.

## O que pode dar errado

Apagar o database de produção por engano. Neste curso só existe lab local. Mesmo assim, o comando de reset fica no script, não num `drop` solto sem nome do database.

## Onde ler a fonte oficial

https://www.mongodb.com/docs/manual/reference/method/db.collection.deleteMany/

## Como saber que terminou

Você aponta como o próximo teste encontra o estoque previsível.

## Perguntas para responder sozinho

- O oráculo compensa estoque hoje? Não. O que isso muda no seu teste?

## Próximo arquivo

[lab-03-teste-com-mongo.md](lab-03-teste-com-mongo.md)
