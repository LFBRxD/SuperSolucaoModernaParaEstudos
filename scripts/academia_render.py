# -*- coding: utf-8 -*-
"""Renderiza a academia QA em um arquivo por meta, lab, leitura ou diagrama."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "docs" / "academia-qa"


def you_are_here(week: int, focus: str) -> str:
    nodes = []
    for n in range(1, 13):
        label = f"S{n:02d}"
        nodes.append(f"S{n}[\"{label}\"]")
    chain = " --> ".join(f"S{n}" for n in range(1, 13))
    return f"""```mermaid
flowchart LR
  {chain}
```

Leia da esquerda para a direita. Esta sessão está na **semana {week:02d}**. Foco: {focus}.
"""


def write(rel: str, text: str) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")
    print(rel)


def meta(week, slug, title, minutes, prereq, focus, what, why, hands, see, wrong, source, done, questions, nxt):
    steps = "\n".join(f"{i}. {s}" for i, s in enumerate(hands, 1))
    qs = "\n".join(f"- {q}" for q in questions)
    write(
        f"semana-{week:02d}/{slug}.md",
        f"""# {title}

Tempo previsto: **{minutes} min**. Semana {week}. Pré-requisito: {prereq}.

## Onde você está

{you_are_here(week, focus)}

## O que é

{what}

## Por que existe neste sistema

{why}

## O que você faz com a mão

{steps}

## O que você deve ver

{see}

## O que pode dar errado

{wrong}

## Onde ler a fonte oficial

{source}

## Como saber que terminou

{done}

## Perguntas para responder sozinho

{qs}

## Próximo arquivo

{nxt}
""",
    )


def lab(week, slug, title, minutes, prereq, focus, diagram, goal, implement, manual, integrated, automate, evolve, commands_win, commands_linux, pitfalls, hints, questions, deliver, rubric, nxt):
    def bullets(items, numbered=False):
        if numbered:
            return "\n".join(f"{i}. {s}" for i, s in enumerate(items, 1))
        return "\n".join(f"- {s}" for s in items)

    qs = "\n".join(f"- {q}" for q in questions)
    write(
        f"semana-{week:02d}/{slug}.md",
        f"""# {title}

Tempo previsto: **{minutes} min**. Semana {week}. Pré-requisito: {prereq}.

## Onde você está

{you_are_here(week, focus)}

## Figura desta sessão

{diagram}

Leia a figura antes do texto. O texto só nomeia o que a figura já mostrou.

## Objetivo

{goal}

## 1. Implementar

{bullets(implement, True)}

## 2. Ver manualmente

{bullets(manual, True)}

## 3. Validar o fluxo integrado

{bullets(integrated, True)}

## 4. Automatizar

{bullets(automate, True)}

## 5. Evoluir

{bullets(evolve, True)}

## Comandos — Windows (PowerShell)

```powershell
{commands_win.strip()}
```

## Comandos — Linux / WSL

```bash
{commands_linux.strip()}
```

## Erros comuns

{bullets(pitfalls)}

## Pistas (leia só se travar)

{bullets(hints)}

A solução comentada não fica neste arquivo. Se precisar de gabarito, olhe o comportamento do oráculo (este repositório) e a fonte oficial. Não copie um serviço inteiro.

## Perguntas

{qs}

## Entregável

{deliver}

## Rubrica

{rubric}

## Próximo arquivo

{nxt}
""",
    )


def leitura(week, slug, title, minutes, focus, why, sections, sources, questions, nxt):
    body = "\n\n".join(f"### {t}\n\n{p}" for t, p in sections)
    qs = "\n".join(f"- {q}" for q in questions)
    src = "\n".join(f"- {s}" for s in sources)
    write(
        f"semana-{week:02d}/{slug}.md",
        f"""# {title}

Tempo de leitura: **{minutes} min**. Não substitua o lab. Leia, feche, e só então faça o lab.

## Onde você está

{you_are_here(week, focus)}

## Por que esta leitura agora

{why}

{body}

## Fontes

{src}

## Perguntas de revisão

{qs}

## Próximo arquivo

{nxt}
""",
    )


def diagrama(week, slug, title, caption, mermaid, read_how, nxt):
    write(
        f"semana-{week:02d}/{slug}.md",
        f"""# {title}

## Onde você está

{you_are_here(week, caption)}

## Figura

{mermaid}

{read_how}

## O que observar

Compare os nomes desta figura com os nomes reais do código e do Compose (`api-gateway`, `orders.events`, portas 11000+). Se um nome divergir, anote: ou o diagrama está velho, ou você está olhando outro ambiente.

## Exercício

Redesenhe esta figura sem olhar, em papel ou Mermaid. Depois abra de novo e marque o que esqueceu.

## Próximo arquivo

{nxt}
""",
    )
