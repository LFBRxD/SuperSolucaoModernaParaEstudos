# Meta 12.3 — Helm e pod

Tempo previsto: **60 min**. Semana 12. Pré-requisito: meta 12.2.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 12**. Foco: o mesmo sistema no Kubernetes de estudo.


## O que é

Helm instala vários manifests de uma vez. Pod é o processo no cluster. Service é o nome estável. O README `infra/helm/study-shop/README.md` manda o install e o port-forward. Observabilidade completa não está no chart: o README diz isso. Não procure Jaeger no cluster e conclua que o pedido não gera trace.

## Por que existe neste sistema

CronJob é o agendamento da plataforma, diferente do Quartz dentro do Java.

## O que você faz com a mão

1. Leia o README do chart até o install.
2. Leia `docs/academia-qa/semana-12/diagrama-02-cronjob.md`.
3. Se você não tiver kind, não finja que instalou. Siga o lab de leitura e marque o limite.

## O que você deve ver

Você sabe o que o chart inclui e o que ele não inclui (Jaeger).

## O que pode dar errado

Achar que `kubectl port-forward` publica para a internet. Ele abre só na sua máquina.

## Onde ler a fonte oficial

https://helm.sh/docs/intro/using_helm/

## Como saber que terminou

Uma frase: por que o trace some no kind deste chart.

## Perguntas para responder sozinho

- Qual a diferença entre CronJob e o Quartz da semana 7?

## Próximo arquivo

[lab-02-cronjob.md](lab-02-cronjob.md)
