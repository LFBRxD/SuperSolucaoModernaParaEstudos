# Meta 9.4 — Idempotência

Tempo previsto: **65 min**. Semana 9. Pré-requisito: meta 9.3.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 09**. Foco: de novo sem efeito duplo.


## O que é

Operação idempotente pode rodar outra vez e o resultado de negócio fica o mesmo. Chave: orderId mais o tipo do efeito (`stock-reserved`). Na segunda vez, você acha a chave e não decrementa de novo.

## Por que existe neste sistema

DLQ e replay sem idempotência duplicam pagamento ou estoque. Os dois temas andam juntos.

## O que você faz com a mão

1. Escolha a chave do espelho.
2. Escreva o teste: processar o mesmo evento duas vezes deixa o estoque igual ao de uma vez.
3. Implemente no lab, não só no papel.

## O que você deve ver

Teste descrito em uma frase com número.

## O que pode dar errado

Usar timestamp como chave. Toda reentrega vira outra chave.

## Onde ler a fonte oficial

https://stripe.com/blog/idempotency (o conceito de chave; ignore a API deles)

## Como saber que terminou

A chave não inclui hora.

## Perguntas para responder sozinho

- Replay da DLQ deve ser seguro por quê?

## Próximo arquivo

[lab-03-replay.md](lab-03-replay.md)
