# Meta 8.5 — mTLS entre serviços

Tempo previsto: **70 min**. Semana 8. Pré-requisito: meta 8.2.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 08**. Foco: identidade do processo.


## O que é

mTLS é TLS dos dois lados. O gateway prova que é o gateway e o orders prova que é o orders, com certificados. JWT continua provando o usuário. Um não substitui o outro.

## Por que existe neste sistema

O momento 3 já existe no oráculo: `docs/tutoriais/03-mtls-grpc.md` e `infra/docker-compose.mtls.yml`. Você executa e quebra de propósito.

## O que você faz com a mão

1. Leia o tutorial 03 inteiro antes de subir o overlay.
2. Anote a diferença da tabela JWT versus certificado.
3. Não apague a pasta `infra/certs`.

## O que você deve ver

Você explica as duas identidades com um exemplo cada.

## O que pode dar errado

Desligar JWT porque 'agora tem mTLS' e deixar a API aberta para qualquer usuário na rede.

## Onde ler a fonte oficial

docs/tutoriais/03-mtls-grpc.md

## Como saber que terminou

A frase das duas identidades está no relatório.

## Perguntas para responder sozinho

- Quem apresenta certificado: o browser ou o gateway?

## Próximo arquivo

[lab-03-quebrar-mtls.md](lab-03-quebrar-mtls.md)
