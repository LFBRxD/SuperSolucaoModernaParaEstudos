# Lab 11.3 — Orçamento e uma melhoria

Tempo previsto: **80 min**. Semana 11. Pré-requisito: lab 11.1.

## Onde você está

```mermaid
flowchart LR
  S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9 --> S10 --> S11 --> S12
```

Leia da esquerda para a direita. Esta sessão está na **semana 11**. Foco: evoluir com número.


## Figura desta sessão

```mermaid
flowchart LR
  Medir[baseline] --> Orc[orcamento escrito]
  Orc --> Mudar[uma mudanca pequena]
  Mudar --> Medir2[medir de novo]
```

Leia a figura antes do texto. O texto só nomeia o que a figura já mostrou.

## Objetivo

Mudar uma coisa e mostrar o número antes e depois, ou mostrar que a mudança não era sobre latência.

## 1. Implementar

1. Escolha uma melhoria pequena no espelho: índice, timeout explícito, ou menos log síncrono.
2. Se não houver o que melhorar com segurança, escreva o orçamento e não invente microotimização.
3. Rode de novo o teste funcional. A melhoria não pode quebrar CONFIRMED.

## 2. Ver manualmente

1. Tabela: métrica, antes, depois.
2. Se você não mediu de novo, a melhoria não entra como feita.

## 3. Validar o fluxo integrado

1. O smoke do oráculo continua verde. Sua mudança foi no espelho, a menos que você tenha corrigido um bug real do oráculo com teste.

## 4. Automatizar

1. k6 ou o cronômetro do polling. Uma métrica, não cinco.

## 5. Evoluir

1. Não tune o Kafka do oráculo no escuro.

## Comandos — Windows (PowerShell)

```powershell
# k6 ou smoke com horario
```

## Comandos — Linux / WSL

```bash
# k6 ou smoke
```

## Erros comuns

- Mudar timeout do teste para o número caber.
- Otimizar sem o teste de regressão.

## Pistas (leia só se travar)

- Orçamento de lab sugerido para discutir, não como verdade universal: p95 do POST abaixo de 2s na sua máquina, estado final em 60s.

A solução comentada não fica neste arquivo. Se precisar de gabarito, olhe o comportamento do oráculo (este repositório) e a fonte oficial. Não copie um serviço inteiro.

## Perguntas

- O que você recusou otimizar e por quê?

## Entregável

Tabela antes/depois ou orçamento com recusa justificada.

## Rubrica

Aprovado se a regressão funcional passou depois da mudança.

## Próximo arquivo

[leitura-01-carga.md](leitura-01-carga.md)
