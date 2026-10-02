# Meta 12.2 — Imagem e configuração

Tempo previsto: **55 min**. Semana 12. Pré-requisito: semana 1.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 12**. Foco: o processo que o CI sobe.


## O que é

A imagem é o jar mais o sistema de arquivos mínimo. Configuração (porta, URL do Kafka) entra por variável, não por recompilar. O que você muda no YAML do espelho tem que existir no Compose, senão funciona na IDE e quebra no container.

## Por que existe neste sistema

O oráculo já tem Dockerfile por serviço. Leia um. Não reescreva todos.

## O que você faz com a mão

1. Abra `apps/orders-service/Dockerfile`.
2. Veja a variável `KAFKA_BOOTSTRAP_SERVERS` no Compose.
3. Escreva o par: nome da env e onde o Java lê.

## O que você deve ver

Um par env → propriedade.

## O que pode dar errado

Senha só dentro da imagem. Ela fica no histórico. No lab já é didático; não acrescente outra.

## Onde ler a fonte oficial

https://docs.docker.com/get-started/docker-concepts/building-images/writing-a-dockerfile/

## Como saber que terminou

Você explica por que o jar sozinho no Windows não vê o hostname `kafka`.

## Perguntas para responder sozinho

- O que é publish de porta versus porta interna?

## Próximo arquivo

[meta-03-helm.md](meta-03-helm.md)
