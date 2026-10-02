# Meta 4.3 — Por que existe gateway

Tempo previsto: **60 min**. Semana 4. Pré-requisito: meta 4.2.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 04**. Foco: uma porta HTTP para o QA.


## O que é

O gateway é a única porta HTTP de negócio para a tela e para o Bruno. Ele autentica, junta dados e traduz erros. Os serviços de orders e inventory não precisam conhecer o browser.

## Por que existe neste sistema

Teste de UI sempre passa por ele. Teste do proto pode passar direto no gRPC, mas isso é outro contrato. Não misture as falhas.

## O que você faz com a mão

1. Liste as rotas em `docs/seguranca.md`.
2. Marque quais o gateway atende sozinho (login, health) e quais ele repassa.
3. Notificações são HTTP por trás, não gRPC. Anote essa exceção.

## O que você deve ver

Tabela rota → destino (gRPC orders, gRPC inventory, HTTP notifications, local).

## O que pode dar errado

Chamar orders na porta 11002 e achar que é a API do produto. 11002 é actuator/HTTP interno, não o contrato do Bruno.

## Onde ler a fonte oficial

https://grpc.io/docs/guides/

## Como saber que terminou

Você explica por que o Bruno aponta para 11001 e não para 11003.

## Perguntas para responder sozinho

- O que quebra se o gateway cai e os outros serviços continuam de pé?

## Próximo arquivo

[lab-02-separar-servicos.md](lab-02-separar-servicos.md)
