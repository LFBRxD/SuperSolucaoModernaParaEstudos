# -*- coding: utf-8 -*-
from academia_render import write, you_are_here

WEEKS = [
    (1, "Mapa e operação", "8–10 h", "Fundamentos"),
    (2, "Primeiro Spring do zero", "8–10 h", "Fundamentos"),
    (3, "MongoDB e massa de teste", "8–10 h", "Dados e contratos"),
    (4, "Protobuf, gRPC e gateway", "8–10 h", "Dados e contratos"),
    (5, "Kafka por dentro", "8–10 h", "Eventos"),
    (6, "Saga e consistência eventual", "8–10 h", "Eventos"),
    (7, "Notificação, webhook e Quartz", "8–10 h", "Eventos"),
    (8, "JWT, OIDC e mTLS", "8–10 h", "Segurança"),
    (9, "Observabilidade, DLQ e idempotência", "8–10 h", "Diagnóstico"),
    (10, "Smoke, Bruno e Playwright", "8–10 h", "Automação"),
    (11, "Carga, acessibilidade e falha controlada", "8–10 h", "Não funcional"),
    (12, "CI, Helm, CronJob e capstone", "8–10 h", "Plataforma"),
]


def build():
    lines = []
    for n, title, hours, level in WEEKS:
        lines.append(f"| {n} | {level} | {title} | {hours} | [semana-{n:02d}/README.md](semana-{n:02d}/README.md) |")
    table = "\n".join(lines)
    write("README.md", f"""# Academia QA — StudyShop

Este arquivo só aponta. O estudo está nos arquivos de cada semana.

Formação de **12 semanas**, **8 a 10 horas por semana**. Você estuda sozinho. Cada sessão tem o próprio markdown. Figura antes do texto.

## Como usar

1. [como-estudar.md](como-estudar.md)
2. [ciclo-das-cinco-etapas.md](ciclo-das-cinco-etapas.md)
3. Semana 1, de cima para baixo, no README da semana.
4. O projeto pronto deste repositório é o **oráculo**. O seu código nasce em `../studyshop-do-zero`.

## Agenda

| Semana | Nível | Tema | Carga | Entrada |
|--------|-------|------|-------|---------|
{table}

## Recuperação

Se atrasar uma semana, não comprima duas semanas num domingo. Siga [recuperacao.md](recuperacao.md).

## Mapas

- [diagramas/README.md](diagramas/README.md)
- [matriz-rastreabilidade.md](matriz-rastreabilidade.md)
- [riscos-conhecidos.md](riscos-conhecidos.md)
- [ferramentas/README.md](ferramentas/README.md)
- [checkpoints/README.md](checkpoints/README.md)
- [desafios/README.md](desafios/README.md)
- [evidencias/README.md](evidencias/README.md)
- [alem/plataforma-de-streaming.md](alem/plataforma-de-streaming.md)

## Onde você está no curso

{you_are_here(1, "comece pela semana 1")}
""")

    write("como-estudar.md", """# Como estudar

Você não é lento por precisar de muitos arquivos. Arquivo curto é uma sessão. Arquivo gigante vira resumo que não dá para executar.

## Ritmo

- 8 a 10 horas por semana.
- Sessões de 60 a 90 minutos.
- Pare no fim do arquivo. Não "adianta" a próxima semana no mesmo dia em que a anterior ficou torta.

## Ordem dentro da semana

O README da semana numera os arquivos. Siga o número. Meta explica. Lab executa. Leitura fixa o nome. Diagrama você redesenha.

## Oráculo e espelho

| | Oráculo (este repo) | Espelho (`../studyshop-do-zero`) |
|--|---------------------|----------------------------------|
| Função | Ver o comportamento pronto | Construir do zero |
| Portas | 11000 em diante | 11101, 11105, 11108, 11109 |
| Você edita a saga? | Não, salvo bug que você documentar | Sim |

## O que fazer quando travar

1. Leia de novo a figura do lab.
2. Leia as pistas no fim do lab.
3. Olhe a fonte oficial linkada.
4. Olhe o oráculo só para ver o comportamento, não para colar a classe inteira.
5. Escreva o que você tentou no relatório. Isso conta como estudo.

## O que não fazer

- Copiar o repositório para a pasta espelho.
- Aumentar timeout até o teste ficar verde sem ler o último status.
- Rodar carga ou scanner fora de localhost.
""")

    write("ciclo-das-cinco-etapas.md", """# Ciclo das cinco etapas

Nenhum lab termina quando o código compila.

```mermaid
flowchart LR
  I[1 Implementar] --> M[2 Ver com a mao]
  M --> G[3 Fluxo integrado]
  G --> A[4 Automatizar]
  A --> E[5 Evoluir]
```

Leia da esquerda para a direita.

1. **Implementar.** Arquivo novo no espelho, ou operação consciente no oráculo quando o lab diz para não codar.
2. **Ver com a mão.** Browser, curl, Bruno, Kafka UI, mongosh, log, Jaeger.
3. **Fluxo integrado.** O mesmo `orderId` em pelo menos dois lugares.
4. **Automatizar.** Um comando que falha com mensagem útil.
5. **Evoluir.** Segurança, espera, medida ou dívida escrita. Não é "refatorar por gosto".

Se a etapa 2 não aconteceu, a etapa 4 não vale.
""")

    write("recuperacao.md", """# Se você atrasar

- Uma semana atrasada: faça só as metas e o primeiro lab da semana atrasada, depois siga. Marque o lab pulado como dívida no portfolio.
- Duas semanas: pare o avanço. Semana parada não se recupera com resumo.
- Não junte a semana 7 (Quartz) com a 10 (Playwright). Uma depende da outra na sua cabeça, não no mesmo dia.

O capstone aceita checkpoint parcial se a lista for honesta. Não aceita lista vazia com "entendi tudo".
""")

    write("riscos-conhecidos.md", """# Riscos conhecidos do oráculo

Isto não é lista de desculpa. É o que o sistema faz hoje, para você não abrir bug fantasma.

| Risco | O que você observa | Onde |
|-------|--------------------|------|
| Estoque não volta se o pagamento falha | `prod-mouse` diminui e o pedido fica `CANCELLED` | cenário 4 |
| Sem scheduler | Pedido pode ficar em `AWAITING_*` para sempre | semana 7 |
| Sem DLQ | Erro no listener vai para o log e a mensagem pode ser commitada | semana 9 |
| Sem idempotência garantida | Reprocessar pode repetir efeito | semana 5 e 9 |
| Notificações sem auth na porta 11007 | GET direto no serviço não pede token | semana 7 |
| CORS largo | Origem `*` no gateway | `CorsConfig` |
| Kafka e Mongo sem TLS | Tráfego do lab é texto | `docs/seguranca.md` |
| Helm sem Jaeger | `OTEL_*` aponta para collector que o chart não cria | README do Helm |
| Smoke antigo só olhava o POST | O smoke atual espera estado final | `scripts/smoke.ps1` |
| UI não lista notificação | Só API e Mongo | semana 7 |
| Segredos de lab | Senhas `qa123`, JWT de exemplo | não usar fora daqui |

No espelho, compensação de estoque, job de expiração, DLQ e idempotência são trabalho seu.
""")

    # week readmes
    files = {
        1: ["meta-01-o-que-e-o-laboratorio.md", "meta-02-processo-porta-e-http.md", "meta-03-container-e-compose.md", "diagrama-01-stack-e-portas.md", "lab-01-subir-a-stack.md", "meta-04-health-agregado.md", "diagrama-02-health.md", "lab-02-health-web-e-api.md", "meta-05-devtools.md", "lab-03-devtools.md", "lab-04-desenhar-o-caminho.md", "leitura-01-http-e-compose.md"],
        2: ["meta-01-jvm-e-maven.md", "meta-02-spring-boot.md", "diagrama-01-ciclo-maven.md", "meta-03-controller.md", "meta-04-erro-http.md", "lab-01-criar-o-projeto.md", "lab-02-endpoint-catalogo.md", "meta-05-teste-junit.md", "lab-03-ver-no-swagger.md", "diagrama-02-antes-depois.md", "leitura-01-spring.md"],
        3: ["meta-01-documento-mongodb.md", "diagrama-01-documento.md", "lab-01-mongosh.md", "meta-02-seed-e-estado.md", "meta-03-equivalencia.md", "meta-04-isolamento.md", "diagrama-02-isolamento.md", "lab-02-persistir-no-espello.md", "lab-03-teste-com-mongo.md", "leitura-01-mongodb.md"],
        4: ["meta-01-protobuf.md", "meta-02-grpc.md", "diagrama-01-rest-grpc.md", "lab-01-ler-o-proto.md", "meta-03-gateway.md", "meta-04-mapeamento-de-erro.md", "diagrama-02-erros.md", "lab-02-separar-servicos.md", "lab-03-contrato.md", "leitura-01-grpc.md"],
        5: ["meta-01-broker.md", "diagrama-01-topico.md", "lab-01-kafka-ui.md", "meta-02-particao-offset.md", "meta-03-consumer-group.md", "diagrama-02-groups.md", "lab-02-console-consumer.md", "meta-04-pelo-menos-uma-vez.md", "lab-03-evento-no-espelho.md", "leitura-01-kafka.md"],
        6: ["meta-01-estados.md", "meta-02-eventual.md", "diagrama-01-feliz.md", "lab-01-feliz.md", "meta-03-pagamento-falho.md", "diagrama-02-falhas.md", "lab-02-falhas.md", "meta-04-correlacao.md", "lab-03-redesenhar.md", "leitura-01-saga.md"],
        7: ["meta-01-notificacao.md", "lab-01-ver-notificacao.md", "meta-02-webhook.md", "meta-03-scheduled.md", "meta-04-quartz.md", "diagrama-01-tres-caminhos.md", "diagrama-02-quartz.md", "meta-05-outbox.md", "lab-02-job-timeout.md", "lab-03-idempotencia-do-job.md", "leitura-01-jobs.md"],
        8: ["meta-01-401-403.md", "diagrama-02-matriz.md", "lab-01-matriz.md", "meta-02-jwt.md", "meta-03-oidc.md", "lab-02-keycloak.md", "meta-04-cors.md", "meta-05-mtls.md", "diagrama-01-jwt-oidc-mtls.md", "lab-03-quebrar-mtls.md", "leitura-01-identidade.md"],
        9: ["meta-01-tres-sinais.md", "diagrama-01-sinais.md", "lab-01-jaeger.md", "meta-02-sli.md", "meta-03-dlq.md", "diagrama-02-dlq.md", "lab-02-dlq.md", "meta-04-idempotencia.md", "lab-03-replay.md", "leitura-01-obs.md"],
        10: ["meta-01-piramide.md", "diagrama-01-piramide.md", "meta-02-bruno-cli.md", "meta-03-espera.md", "diagrama-02-espera.md", "lab-01-smoke-full.md", "lab-02-playwright-login.md", "lab-03-playwright-pedido.md", "meta-04-evidencia.md", "leitura-01-automacao.md"],
        11: ["meta-01-percentil.md", "diagrama-01-carga.md", "lab-01-k6.md", "meta-02-acessibilidade.md", "meta-03-seguranca-passiva.md", "lab-02-seguranca-passiva.md", "meta-04-falha-controlada.md", "diagrama-02-job-lento.md", "lab-03-orcamento.md", "leitura-01-carga.md"],
        12: ["meta-01-pipeline.md", "diagrama-01-ci.md", "lab-01-ler-pipeline.md", "meta-02-imagem.md", "meta-03-helm.md", "diagrama-02-cronjob.md", "lab-02-cronjob.md", "meta-04-capstone.md", "lab-03-apresentar.md", "leitura-01-plataforma.md"],
    }
    for n, title, hours, level in WEEKS:
        items = "\n".join(f"{i}. [{name}]({name}) — cerca de 60–90 min" for i, name in enumerate(files[n], 1))
        nxt = f"Semana {n+1}." if n < 12 else "Capstone e portfolio."
        write(f"semana-{n:02d}/README.md", f"""# Semana {n} — {title}

Nível: {level}. Carga: {hours}. Não pule arquivo.

## Onde você está

{you_are_here(n, title)}

## Ordem

{items}

## Saída da semana

Você consegue explicar o foco acima com um exemplo que você mesmo executou, e apontar o próximo arquivo.

## Próximo

{nxt}
""")

    write("matriz-rastreabilidade.md", """# Matriz de rastreabilidade

| Cenário | Manual | Bruno | Smoke | Playwright |
|---------|--------|-------|-------|------------|
| Health UP | semana 1 lab 1.2 | health.bru | sim | não é o foco |
| Login e 401 | semana 8 lab 8.1 | login.bru, auth-401-products.bru | sim | login-rbac.spec.ts |
| Catálogo | semana 1 e 6 | list-products.bru | sim | pedido-feliz.spec.ts |
| Pedido CONFIRMED | semana 6 lab 6.1 | poll-order.bru | sim | pedido-feliz.spec.ts |
| Pagamento falho | semana 6 lab 6.2 | create-order-payment-fail.bru | sim | pedido-pagamento-falho.spec.ts |
| Estoque insuficiente | semana 6 lab 6.2 | create-order-stock-fail.bru | sim | pedido-estoque.spec.ts |
| Admin stock 403/200 | semana 8 | update-stock.bru, login-admin.bru | sim | admin-stock.spec.ts |
| Notificação | semana 7 lab 7.1 | notifications-by-order.bru | sim | não há tela |
| mTLS | semana 8 lab 8.3 | não | não | não |
| Job Quartz | semana 7 lab 7.2 | não (é no espelho) | não | não |
| DLQ | semana 9 | não (é no espelho) | não | não |
| k6 | semana 11 | não | não | não |

CI: `.github/workflows/qa-lab.yml` roda smoke e Playwright no oráculo. Validadores do espelho rodam na sua máquina.
""")

    write("diagramas/README.md", """# Índice de diagramas

Figuras transversais:

- [ciclo.md](ciclo.md)
- [niveis.md](niveis.md)
- [ferramentas.md](ferramentas.md)

Figuras de cada semana ficam na pasta `semana-XX/diagrama-*.md` e também no topo de cada lab.

| Semana | Arquivos |
|--------|----------|
| 1 | diagrama-01-stack-e-portas, diagrama-02-health |
| 2 | diagrama-01-ciclo-maven, diagrama-02-antes-depois |
| 3 | diagrama-01-documento, diagrama-02-isolamento |
| 4 | diagrama-01-rest-grpc, diagrama-02-erros |
| 5 | diagrama-01-topico, diagrama-02-groups |
| 6 | diagrama-01-feliz, diagrama-02-falhas |
| 7 | diagrama-01-tres-caminhos, diagrama-02-quartz |
| 8 | diagrama-01-jwt-oidc-mtls, diagrama-02-matriz |
| 9 | diagrama-01-sinais, diagrama-02-dlq |
| 10 | diagrama-01-piramide, diagrama-02-espera |
| 11 | diagrama-01-carga, diagrama-02-job-lento |
| 12 | diagrama-01-ci, diagrama-02-cronjob |
""")

    write("diagramas/ciclo.md", """# Ciclo de estudo

```mermaid
flowchart LR
  I[Implementar] --> V[Ver com a mao]
  V --> F[Fluxo integrado]
  F --> A[Automatizar]
  A --> E[Evoluir]
```

Leia da esquerda para a direita. Detalhe em [../ciclo-das-cinco-etapas.md](../ciclo-das-cinco-etapas.md).
""")

    write("diagramas/niveis.md", """# Doze semanas

```mermaid
flowchart LR
  S1[S1 operar] --> S2[S2 Spring]
  S2 --> S3[S3 Mongo]
  S3 --> S4[S4 gRPC]
  S4 --> S5[S5 Kafka]
  S5 --> S6[S6 saga]
  S6 --> S7[S7 Quartz]
  S7 --> S8[S8 identidade]
  S8 --> S9[S9 traces e DLQ]
  S9 --> S10[S10 testes]
  S10 --> S11[S11 carga]
  S11 --> S12[S12 CI]
```

Leia da esquerda para a direita. Cada caixa é uma semana, não um resumo para pular as outras.
""")

    write("diagramas/ferramentas.md", """# O que cada ferramenta enxerga

```mermaid
flowchart TB
  Pedido[um pedido]
  Pedido --> Dev[DevTools]
  Pedido --> Bruno[Bruno]
  Pedido --> UI[Kafka UI]
  Pedido --> Mongo[mongosh]
  Pedido --> Log[docker logs]
  Pedido --> Jaeger[Jaeger]
  Pedido --> Prom[Prometheus]
```

Nenhuma caixa substitui as outras. A tabela está em [../ferramentas/README.md](../ferramentas/README.md).
""")

    tools = {
        "devtools.md": ("DevTools", "O HTTP que o browser fez e o localStorage.", "F12, Network, Preserve log, Fetch/XHR.", "http://localhost:11000", "https://developer.chrome.com/docs/devtools/network"),
        "swagger.md": ("Swagger", "Rotas HTTP do gateway.", "http://localhost:11001/swagger-ui.html e Authorize com Bearer.", "11001", "https://swagger.io/docs/specification/v3_0/about/"),
        "bruno.md": ("Bruno", "Requests repetíveis com assert.", "Abra a pasta bruno/study-shop. Rode login antes.", "coleção do repo", "https://docs.usebruno.com/"),
        "curl.md": ("curl", "HTTP sem browser.", "curl.exe -i no Windows. curl -s no bash. Sempre que a rota for protegida, mande Authorization.", "11001", "https://curl.se/docs/manpage.html"),
        "kafka-ui.md": ("Kafka UI", "Tópicos, mensagens, groups e lag.", "http://localhost:11016 depois do compose up.", "11016", "https://kafka.apache.org/documentation/#gettingStarted"),
        "kafka-cli.md": ("Kafka CLI", "O mesmo dado da UI no terminal.", """docker compose exec kafka /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --list

docker compose exec kafka /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic orders.events --from-beginning --group qa-lab-leitura

docker compose exec kafka /opt/kafka/bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --all-groups""", "dentro do container, localhost:9092", "https://kafka.apache.org/documentation/#basic_ops"),
        "mongosh.md": ("mongosh", "Documento gravado.", "docker compose exec mongodb mongosh inventory --eval 'show collections'", "11008 no host", "https://www.mongodb.com/docs/mongodb-shell/"),
        "docker.md": ("Docker", "Processo, log, porta.", "docker compose ps e docker compose logs --tail=80 SERVICO", "pasta infra", "https://docs.docker.com/compose/"),
        "keycloak.md": ("Keycloak", "Login do momento 2.", "http://localhost:11015 admin/admin, realm study-shop. Só com o overlay.", "11015", "docs/tutoriais/02-oidc-keycloak.md"),
        "openssl.md": ("OpenSSL", "Certificado do mTLS.", "openssl x509 -in infra/certs/orders.crt -noout -subject -ext subjectAltName", "infra/certs", "docs/tutoriais/03-mtls-grpc.md"),
        "jaeger.md": ("Jaeger", "Trace.", "http://localhost:11011", "11011", "docs/observabilidade.md"),
        "prometheus.md": ("Prometheus e Grafana", "Número ao longo do tempo.", "Prometheus http://localhost:11012 query up. Grafana http://localhost:11010 admin/admin.", "11012 e 11010", "docs/observabilidade.md"),
        "playwright.md": ("Playwright", "UI repetível e trace da falha.", "cd apps/web; npm run e2e", "11000", "https://playwright.dev/docs/trace-viewer"),
        "k6.md": ("k6", "Latência e erro sob carga local.", "k6 run tests/k6/pedido-baseline.js", "11001", "https://grafana.com/docs/k6/latest/"),
        "quartz.md": ("Quartz", "Job do espelho, não do oráculo.", "Log com jobName, fireTime, orderId. GET interno se você criou. Tabelas QRTZ_ se o JobStore for JDBC.", "espelho", "https://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/"),
    }
    trows = []
    for fname, (title, sees, how, where, src) in tools.items():
        trows.append(f"| [{title}]({fname}) | {sees} |")
        write(f"ferramentas/{fname}", f"""# {title}

## O que ela enxerga

{sees}

## Onde

{where}

## Como usar neste lab

{how}

## Fonte

{src}

## Não serve para

Substituir as outras ferramentas da [lista](README.md).
""")
    write("ferramentas/README.md", """# Ferramentas

| Ferramenta | Enxerga |
|------------|---------|
""" + "\n".join(trows) + "\n")

    checkpoints = [
        ("bootstrap", "Existem pom.xml e src/main/java no espelho. README cita a porta 11101."),
        ("catalog-api", "GET de produtos documentado. Teste ou README mostra 200 e 404."),
        ("orders-mongo", "URI do Mongo do espelho não é a porta 11008. Há coleção ou entidade de pedido."),
        ("grpc-gateway", "Há arquivo .proto e mais de um processo descrito no README."),
        ("kafka-events", "README ou código cita um tópico e eventType."),
        ("saga", "Estados CONFIRMED e CANCELLED aparecem no README do espelho ou no código."),
        ("scheduled-jobs", "Há Quartz ou dependência quartz e um @Scheduled. README explica a diferença. Há menção a idempotência do job."),
        ("web-auth", "401 e 403 documentados, ou filtro de segurança no código."),
        ("observability", "README diz onde está o log ou o trace."),
        ("automation-ci", "Há comando de teste no README (mvn test ou equivalente)."),
        ("platform", "Dockerfile ou compose do espelho, ou nota honesta de que ainda não há."),
    ]
    write("checkpoints/README.md", """# Checkpoints do espelho

O validador olha arquivos e o README. Ele não dá nota de estilo. `ACADEMY_PROJECT_DIR` aponta para a pasta do espelho.

| Id | O que prova, de forma grosseira |
|----|----------------------------------|
""" + "\n".join(f"| `{i}` | {d} |" for i, d in checkpoints) + """

```powershell
$env:ACADEMY_PROJECT_DIR = "E:\\projetos\\studyshop-do-zero"
.\\scripts\\academy\\validate-checkpoint.ps1 -Checkpoint all
```

```bash
export ACADEMY_PROJECT_DIR=../studyshop-do-zero
./scripts/academy/validate-checkpoint.sh all
```
""")
    for i, d in checkpoints:
        write(f"checkpoints/{i}.md", f"""# Checkpoint `{i}`

## Antes

O espelho não cumpre esta fatia.

## Depois

{d}

## Como verificar

`scripts/academy/validate-checkpoint.ps1 -Checkpoint {i}`

## Honesto

Se falhar, o capstone lista a dívida. Não apague o validador.
""")

    write("desafios/README.md", """# Desafios do espelho

O oráculo não entrega estas peças prontas (mTLS é a exceção: já existe no oráculo para você observar).

- [webhook.md](webhook.md)
- [quartz.md](quartz.md)
- [dlq.md](dlq.md)
- [mtls.md](mtls.md)
- [seguranca-passiva.md](seguranca-passiva.md)
- [resiliencia.md](resiliencia.md)
""")

    write("desafios/webhook.md", """# Desafio — webhook

## Estado atual do oráculo

Não há HTTP de saída. Notificação é documento + GET.

## Contrato mínimo do espelho

- POST para `http://127.0.0.1:11180/hooks/orders`
- Corpo JSON com `eventId`, `eventType`, `orderId`
- Header `X-Signature`: hex de HMAC-SHA256 do corpo cru, segredo no YAML de lab
- Timeout de 2 segundos
- No máximo 3 tentativas
- Receptor devolve 401 se a assinatura não bater
- O mesmo `eventId` não aplica efeito duas vezes

## Onde ler

Semana 7, meta 7.2 e lab 7.3. RFC de HMAC: https://datatracker.ietf.org/doc/html/rfc2104

## Validador

Procura as strings `X-Signature` e `11180` no projeto espelho (`checkpoint` não cobre sozinho; veja `scripts/academy/validate-challenge.ps1 -Name webhook`).
""")

    write("desafios/quartz.md", """# Desafio — Quartz

## Estado atual do oráculo

Não há scheduler. Pedido intermediário pode ficar parado.

## Contrato mínimo do espelho

- Um job Quartz que cancela pedido em espera depois de um prazo curto de lab
- Um `@Scheduled` diferente, documentado como mais fraco
- Log com `jobName`, `fireTime`, `orderId`
- Segunda execução não altera de novo um pedido já cancelado
- Intervalo de lab em segundos, com nota do valor que você usaria em produção

## Onde ler

https://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/tutorial-lesson-01.html

Semana 7.

## Validador

`validate-challenge.ps1 -Name quartz` procura dependência quartz e `@Scheduled`.
""")

    write("desafios/dlq.md", """# Desafio — DLQ e idempotência

## Estado atual do oráculo

Listener registra erro e não há fila morta.

## Contrato mínimo do espelho

- Após 3 falhas, a mensagem vai para tópico `lab.dlq` ou coleção `dead_letters`
- O registro tem orderId, erro e payload
- Replay é comando explícito
- Segunda aplicação do mesmo efeito não muda o estoque

## Onde ler

Semana 9. https://kafka.apache.org/documentation/#semantics

## Validador

`validate-challenge.ps1 -Name dlq` procura `dlq` ou `dead_letter` no espelho.
""")

    write("desafios/mtls.md", """# Desafio — mTLS

## Estado atual do oráculo

Já existe. Tutorial `docs/tutoriais/03-mtls-grpc.md`, overlay `infra/docker-compose.mtls.yml`, certs em `infra/certs`.

## O que você faz

Executa o tutorial, quebra a confiança, restaura. No espelho, mTLS é opcional no capstone. Não é desculpa para pular o lab 8.3 no oráculo.

## Validador

`validate-challenge.ps1 -Name mtls` confere os arquivos do oráculo, não do espelho.
""")

    write("desafios/seguranca-passiva.md", """# Checklist passivo (localhost)

Marque achado ou não, com arquivo. Não escaneie rede que não é sua.

- [ ] `GET` em `http://localhost:11007/api/notifications` sem token responde 200
- [ ] CORS do gateway permite origem ampla (`CorsConfig`)
- [ ] Kafka no Compose está `PLAINTEXT`
- [ ] Mongo no Compose não pede senha
- [ ] `docs/seguranca.md` diz que isso é lab
- [ ] UI esconder o menu não impede PUT (403 com token de qa)
- [ ] Segredo JWT do lab está no Compose e não deve ir para outro ambiente

Correção esperada no espelho: não copiar a porta aberta sem auth.
""")

    write("desafios/resiliencia.md", """# Desafio — resiliência

## O que observar no oráculo

Pare `payments-service`, crie um pedido, veja em que status ele fica, suba o serviço de novo.

## O que construir no espelho

- Deadline na chamada interna
- Job de expiração (desafio Quartz)
- Idempotência (desafio DLQ)

Não use ferramenta de ataque. `docker compose stop` no seu Compose basta.
""")

    write("evidencias/README.md", """# Evidências

Copie o template para um lugar seu (pasta fora do git, ou fork). Não encha o repositório de print.

- [checklist-conclusao.md](checklist-conclusao.md)
- [templates/relatorio-lab.md](templates/relatorio-lab.md)
- [templates/bug-report.md](templates/bug-report.md)
- [templates/evidencia-trace-jaeger.md](templates/evidencia-trace-jaeger.md)
- [templates/portfolio-aluno.md](templates/portfolio-aluno.md)
""")

    write("evidencias/checklist-conclusao.md", """# Checklist por nível

## Semanas 1–2

- [ ] Stack do oráculo sobe e health fica UP
- [ ] Desenho seu do caminho browser → gateway
- [ ] Espelho sobe na porta 11101 com GET de catálogo

## Semanas 3–4

- [ ] Documento visto no mongosh
- [ ] Espelho não usa a porta 11008
- [ ] Chamada passa por um segundo processo ou a dívida está escrita

## Semanas 5–7

- [ ] orderId visto na Kafka UI
- [ ] CONFIRMED, CANCELLED por pagamento e CANCELLED por estoque
- [ ] Job do espelho cancela pedido parado e a segunda vez não duplica
- [ ] Webhook local com assinatura, ou dívida escrita

## Semanas 8–9

- [ ] 401, 403 e 200
- [ ] Dois traces comparados
- [ ] DLQ visível no espelho, ou dívida escrita
- [ ] mTLS quebrado e restaurado no oráculo

## Semanas 10–12

- [ ] smoke OK
- [ ] Playwright dos fluxos críticos verde
- [ ] k6 com p95 anotado
- [ ] Pipeline lido
- [ ] Portfolio com checkpoints honestos
""")

    write("evidencias/templates/relatorio-lab.md", """# Relatório de lab

- Semana:
- Arquivo do lab:
- O que eu fiz com a mão:
- O que eu vi (status, id, número):
- Figura do que aconteceu (Mermaid ou foto do papel):
- O que automatizei (comando):
- O que ficou para evoluir:
""")

    write("evidencias/templates/bug-report.md", """# Bug

- Ambiente: oráculo local / espelho
- Usuário: qa ou admin (não cole a senha)
- Passos:
- Esperado:
- Obtido (status e corpo sem token):
- orderId:
- Limitação conhecida do lab? sim / não
- Onde olhei (log, Kafka, Mongo, Jaeger):
""")

    write("evidencias/templates/evidencia-trace-jaeger.md", """# Trace

- Cenário: feliz / pagamento falho
- Horário:
- orderId:
- Serviços que apareceram no Jaeger:
- O que foi diferente do outro cenário:
- Query `up` no Prometheus (quais jobs em 1):
""")

    write("evidencias/templates/portfolio-aluno.md", """# Portfolio

- Horas gastas por semana (honesto):
- Checkpoints verdes:
- Dívidas:
- Uma melhoria medida (antes e depois) ou a recusa justificada:
- Risco do oráculo que eu não vou copiar:
- Próximo ciclo (opcional): [plataforma de streaming](../../alem/plataforma-de-streaming.md)
""")

    write("alem/plataforma-de-streaming.md", """# Depois das 12 semanas — problema maior

Isto não é tarefa da semana 12. É o próximo ciclo, se você quiser.

StudyShop é pedido e estoque. Uma plataforma de vídeo é outro problema: arquivo grande, catálogo, busca, perfil, recomendação, várias regiões. O método é o mesmo: implementar um recorte, ver com a ferramenta certa, integrar por um id, automatizar, medir.

```mermaid
flowchart LR
  Agora[pedido e estoque] --> Busca[catalogo e busca]
  Busca --> Midia[arquivo e CDN]
  Midia --> Regiao[mais de uma regiao]
```

| Problema | Risco de teste | O que medir |
|----------|----------------|-------------|
| Catálogo grande | busca vazia ou lenta | p95 da busca |
| Arquivo de vídeo | upload incompleto | taxa de conclusão |
| Recomendação | lista vazia para usuário novo | fallback |
| Multi-região | dado atrasado | lag e erro |

Não copie a arquitetura do e-commerce e chame de streaming. Copie o ciclo de estudo.
""")

    write("semana-12/exemplo-cronjob.yaml", """# Exemplo de estudo. Não aplica no cluster sozinho se você só ler o arquivo.
apiVersion: batch/v1
kind: CronJob
metadata:
  name: studyshop-lab-date
spec:
  schedule: "*/1 * * * *"
  concurrencyPolicy: Forbid
  jobTemplate:
    spec:
      template:
        spec:
          restartPolicy: Never
          containers:
            - name: date
              image: busybox:1.36
              command: ["date"]
""")
