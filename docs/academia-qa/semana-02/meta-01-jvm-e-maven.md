# Meta 2.1 — JVM e Maven

Tempo previsto: **70 min**. Semana 2. Pré-requisito: semana 1 concluída.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 02**. Foco: como um projeto Java nasce.


## O que é

A JVM executa bytecode Java. O Maven compila, baixa bibliotecas e empacota um jar. O arquivo `pom.xml` é a lista de ingredientes. `mvn package` produz o jar. Sem isso, não existe serviço Spring.

## Por que existe neste sistema

Na semana 2 você cria o projeto espelho do zero. O oráculo já tem um `pom.xml` na raiz. O seu projeto começa menor: um único módulo.

## O que você faz com a mão

1. Na raiz do oráculo, abra `pom.xml` e leia `java.version` e a lista de `<module>`.
2. Rode `java -version` e `mvn -version` no terminal. Se faltar, instale JDK 21 e Maven antes de continuar.
3. Não rode o build completo ainda se a stack Docker já está no ar; só confirme as versões.

## O que você deve ver

Java 21 e Maven reconhecidos pelo terminal.

## O que pode dar errado

Ter só o JRE e não o JDK: compila nada. `javac` precisa existir.

## Onde ler a fonte oficial

https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html

## Como saber que terminou

Você diz, com suas palavras, o que o `pom.xml` declara.

## Perguntas para responder sozinho

- O que é um módulo Maven neste repo?
- Por que o projeto do zero começa com um módulo só?

## Próximo arquivo

[meta-02-spring-boot.md](meta-02-spring-boot.md)
