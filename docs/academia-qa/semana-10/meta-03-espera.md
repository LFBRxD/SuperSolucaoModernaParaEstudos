# Meta 10.3 — Esperar estado final sem sleep cego

Tempo previsto: **60 min**. Semana 10. Pré-requisito: meta 6.2.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 10**. Foco: polling com teto.


## O que é

Espere até o status ser final ou até o relógio estourar. Intervalo fixo curto, timeout explícito, mensagem com o último status visto. `Thread.sleep(60000)` sempre, mesmo quando confirmou em 2 segundos, só deixa a suíte lenta.

## Por que existe neste sistema

Playwright tem `expect.poll` ou repetir o GET. O smoke do repo faz loop. Copie a ideia, não um número mágico sem mensagem.

## O que você faz com a mão

1. Leia a função de espera em `scripts/smoke.sh`.
2. Anote timeout e intervalo.
3. Escreva a mensagem de falha que você gostaria de ler.

## O que você deve ver

Timeout, intervalo e exemplo de mensagem.

## O que pode dar errado

Aumentar timeout para 10 minutos para 'não flake' e esconder serviço parado.

## Onde ler a fonte oficial

https://playwright.dev/docs/test-assertions#expectpoll

## Como saber que terminou

Sua mensagem de falha inclui o último status.

## Perguntas para responder sozinho

- CONFIRMED e CANCELLED são os únicos finais. O que você faz com AWAITING_* no fim do tempo?

## Próximo arquivo

[lab-03-playwright-pedido.md](lab-03-playwright-pedido.md)
