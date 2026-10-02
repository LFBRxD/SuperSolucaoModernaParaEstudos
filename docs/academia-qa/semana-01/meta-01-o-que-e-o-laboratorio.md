# Meta 1.1 — O que é este laboratório

Tempo previsto: **60 min**. Semana 1. Pré-requisito: nenhum.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 01**. Foco: conhecer o sistema antes de operar.


## O que é

O StudyShop é um e-commerce de estudo. Não é uma loja real. Ele existe para você ver, quebrar e reconstruir as peças que um QA encontra em sistemas distribuídos: site, API, banco, mensagens, segurança e telas de diagnóstico.

## Por que existe neste sistema

Você vai usar a solução pronta como prova dos nove. O projeto que você criar do zero (pasta irmã `studyshop-do-zero`) tem que chegar a um comportamento parecido. Se você só clicar na tela pronta, não aprende a construir.

## O que você faz com a mão

1. Abra o README na raiz do repositório e anote as portas que começam em 11000.
2. Abra `docs/arquitetura.md` e copie, com suas palavras, a lista de serviços.
3. Abra `docs/glossario.md` e marque três palavras que você ainda não sabe explicar.

## O que você deve ver

Uma lista sua com: nome do serviço, porta, e uma frase do que ele faz. Sem copiar a tabela inteira do README.

## O que pode dar errado

Achar que precisa entender Kafka hoje. Nesta semana Kafka só existe no mapa. Você ainda não precisa consumir mensagem.

## Onde ler a fonte oficial

README do repositório e https://docs.docker.com/get-started/overview/ (só a ideia de container).

## Como saber que terminou

Você consegue apontar, sem abrir o README, quem fala HTTP com o browser e quem guarda o catálogo.

## Perguntas para responder sozinho

- Qual serviço o browser chama primeiro?
- O que é o oráculo neste curso?
- Onde ficará o seu projeto do zero?

## Próximo arquivo

[lab-01-subir-a-stack.md](lab-01-subir-a-stack.md)
