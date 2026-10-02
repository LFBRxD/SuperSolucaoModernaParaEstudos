# Meta 11.3 — Olhar sem explorar ataque

Tempo previsto: **50 min**. Semana 11. Pré-requisito: semana 8.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 11**. Foco: baseline de configuração.


## O que é

Baseline passivo é conferir o que já está documentado como risco: porta 11007 sem auth, CORS largo, Kafka sem TLS, segredo de lab no compose. Você não varre a internet e não escreve exploit.

## Por que existe neste sistema

O checklist `docs/academia-qa/desafios/seguranca-passiva.md` lista o que marcar. Corrigir no espelho é evolução. No oráculo, você registra.

## O que você faz com a mão

1. Percorra o checklist e marque achado ou não achado, com o arquivo.
2. Não rode scanner contra host que não seja localhost.
3. Não cole o JWT secret em print público fora do repo de estudo.

## O que você deve ver

Checklist marcado.

## O que pode dar errado

Tratar o checklist como pentest e tentar invadir outro sistema.

## Onde ler a fonte oficial

docs/academia-qa/desafios/seguranca-passiva.md

## Como saber que terminou

Cada item tem evidência local.

## Perguntas para responder sozinho

- Qual risco você corrigiria primeiro no espelho?

## Próximo arquivo

[meta-04-falha-controlada.md](meta-04-falha-controlada.md)
