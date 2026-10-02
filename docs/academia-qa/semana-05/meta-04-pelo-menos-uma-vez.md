# Meta 5.4 — Entrega pelo menos uma vez

Tempo previsto: **60 min**. Semana 5. Pré-requisito: meta 5.3.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 05**. Foco: a mesma mensagem pode chegar duas vezes.


## O que é

O consumidor pode processar a mensagem e falhar antes de gravar o offset. Kafka entrega de novo. O efeito (baixar estoque, criar notificação) precisa ser idempotente: fazer duas vezes não pode cobrar duas vezes.

## Por que existe neste sistema

O oráculo não garante isso de ponta a ponta. É um risco. No espelho, você vai tratar isso nas semanas 7 e 9.

## O que você faz com a mão

1. Leia o risco no hub `riscos-conhecidos.md`.
2. Escreva um exemplo: `OrderCreated` processado duas vezes. O que aconteceria com o estoque se o código só fizesse `quantity - 1` sem checar o pedido.
3. Não implemente a trava ainda.

## O que você deve ver

Um parágrafo seu sobre duplicata.

## O que pode dar errado

Achar que Kafka entrega exatamente uma vez só porque 'é Kafka'. Não neste lab.

## Onde ler a fonte oficial

https://kafka.apache.org/documentation/#semantics

## Como saber que terminou

Você diz 'pelo menos uma vez' com um exemplo de estoque.

## Perguntas para responder sozinho

- Onde você registraria que o orderId já foi reservado?

## Próximo arquivo

[lab-03-evento-no-espelho.md](lab-03-evento-no-espelho.md)
