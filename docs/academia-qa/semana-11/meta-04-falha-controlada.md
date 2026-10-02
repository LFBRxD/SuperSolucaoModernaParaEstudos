# Meta 11.4 — Latência e processo parado

Tempo previsto: **55 min**. Semana 11. Pré-requisito: meta 11.1.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 11**. Foco: o sistema avisa em vez de pendurar.


## O que é

Parar um container ou atrasar uma resposta mostra se o gateway estoura deadline ou se a thread fica presa. Você já fez isso com inventory na semana 4. Agora você mede o tempo até o erro.

## Por que existe neste sistema

Não use ferramenta de flood. Um `docker compose stop` e um cronômetro bastam.

## O que você faz com a mão

1. Pare payments, crie um pedido, meça até o timeout do seu polling.
2. Suba payments de novo.
3. Anote se o pedido ficou preso. Esse é o caso do job da semana 7.

## O que você deve ver

Tempo até o teste desistir, e o status em que o pedido ficou.

## O que pode dar errado

Deixar o serviço parado e encerrar o dia.

## Onde ler a fonte oficial

docs/academia-qa/ferramentas/docker.md

## Como saber que terminou

Você religou o serviço e o health voltou a UP.

## Perguntas para responder sozinho

- O job de expiração ajudaria neste caso?

## Próximo arquivo

[lab-03-orcamento.md](lab-03-orcamento.md)
