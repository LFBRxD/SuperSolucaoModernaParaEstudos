# Meta 2.3 — Controller, serviço e repositório

Tempo previsto: **75 min**. Semana 2. Pré-requisito: meta 2.2.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 02**. Foco: caminho dentro do processo.


## O que é

Controller recebe HTTP e devolve HTTP. Serviço aplica regra. Repositório fala com o banco. Nesta semana o repositório pode ser uma lista em memória. O banco entra na semana 3.

## Por que existe neste sistema

Se tudo fica no controller, o teste vira um teste de HTTP para uma regra que deveria ser uma função. Separar agora evita reescrever depois.

## O que você faz com a mão

1. No oráculo, abra `ApiController.java` e veja que ele chama clientes gRPC, não o Mongo direto.
2. No seu projeto espelho, planeje três classes: `ProductController`, `ProductService`, `ProductRepository` em memória.
3. Escreva no papel os campos de um produto: id, nome, preço, quantidade.

## O que você deve ver

Um desenho de três caixas com uma seta HTTP só na primeira.

## O que pode dar errado

Colocar regra de estoque dentro do controller 'porque é pequeno'. O lab pede a separação mesmo assim.

## Onde ler a fonte oficial

https://spring.io/guides/gs/rest-service

## Como saber que terminou

Você descreve quem pode conhecer HTTP e quem não pode.

## Perguntas para responder sozinho

- O controller deve saber o formato do Mongo?
- Não nesta semana. Por quê?

## Próximo arquivo

[lab-01-criar-o-projeto.md](lab-01-criar-o-projeto.md)
