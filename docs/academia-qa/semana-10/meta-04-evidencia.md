# Meta 10.4 — Evidência quando falha

Tempo previsto: **50 min**. Semana 10. Pré-requisito: meta 10.3.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 10**. Foco: o relatório que você consegue ler depois.


## O que é

Teste verde não precisa de print. Teste vermelho precisa de status, corpo, orderId e, na UI, trace do Playwright. Sem isso você repete o clique amanhã sem lembrar.

## Por que existe neste sistema

O CI guarda log do Compose e o relatório do Playwright. Localmente você usa os templates em `docs/academia-qa/evidencias/templates/`.

## O que você faz com a mão

1. Abra o template de bug.
2. Preencha um bug didático: estoque que não volta após pagamento falho, marcado como limitação conhecida, não como defeito surpresa.
3. Ou preencha um defeito real se você achou um.

## O que você deve ver

Um template preenchido.

## O que pode dar errado

Print sem URL, sem horário e sem usuário (`qa` ou `admin`).

## Onde ler a fonte oficial

docs/academia-qa/evidencias/templates/bug-report.md

## Como saber que terminou

Outra pessoa entende o bug sem perguntar para você.

## Perguntas para responder sozinho

- O que não entra no relatório? (token, senha)

## Próximo arquivo

[leitura-01-automacao.md](leitura-01-automacao.md)
