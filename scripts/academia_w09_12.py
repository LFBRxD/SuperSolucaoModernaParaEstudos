# -*- coding: utf-8 -*-
from academia_render import meta, lab, leitura, diagrama

def build():
    meta(9, "meta-01-tres-sinais", "Meta 9.1 — Log, métrica e trace", 70,
         "semana 6", "três jeitos de olhar a mesma request",
         "Log é uma linha sobre um fato. Métrica é um número ao longo do tempo (quantas requests, quantos erros). Trace é o caminho de uma request pelos serviços, com um trace id. Os três se completam. Um sozinho mente por omissão.",
         "No lab, o trace vai do serviço ao OpenTelemetry Collector e ao Jaeger (11011). Métrica o Prometheus busca no actuator (11012). Log você lê com `docker compose logs`.",
         ["Faça um pedido feliz.",
          "Abra o Jaeger e filtre pelo serviço `api-gateway` no horário do pedido.",
          "Abra um log do `orders-service` no mesmo minuto."],
         "Um trace e uma linha de log que você acredita serem do mesmo pedido.",
         "Procurar o orderId no Prometheus. Lá estão agregados, não o id, a menos que alguém tenha colocado label de alta cardinalidade (não faça isso).",
         "https://opentelemetry.io/docs/what-is-opentelemetry/",
         "Você diz o que cada ferramenta responde: o quê aconteceu, quanto aconteceu, por onde passou.",
         ["Qual das três mostra o orderId com mais facilidade hoje?"],
         "[lab-01-jaeger.md](lab-01-jaeger.md)")

    meta(9, "meta-02-sli", "Meta 9.2 — SLI simples", 55,
         "meta 9.1", "número que vira orçamento",
         "SLI é o indicador: por exemplo, porcentagem de pedidos que chegam a estado final em 60 segundos. SLO é a meta: por exemplo, 99% no lab. Sem o indicador, 'está lento' não é testável.",
         "Na semana 11 você mede. Hoje você escolhe o indicador e escreve como contar.",
         ["Defina um SLI: tempo até CONFIRMED ou CANCELLED.",
          "Defina um SLO de lab frouxo o bastante para a sua máquina, e anote a máquina.",
          "Não escolha 'CPU baixa'. Isso não é o que o usuário sente."],
         "Uma frase SLI e uma frase SLO.",
         "SLO de 50 ms copiado de blog, impossível com saga e Docker no notebook.",
         "https://sre.google/sre-book/service-level-objectives/",
         "O SLI cabe numa linha e você sabe de qual timestamp até qual timestamp.",
         ["O health UP entra nesse SLI? Não. Por quê?"],
         "[meta-03-dlq.md](meta-03-dlq.md)")

    meta(9, "meta-03-dlq", "Meta 9.3 — DLQ e replay", 70,
         "semana 5 e 7", "mensagem que não deve girar para sempre",
         "DLQ (dead letter) é o lugar da mensagem que falhou demais. Sem ela, ou você perde o evento, ou você reprocessa infinito e repete o estrago. Replay é pegar essa mensagem e mandar de novo, de propósito, depois de corrigir a causa.",
         "O oráculo só dá log.error e segue. Não há DLQ. Você constrói no espelho: tópico `lab.dlq` ou coleção.",
         ["Leia `docs/academia-qa/desafios/dlq.md`.",
          "Desenhe: consumer falha → tenta N vezes → publica na DLQ com o erro e o orderId.",
          "Replay é um comando seu, não automático no primeiro dia."],
         "Desenho com N tentativas e um lugar inspectável.",
         "Engolir a exceção e commitar o offset. A mensagem some e o pedido fica preso sem rastro.",
         "https://kafka.apache.org/documentation/#design_consumerposition",
         "Você explica por que retry infinito é pior do que DLQ.",
         ["O que você guarda junto: payload original ou só o erro?"],
         "[lab-02-dlq.md](lab-02-dlq.md)")

    meta(9, "meta-04-idempotencia", "Meta 9.4 — Idempotência", 65,
         "meta 9.3", "de novo sem efeito duplo",
         "Operação idempotente pode rodar outra vez e o resultado de negócio fica o mesmo. Chave: orderId mais o tipo do efeito (`stock-reserved`). Na segunda vez, você acha a chave e não decrementa de novo.",
         "DLQ e replay sem idempotência duplicam pagamento ou estoque. Os dois temas andam juntos.",
         ["Escolha a chave do espelho.",
          "Escreva o teste: processar o mesmo evento duas vezes deixa o estoque igual ao de uma vez.",
          "Implemente no lab, não só no papel."],
         "Teste descrito em uma frase com número.",
         "Usar timestamp como chave. Toda reentrega vira outra chave.",
         "https://stripe.com/blog/idempotency (o conceito de chave; ignore a API deles)",
         "A chave não inclui hora.",
         ["Replay da DLQ deve ser seguro por quê?"],
         "[lab-03-replay.md](lab-03-replay.md)")

    lab(9, "lab-01-jaeger", "Lab 9.1 — Dois traces: feliz e falha", 80,
        "meta 9.1", "Jaeger",
        """```mermaid
flowchart LR
  Apps[servicos] --> Otel[otel-collector]
  Otel --> Jaeger[Jaeger :11011]
  Otel --> Prom[Prometheus :11012]
  Prom --> Graf[Grafana :11010]
```""",
        "Comparar o trace do pedido feliz com o do pagamento forçado.",
        ["Não implemente trace no espelho neste lab se o tempo apertar. Observe o oráculo. O checkpoint de observabilidade pede o espelho depois, com pelo menos logs estruturados."],
        ["Pedido feliz. Ache o trace. Anote serviços que aparecem.",
         "Pedido com falha de pagamento. Anote o que muda.",
         "No Prometheus, abra a query `up` e diga quais jobs estão 1."],
        ["O orderId pode não estar no span. Correlacione por horário e pelo log. Escreva essa limitação.",
         "Grafana: abra o dashboard StudyShop e diga o que o painel `up` mostra."],
        ["Preencha o template `docs/academia-qa/evidencias/templates/evidencia-trace-jaeger.md` duas vezes."],
        ["Se não houver trace, confira `OTEL_EXPORTER_OTLP_ENDPOINT` e se o collector está de pé. Não desligue o export 'para sumir o erro'."],
        "Start-Process http://localhost:11011",
        "xdg-open http://localhost:11011 || true",
        ["Olhar trace de ontem.", "Query `up` sem resultado porque o Prometheus não alcança o nome Docker (você está fora da rede: use a UI, que já está configurada)."],
        ["docs/observabilidade.md tem o passo a passo das URLs."],
        ["Os dois traces deveriam ser idênticos?"],
        "Template de trace preenchido para os dois cenários.",
        "Aprovado se você aponta uma diferença concreta entre feliz e falha.",
        "[lab-02-dlq.md](lab-02-dlq.md)")

    lab(9, "lab-02-dlq", "Lab 9.2 — Falhar de propósito e cair na DLQ", 90,
        "meta 9.3", "DLQ no espelho",
        """```mermaid
flowchart LR
  Msg[mensagem] --> C[consumer]
  C -->|ok| Ok[efeito unico]
  C -->|falhou N vezes| DLQ[lab.dlq ou colecao]
```""",
        "Uma mensagem ruim não gira para sempre e fica visível.",
        ["No espelho, o consumer de um tópico de lab falha se o payload tiver `forceError: true`.",
         "Depois de 3 tentativas, grave na DLQ com orderId, erro e payload.",
         "Loge cada tentativa."],
        ["Publique uma mensagem boa e uma ruim.",
         "A boa aplica efeito uma vez.",
         "A ruim aparece na DLQ e para."],
        ["O orderId da DLQ é o da mensagem original.",
         "O tópico principal não cresce sem limite por causa do retry (não re-publique no mesmo tópico sem controle)."],
        ["Teste automatizado com broker de teste ou com a coleção DLQ, assertindo 1 documento depois de N tentativas."],
        ["Conte tentativas. Se passar de 3, o teste falha."],
        "# espelho",
        "# espelho",
        ["Catch vazio.", "Re-publicar no mesmo tópico e criar loop."],
        ["Tópico separado `lab.dlq` ou coleção `dead_letters`."],
        ["Como você vê a DLQ sem debugger?"],
        "Evidência da mensagem boa e da ruim.",
        "Aprovado se a ruim para sozinha e é listável.",
        "[lab-03-replay.md](lab-03-replay.md)")

    lab(9, "lab-03-replay", "Lab 9.3 — Replay idempotente", 80,
        "lab 9.2 e meta 9.4", "reprocessar sem duplicar",
        """```mermaid
sequenceDiagram
  participant DLQ
  participant Worker
  participant Estoque
  DLQ->>Worker: replay
  Worker->>Estoque: aplica se a chave nao existe
  Worker->>Estoque: segunda vez nao altera
```""",
        "Reprocessar a mesma mensagem não muda o estoque duas vezes.",
        ["Guarde a chave orderId+efeito antes de aplicar.",
         "Um comando ou endpoint de lab `POST /lab/replay/{id}` tira da DLQ e processa.",
         "Chame duas vezes."],
        ["Estoque depois da primeira vez anotado.",
         "Estoque depois da segunda igual.",
         "Log diz 'já aplicado' na segunda."],
        ["A mensagem de DLQ e o estoque referenciam o mesmo id."],
        ["Teste JUnit ou script com os dois números."],
        ["Não faça replay automático em loop. Um comando explícito."],
        "# curl do replay no README do espelho",
        "# curl do replay",
        ["Apagar a chave no sucesso e a segunda vez aplicar de novo.", "Replay em produção apontando para o oráculo."],
        ["A chave fica no Mongo do espelho, coleção `applied_effects`."],
        ["Por que a segunda chamada ainda retorna 200 e não 500?"],
        "Teste verde com estoque estável.",
        "Aprovado se a segunda aplicação não altera o número.",
        "[leitura-01-obs.md](leitura-01-obs.md)")

    leitura(9, "leitura-01-obs", "Leitura 9 — Onde olhar primeiro", 35,
            "semana 9",
            "Ordem de investigação para não abrir dez ferramentas sem pergunta.",
            [("Ordem", "1) status HTTP e corpo. 2) orderId no log. 3) mensagem no tópico. 4) trace no horário. 5) lag e métrica `up`."),
             ("DLQ", "Sem rastro, o retry vira achismo."),
             ("Idempotência", "Replay só é seguro com chave de efeito.")],
            ["https://opentelemetry.io/docs/what-is-opentelemetry/", "docs/observabilidade.md"],
            ["O que o Prometheus não guarda neste lab?",
             "Qual o N de tentativas que você escolheu?"],
            "Semana 10.")

    diagrama(9, "diagrama-01-sinais", "Diagrama 9.1 — A mesma compra em três sinais",
             "correlação",
             """```mermaid
flowchart TB
  Pedido[orderId]
  Pedido --> Log[log do servico]
  Pedido --> Topic[mensagem Kafka]
  Pedido --> Trace[trace no Jaeger por horario]
  Pedido --> Metric[metrica agregada sem o id]
```""",
             "Métrica não substitui o id. Ela diz se o problema é só seu ou de todo mundo.",
             "[diagrama-02-dlq.md](diagrama-02-dlq.md)")

    diagrama(9, "diagrama-02-dlq", "Diagrama 9.2 — Retry, DLQ, replay",
             "fim do loop",
             """```mermaid
flowchart LR
  A[tentativa 1] --> B[tentativa 2]
  B --> C[tentativa 3]
  C --> D[DLQ]
  D --> E[replay manual]
  E --> F[efeito idempotente]
```""",
             "A seta de replay não volta para o retry automático.",
             "Semana 10.")

    # semana 10
    meta(10, "meta-01-piramide", "Meta 10.1 — Pirâmide de testes", 55,
         "semanas 2 a 9", "o que cada teste aguenta",
         "Teste de unidade é rápido e estreito. Teste de API olha HTTP. Teste de UI olha o browser e é o mais lento e frágil. A pirâmide pede muitos testes baratos e poucos de ponta. Subir Docker para testar uma soma é desperdício. Não ter nenhum teste de ponta deixa a saga sem rede.",
         "Você já tem JUnit do espelho, smoke do oráculo, Bruno e, nesta semana, Playwright.",
         ["Desenhe a pirâmide e coloque um teste seu em cada faixa.",
          "Marque qual faixa falta.",
          "Não mova tudo para Playwright."],
         "Desenho com três faixas e um exemplo em cada.",
         "Só E2E, porque 'é o que o usuário vê', e a suíte leva 40 minutos e falha por animação.",
         "https://martinfowler.com/articles/practical-test-pyramid.html",
         "Você justifica um teste que NÃO é de UI.",
         ["O polling da saga fica em qual faixa?"],
         "[lab-01-smoke-full.md](lab-01-smoke-full.md)")

    meta(10, "meta-02-bruno-cli", "Meta 10.2 — Bruno como suíte", 55,
         "meta 10.1", "a coleção que roda sozinha",
         "Bruno guarda requests em arquivo. A CLI roda a pasta e falha se o assert falhar. Variável `accessToken` passa do login para o próximo request. Sem ordem e sem assert, a coleção é só favorito.",
         "A pasta `bruno/study-shop` é a suíte de API do oráculo. Você completa o que faltava: 401, falha de pagamento, estoque, polling, notificação.",
         ["Abra a coleção no Bruno ou leia os `.bru`.",
          "Veja `environments/local.bru`.",
          "Leia o README da pasta."],
         "Você sabe qual request grava o token.",
         "Rodar create-order sem ter rodado login e culpar a API.",
         "https://docs.usebruno.com/bru-cli/overview",
         "Um comando de CLI está copiado no seu caderno.",
         ["O que o assert de status 200 não prova sobre a saga?"],
         "[lab-02-playwright-login.md](lab-02-playwright-login.md)")

    meta(10, "meta-03-espera", "Meta 10.3 — Esperar estado final sem sleep cego", 60,
         "meta 6.2", "polling com teto",
         "Espere até o status ser final ou até o relógio estourar. Intervalo fixo curto, timeout explícito, mensagem com o último status visto. `Thread.sleep(60000)` sempre, mesmo quando confirmou em 2 segundos, só deixa a suíte lenta.",
         "Playwright tem `expect.poll` ou repetir o GET. O smoke do repo faz loop. Copie a ideia, não um número mágico sem mensagem.",
         ["Leia a função de espera em `scripts/smoke.sh`.",
          "Anote timeout e intervalo.",
          "Escreva a mensagem de falha que você gostaria de ler."],
         "Timeout, intervalo e exemplo de mensagem.",
         "Aumentar timeout para 10 minutos para 'não flake' e esconder serviço parado.",
         "https://playwright.dev/docs/test-assertions#expectpoll",
         "Sua mensagem de falha inclui o último status.",
         ["CONFIRMED e CANCELLED são os únicos finais. O que você faz com AWAITING_* no fim do tempo?"],
         "[lab-03-playwright-pedido.md](lab-03-playwright-pedido.md)")

    meta(10, "meta-04-evidencia", "Meta 10.4 — Evidência quando falha", 50,
         "meta 10.3", "o relatório que você consegue ler depois",
         "Teste verde não precisa de print. Teste vermelho precisa de status, corpo, orderId e, na UI, trace do Playwright. Sem isso você repete o clique amanhã sem lembrar.",
         "O CI guarda log do Compose e o relatório do Playwright. Localmente você usa os templates em `docs/academia-qa/evidencias/templates/`.",
         ["Abra o template de bug.",
          "Preencha um bug didático: estoque que não volta após pagamento falho, marcado como limitação conhecida, não como defeito surpresa.",
          "Ou preencha um defeito real se você achou um."],
         "Um template preenchido.",
         "Print sem URL, sem horário e sem usuário (`qa` ou `admin`).",
         "docs/academia-qa/evidencias/templates/bug-report.md",
         "Outra pessoa entende o bug sem perguntar para você.",
         ["O que não entra no relatório? (token, senha)"],
         "[leitura-01-automacao.md](leitura-01-automacao.md)")

    lab(10, "lab-01-smoke-full", "Lab 10.1 — Rodar o smoke até o estado final", 70,
        "scripts de smoke", "oráculo",
        """```mermaid
flowchart LR
  H[health] --> L[login]
  L --> P[produtos]
  P --> O[pedido]
  O --> W[espera CONFIRMED]
  W --> N[notificacao]
  L --> F[falhas e RBAC]
```""",
        "Ver a suíte de API do oráculo passar, incluindo espera da saga.",
        ["Não reescreva o script se ele já cobre os casos. Leia-o e rode.",
         "Se um passo falhar, conserte o ambiente antes de 'pular o assert'."],
        ["`.\\scripts\\smoke.ps1` ou `./scripts/smoke.sh`.",
         "Leia cada linha que o script imprime.",
         "Confira que ele espera status final e busca notificação."],
        ["O orderId impresso existe no Kafka UI.",
         "O 401 sem token e o 403 do qa estão na saída."],
        ["O comando é o próprio script. Você não copia o curl para outro lugar sem necessidade."],
        ["Anote a duração. Se passar de 3 minutos, olhe qual passo esperou demais."],
        ".\\scripts\\smoke.ps1",
        "./scripts/smoke.sh",
        ["Stack no meio do boot.", "Estoque zerado por testes anteriores sem reset. Use `scripts/qa-reset` se precisar do seed."],
        ["Timeout padrão 60s. Variável de ambiente documentada no cabeçalho do script."],
        ["Qual passo o smoke antigo (só o POST) não provava?"],
        "Saída com Smoke OK.",
        "Aprovado se CONFIRMED, CANCELLED de pagamento e CANCELLED de estoque aparecem na saída.",
        "[lab-02-playwright-login.md](lab-02-playwright-login.md)")

    lab(10, "lab-02-playwright-login", "Lab 10.2 — Login e menu de admin na UI", 80,
        "meta 10.1", "Playwright",
        """```mermaid
flowchart LR
  T[spec login] --> UI[web :11000]
  UI --> API[gateway :11001]
```""",
        "Automatizar o que você viu no DevTools na semana 1: qa não vê estoque, admin vê.",
        ["Os specs já estão em `apps/web/e2e`. Leia `login-rbac.spec.ts` antes de rodar.",
         "Instale o browser do Playwright uma vez: `npx playwright install chromium` dentro de `apps/web`."],
        ["Suba a stack.",
         "`npm run e2e` em `apps/web`, ou só o spec de login.",
         "Abra o relatório HTML se falhar."],
        ["O spec usa `data-testid`, não texto solto traduzível, sempre que o mapa em `docs/cenarios-qa.md` tem id.",
         "Se você adicionar um spec, use os mesmos ids."],
        ["O comando fica no `package.json` como `e2e`."],
        ["Não aumente timeout global para 5 minutos. Ajuste a espera do elemento que falta."],
        "cd apps/web\nnpm run e2e -- e2e/login-rbac.spec.ts",
        "cd apps/web\nnpm run e2e -- e2e/login-rbac.spec.ts",
        ["Web ainda em splash e o testid não apareceu.", "Stack em modo OIDC e o formulário local não existe. O spec assume momento 1."],
        ["`npx playwright show-report` abre o trace."],
        ["Por que o spec não procura a palavra Estoque no CSS e sim `nav-admin-stock`?"],
        "Spec verde.",
        "Aprovado se qa sem menu e admin com menu passam no mesmo arquivo.",
        "[lab-03-playwright-pedido.md](lab-03-playwright-pedido.md)")

    lab(10, "lab-03-playwright-pedido", "Lab 10.3 — Pedido feliz e falhas na UI", 90,
        "lab 10.2", "estado final na tela",
        """```mermaid
sequenceDiagram
  participant PW as Playwright
  participant UI as catalogo
  participant Det as detalhe
  PW->>UI: cria pedido
  PW->>Det: espera order-status final
```""",
        "A UI chega em CONFIRMED, em CANCELLED por pagamento e em CANCELLED por estoque.",
        ["Leia os specs de pedido. Eles esperam o testid `order-status`.",
         "O de estoque insuficiente repõe `prod-raro` via API admin antes, para não depender da sujeira anterior."],
        ["Rode a pasta `e2e`.",
         "Se um spec falhar, abra o trace e o último status visto."],
        ["Confira no log do Playwright o orderId.",
         "Busque esse id na Kafka UI uma vez, para ligar UI e evento."],
        ["Mantenha os quatro fluxos: login/RBAC, feliz, pagamento, estoque, e o admin salvando estoque.",
         "Não duplique o smoke inteiro na UI."],
        ["Flaky: olhe se você assertou estado intermediário. Troque para esperar o final."],
        "cd apps/web\nnpm run e2e",
        "cd apps/web && npm run e2e",
        ["`prod-raro` com estoque 0.", "Clicar em adicionar uma vez só e a quantidade ficar 1, então o pedido confirma em vez de rejeitar."],
        ["O spec adiciona o raro duas vezes. Leia o código antes de mudar o produto."],
        ["Qual assert está na UI e qual continua só na API?"],
        "Suíte e2e verde com a stack no ar.",
        "Aprovado se os três finais de pedido passam.",
        "[leitura-01-automacao.md](leitura-01-automacao.md)")

    leitura(10, "leitura-01-automacao", "Leitura 10 — O que não automatizar ainda", 30,
            "semana 10",
            "Evitar suíte que ninguém roda.",
            [("Automatize", "Status final, 401/403, notificação existe, menu admin."),
             ("Deixe manual", "Explorar a UI do Jaeger, julgar se um texto de motivo está claro, quebrar certificado."),
             ("Evidência", "Falha sem orderId não serve.")],
            ["https://playwright.dev/docs/best-practices", "docs/cenarios-qa.md"],
            ["Cite um teste que deve continuar manual e por quê."],
            "Semana 11.")

    diagrama(10, "diagrama-01-piramide", "Diagrama 10.1 — Pirâmide neste repositório",
             "ferramentas",
             """```mermaid
flowchart TB
  E2E[Playwright poucos fluxos]
  API[Bruno e smoke]
  Int[JUnit com Spring no espelho]
  Unit[regras puras]
  E2E --> API --> Int --> Unit
```""",
             "Quanto mais embaixo, mais vezes você roda.",
             "[diagrama-02-espera.md](diagrama-02-espera.md)")

    diagrama(10, "diagrama-02-espera", "Diagrama 10.2 — Espera do estado final",
             "não assertar o meio",
             """```mermaid
flowchart LR
  Post[POST pedido] --> Loop{status final?}
  Loop -->|nao e ainda tem tempo| Get[GET de novo]
  Get --> Loop
  Loop -->|CONFIRMED ou CANCELLED| Ok[assert do cenario]
  Loop -->|timeout| Falha[mostra ultimo status]
```""",
             "O loop tem teto. A falha mostra o último status, não só 'timeout'.",
             "Semana 11.")

    # semana 11
    meta(11, "meta-01-percentil", "Meta 11.1 — Latência e percentil", 55,
         "semana 9 SLI", "não usar só a média",
         "A média esconde a cauda. p95 é o tempo abaixo do qual 95% das chamadas ficaram. Se o p95 do POST de pedido passa do orçamento, o usuário lento sofre mesmo com média bonita.",
         "k6 mede isso. O script do repo está em `tests/k6`. O orçamento do lab é largo porque a máquina é um notebook com Docker.",
         ["Leia o script `tests/k6/pedido-baseline.js` e ache o threshold.",
          "Não rode carga contra ambiente que não é seu.",
          "Anote a diferença entre baseline (pouca carga) e pico."],
         "Você define p95 com suas palavras e aponta o threshold do script.",
         "Comemorar média de 100 ms com p95 de 10 s.",
         "https://grafana.com/docs/k6/latest/using-k6/thresholds/",
         "Uma frase: o que acontece se o threshold falha (o processo do k6 sai com erro).",
         ["Health check entra na meta de latência do pedido?"],
         "[lab-01-k6.md](lab-01-k6.md)")

    meta(11, "meta-02-acessibilidade", "Meta 11.2 — Acessibilidade automatizada", 50,
         "semana 10", "a UI não é só o caminho feliz visual",
         "axe procura problemas objetivos: botão sem nome, contraste ruim, input sem label. Não substitui usar a tela com teclado, mas pega o que você não vê.",
         "O spec `a11y.spec.ts` roda axe na tela de login e no catálogo depois do login.",
         ["Leia o spec.",
          "Rode só ele.",
          "Se falhar, leia a regra do axe. Não dê disable na regra sem anotar o motivo."],
         "Relatório do axe lido, verde ou com uma violação explicada.",
         "Desligar todas as regras para ficar verde.",
         "https://github.com/dequelabs/axe-core/blob/develop/doc/rule-descriptions.md",
         "Você cita uma regra pelo nome.",
         ["O que o axe não testa? (fluxo de pedido, saga)"],
         "[lab-02-seguranca-passiva.md](lab-02-seguranca-passiva.md)")

    meta(11, "meta-03-seguranca-passiva", "Meta 11.3 — Olhar sem explorar ataque", 50,
         "semana 8", "baseline de configuração",
         "Baseline passivo é conferir o que já está documentado como risco: porta 11007 sem auth, CORS largo, Kafka sem TLS, segredo de lab no compose. Você não varre a internet e não escreve exploit.",
         "O checklist `docs/academia-qa/desafios/seguranca-passiva.md` lista o que marcar. Corrigir no espelho é evolução. No oráculo, você registra.",
         ["Percorra o checklist e marque achado ou não achado, com o arquivo.",
          "Não rode scanner contra host que não seja localhost.",
          "Não cole o JWT secret em print público fora do repo de estudo."],
         "Checklist marcado.",
         "Tratar o checklist como pentest e tentar invadir outro sistema.",
         "docs/academia-qa/desafios/seguranca-passiva.md",
         "Cada item tem evidência local.",
         ["Qual risco você corrigiria primeiro no espelho?"],
         "[meta-04-falha-controlada.md](meta-04-falha-controlada.md)")

    meta(11, "meta-04-falha-controlada", "Meta 11.4 — Latência e processo parado", 55,
         "meta 11.1", "o sistema avisa em vez de pendurar",
         "Parar um container ou atrasar uma resposta mostra se o gateway estoura deadline ou se a thread fica presa. Você já fez isso com inventory na semana 4. Agora você mede o tempo até o erro.",
         "Não use ferramenta de flood. Um `docker compose stop` e um cronômetro bastam.",
         ["Pare payments, crie um pedido, meça até o timeout do seu polling.",
         "Suba payments de novo.",
         "Anote se o pedido ficou preso. Esse é o caso do job da semana 7."],
         "Tempo até o teste desistir, e o status em que o pedido ficou.",
         "Deixar o serviço parado e encerrar o dia.",
         "docs/academia-qa/ferramentas/docker.md",
         "Você religou o serviço e o health voltou a UP.",
         ["O job de expiração ajudaria neste caso?"],
         "[lab-03-orcamento.md](lab-03-orcamento.md)")

    lab(11, "lab-01-k6", "Lab 11.1 — Baseline de carga no gateway", 70,
        "k6 instalado", "carga local",
        """```mermaid
flowchart LR
  K6[k6] --> Gw[gateway :11001]
  Gw --> Saga[saga]
  K6 --> Rel[p95 e erros]
```""",
        "Medir, não otimizar no escuro.",
        ["Instale k6: https://grafana.com/docs/k6/latest/set-up/install-k6/",
         "Leia o script antes de rodar. Ele faz login e cria poucos pedidos.",
         "Não aumente o VU além do que o script diz sem anotar."],
        ["`k6 run tests/k6/pedido-baseline.js` com a stack no ar.",
         "Copie p95, taxa de erro e quantas iterações.",
         "Se o threshold falhar, não mude o número para ficar verde. Anote o fato."],
        ["Olhe lag do Kafka depois da corrida.",
         "Olhe estoque: a corrida consome mouse. Reponha com admin ou reset se precisar."],
        ["O script é a automação. Guarde o output no relatório."],
        ["Uma corrida só. Soak longo fica como nota, não como obrigação de horas nesta semana."],
        "k6 run tests/k6/pedido-baseline.js",
        "k6 run tests/k6/pedido-baseline.js",
        ["Rodar contra produção.", "VU alto que enche o disco de log e você não percebe."],
        ["O script usa as mesmas senhas de lab. Não troque para senha pessoal."],
        ["O que você otimizaria primeiro, com este número na mão?"],
        "Output do k6 colado no relatório.",
        "Aprovado se há p95 e uma decisão (manter threshold ou registrar que a máquina não aguenta, sem falsificar).",
        "[lab-02-seguranca-passiva.md](lab-02-seguranca-passiva.md)")

    lab(11, "lab-02-seguranca-passiva", "Lab 11.2 — Checklist e axe", 70,
        "metas 11.2 e 11.3", "qualidade além do status",
        """```mermaid
flowchart TB
  Axe[axe na tela de login] --> Rel1[violacoes]
  Check[checklist de config] --> Rel2[riscos conhecidos]
```""",
        "Juntar acessibilidade e configuração insegura do lab num relatório só.",
        ["Rode o spec de a11y.",
         "Preencha o checklist passivo."],
        ["Abra a tela de login só com teclado (Tab até o botão). Anote se conseguiu entrar.",
         "Isso não está no axe. É o complemento manual."],
        ["Nenhum item 'não sei' sem dizer qual arquivo você abriu."],
        ["O spec de a11y entra no `npm run e2e` se não estiver marcado como opcional. Veja o nome do arquivo."],
        ["Se corrigir um label no oráculo, rode o spec de novo. Não deixe correção sem teste."],
        "cd apps/web\nnpx playwright test e2e/a11y.spec.ts",
        "cd apps/web && npx playwright test e2e/a11y.spec.ts",
        ["Scanner apontado para IP público.", "Corrigir CORS do oráculo no meio do curso e quebrar o tutorial sem anotar."],
        ["Riscos do oráculo podem permanecer, desde que o checklist os nomeie. Correção séria fica no espelho."],
        ["Qual achado é de lab de propósito?"],
        "Checklist e resultado do axe.",
        "Aprovado se os dois existem e o teclado foi tentado.",
        "[lab-03-orcamento.md](lab-03-orcamento.md)")

    lab(11, "lab-03-orcamento", "Lab 11.3 — Orçamento e uma melhoria", 80,
        "lab 11.1", "evoluir com número",
        """```mermaid
flowchart LR
  Medir[baseline] --> Orc[orcamento escrito]
  Orc --> Mudar[uma mudanca pequena]
  Mudar --> Medir2[medir de novo]
```""",
        "Mudar uma coisa e mostrar o número antes e depois, ou mostrar que a mudança não era sobre latência.",
        ["Escolha uma melhoria pequena no espelho: índice, timeout explícito, ou menos log síncrono.",
         "Se não houver o que melhorar com segurança, escreva o orçamento e não invente microotimização.",
         "Rode de novo o teste funcional. A melhoria não pode quebrar CONFIRMED."],
        ["Tabela: métrica, antes, depois.",
         "Se você não mediu de novo, a melhoria não entra como feita."],
        ["O smoke do oráculo continua verde. Sua mudança foi no espelho, a menos que você tenha corrigido um bug real do oráculo com teste."],
        ["k6 ou o cronômetro do polling. Uma métrica, não cinco."],
        ["Não tune o Kafka do oráculo no escuro."],
        "# k6 ou smoke com horario",
        "# k6 ou smoke",
        ["Mudar timeout do teste para o número caber.", "Otimizar sem o teste de regressão."],
        ["Orçamento de lab sugerido para discutir, não como verdade universal: p95 do POST abaixo de 2s na sua máquina, estado final em 60s."],
        ["O que você recusou otimizar e por quê?"],
        "Tabela antes/depois ou orçamento com recusa justificada.",
        "Aprovado se a regressão funcional passou depois da mudança.",
        "[leitura-01-carga.md](leitura-01-carga.md)")

    leitura(11, "leitura-01-carga", "Leitura 11 — Carga sem teatro", 30,
            "semana 11",
            "Não transformar k6 em prova de capacidade de produção.",
            [("Baseline", "Poucos usuários, número repetível."),
             ("Pico", "Subida curta para ver erro e lag."),
             ("O que este notebook não prova", "Comportamento com dezenas de nós, disco remoto e rede real.")],
            ["https://grafana.com/docs/k6/latest/"],
            ["Por que o threshold do lab é largo?",
             "Qual risco o k6 não enxerga? (mTLS, acessibilidade)"],
            "Semana 12.")

    diagrama(11, "diagrama-01-carga", "Diagrama 11.1 — O que a carga atravessa",
             "não é só o gateway",
             """```mermaid
flowchart LR
  K6 --> Gw[gateway]
  Gw --> Ord[orders]
  Ord --> Kafka
  Kafka --> Inv[inventory]
  Kafka --> Pay[payments]
```""",
             "Gargalo pode ser o consumidor, não o HTTP que o k6 chama.",
             "[diagrama-02-job-lento.md](diagrama-02-job-lento.md)")

    diagrama(11, "diagrama-02-job-lento", "Diagrama 11.2 — Job lento e o prazo do pedido",
             "SLA do relógio",
             """```mermaid
flowchart TB
  Pedido[pedido esperando] --> Prazo[prazo de 20s no lab]
  Job[job a cada 30s] --> Atraso[pode passar do prazo]
  Prazo --> Atraso
```""",
             "Se o intervalo do job é maior que o prazo, o cancelamento atrasa. Os dois números precisam ser lidos juntos.",
             "Semana 12.")

    # semana 12
    meta(12, "meta-01-pipeline", "Meta 12.1 — O que o CI faz", 60,
         "semana 10", "o mesmo comando fora da sua máquina",
         "CI roda o que você já roda: build, smoke, testes. A diferença é que roda limpo e guarda log quando falha. O arquivo é `.github/workflows/qa-lab.yml`.",
         "Sem CI, só o seu notebook sabe que passou. O workflow é a definição repetível.",
         ["Abra o YAML e liste os jobs.",
          "Ache o passo que sobe o Compose e o passo que sempre derruba (if: always).",
          "Não desabilite o teardown."],
         "Lista de jobs em cinco linhas suas.",
         "Workflow que nunca faz down e deixa runner sujo. O deste repo usa always.",
         "https://docs.github.com/en/actions/get-started/understand-github-actions",
         "Você aponta o passo do smoke e o passo do Playwright.",
         ["Por que o log é coletado mesmo quando falha?"],
         "[lab-01-ler-pipeline.md](lab-01-ler-pipeline.md)")

    meta(12, "meta-02-imagem", "Meta 12.2 — Imagem e configuração", 55,
         "semana 1", "o processo que o CI sobe",
         "A imagem é o jar mais o sistema de arquivos mínimo. Configuração (porta, URL do Kafka) entra por variável, não por recompilar. O que você muda no YAML do espelho tem que existir no Compose, senão funciona na IDE e quebra no container.",
         "O oráculo já tem Dockerfile por serviço. Leia um. Não reescreva todos.",
         ["Abra `apps/orders-service/Dockerfile`.",
          "Veja a variável `KAFKA_BOOTSTRAP_SERVERS` no Compose.",
          "Escreva o par: nome da env e onde o Java lê."],
         "Um par env → propriedade.",
         "Senha só dentro da imagem. Ela fica no histórico. No lab já é didático; não acrescente outra.",
         "https://docs.docker.com/get-started/docker-concepts/building-images/writing-a-dockerfile/",
         "Você explica por que o jar sozinho no Windows não vê o hostname `kafka`.",
         ["O que é publish de porta versus porta interna?"],
         "[meta-03-helm.md](meta-03-helm.md)")

    meta(12, "meta-03-helm", "Meta 12.3 — Helm e pod", 60,
         "meta 12.2", "o mesmo sistema no Kubernetes de estudo",
         "Helm instala vários manifests de uma vez. Pod é o processo no cluster. Service é o nome estável. O README `infra/helm/study-shop/README.md` manda o install e o port-forward. Observabilidade completa não está no chart: o README diz isso. Não procure Jaeger no cluster e conclua que o pedido não gera trace.",
         "CronJob é o agendamento da plataforma, diferente do Quartz dentro do Java.",
         ["Leia o README do chart até o install.",
          "Leia `docs/academia-qa/semana-12/diagrama-02-cronjob.md`.",
          "Se você não tiver kind, não finja que instalou. Siga o lab de leitura e marque o limite."],
         "Você sabe o que o chart inclui e o que ele não inclui (Jaeger).",
         "Achar que `kubectl port-forward` publica para a internet. Ele abre só na sua máquina.",
         "https://helm.sh/docs/intro/using_helm/",
         "Uma frase: por que o trace some no kind deste chart.",
         ["Qual a diferença entre CronJob e o Quartz da semana 7?"],
         "[lab-02-cronjob.md](lab-02-cronjob.md)")

    meta(12, "meta-04-capstone", "Meta 12.4 — Prova dos nove", 70,
         "checkpoints do espelho", "comparar sem copiar",
         "A prova é: o espelho sobe do zero, passa nos validadores dos checkpoints que você implementou, e você explica uma diferença consciente em relação ao oráculo (nome de campo, compensação de estoque, DLQ, job). Igualdade byte a byte não é o objetivo.",
         "O oráculo continua sendo a referência de comportamento público: login, catálogo, pedido que termina, 401/403.",
         ["Liste os checkpoints em `docs/academia-qa/checkpoints`.",
          "Marque feito, parcial ou não feito.",
          "Para cada parcial, uma frase do que falta."],
         "Lista honesta.",
         "Copiar o repositório inteiro para a pasta espelho e dizer que reconstruiu.",
         "docs/academia-qa/checkpoints/README.md",
         "Você apresenta a lista sem esconder o que faltou.",
         ["Qual diferença do espelho é melhoria e qual é dívida?"],
         "[lab-03-apresentar.md](lab-03-apresentar.md)")

    lab(12, "lab-01-ler-pipeline", "Lab 12.1 — Ler o workflow e rodar local o que ele roda", 70,
        "meta 12.1", "CI",
        """```mermaid
flowchart TB
  Push[push] --> Build[build e lint]
  Build --> Up[compose up]
  Up --> Smoke[smoke]
  Smoke --> E2E[playwright]
  E2E --> Down[compose down sempre]
  Smoke -->|falhou| Logs[guardar logs]
```""",
        "Executar localmente a espinha do workflow.",
        ["Leia `.github/workflows/qa-lab.yml` e numere os passos como o diagrama.",
         "Rode build de um módulo ou `mvn -DskipTests package` se a máquina aguentar, mais o smoke, mais o e2e se a stack estiver no ar."],
        ["Se o smoke falhar, olhe o log como o CI faria.",
         "Não comente o passo para 'passar'."],
        ["O down no final não depende do verde. Confira o `if: always()` no YAML."],
        ["O workflow é a automação. Você não recria outro CI paralelo."],
        ["Anote o tempo total. Compare com as 8–10 horas da semana: CI é minutos, estudo é o resto."],
        "Get-Content .github/workflows/qa-lab.yml",
        "sed -n '1,200p' .github/workflows/qa-lab.yml",
        ["Runner sem Docker e o job de compose falha. O YAML precisa dizer isso.", "Segredo de produção no workflow. Não adicione."],
        ["O job de documentação só checa se os README das semanas existem."],
        ["Qual passo você não conseguiu rodar local e por quê?"],
        "Lista passo → rodei ou não.",
        "Aprovado se você leu o YAML e rodou o smoke ou explicou o bloqueio com evidência.",
        "[lab-02-cronjob.md](lab-02-cronjob.md)")

    lab(12, "lab-02-cronjob", "Lab 12.2 — CronJob no papel e, se houver cluster, no kind", 80,
        "meta 12.3", "agendamento fora da JVM",
        """```mermaid
flowchart LR
  Cron[CronJob a cada minuto] --> Pod[pod curto]
  Pod --> Log[kubectl logs]
  Quartz[Quartz dentro do servico] --> JVM[processo longo]
```""",
        "Explicar quando o agendamento mora no cluster e quando mora no Quartz.",
        ["Escreva um manifest de estudo (no relatório ou em `docs/academia-qa/semana-12/exemplo-cronjob.yaml` se ele existir) que só imprime a data e termina.",
         "Não use esse manifest para apagar banco.",
         "Se tiver kind e helm, siga o README do chart e faça port-forward. Se não tiver, entregue o manifest e a comparação com o Quartz."],
        ["`kubectl get pods` mostra o pod do CronJob completando, se você instalou.",
         "Ou você descreve o que veria."],
        ["O pedido do oráculo não depende desse CronJob. Escreva isso para não misturar."],
        ["O manifest é a automação quando houver cluster. Sem cluster, o entregável é o YAML revisado por você, com `concurrencyPolicy: Forbid` comentado na sua nota."],
        ["Compare com o job de 20 segundos da semana 7: CronJob de 1 minuto é grosso demais para aquele prazo."],
        "kubectl version --client",
        "kubectl version --client",
        ["CronJob que roda o smoke destrutivo em cluster compartilhado. Não faça.", "Achar Jaeger no chart e perder uma hora. O README diz que não está."],
        ["infra/helm/study-shop/README.md seção de observabilidade."],
        ["Por que Forbid evita duas execuções juntas?"],
        "Manifest comentado e a comparação com Quartz.",
        "Aprovado se a comparação cita prazo curto versus cron de plataforma.",
        "[lab-03-apresentar.md](lab-03-apresentar.md)")

    lab(12, "lab-03-apresentar", "Lab 12.3 — Apresentar o espelho", 90,
        "todos os checkpoints que você fez", "capstone",
        """```mermaid
flowchart LR
  Oraculo[oraculo porta 11001] -. comportamento .-> Voce[sua explicacao]
  Espelho[espelho] -. comportamento .-> Voce
```""",
        "Contar o caminho do zero até o ponto em que você parou, com evidência.",
        ["Rode os validadores: `scripts/academy/validate-checkpoint.ps1 -Checkpoint all` com `ACADEMY_PROJECT_DIR` apontando para o espelho.",
         "O que falhar entra na lista de dívida, não é apagado do validador."],
        ["Para um pedido do oráculo, mostre status final e uma mensagem Kafka.",
         "Para o espelho, mostre o equivalente que existir (catálogo, job ou saga)."],
        ["Preencha `docs/academia-qa/evidencias/templates/portfolio-aluno.md` (cópia sua, fora do git se preferir).",
         "Inclua o desenho da arquitetura do espelho."],
        ["Não automatize a apresentação. Os testes é que estão automatizados."],
        ["Roadmap opcional: `docs/academia-qa/alem/plataforma-de-streaming.md`. Não é obrigatório para passar."],
        ".\\scripts\\academy\\validate-checkpoint.ps1 -Checkpoint all",
        "ACADEMY_PROJECT_DIR=../studyshop-do-zero ./scripts/academy/validate-checkpoint.sh all",
        ["Dizer que terminou com validador vermelho sem lista de dívida.", "Apresentar só o oráculo."],
        ["O hub `docs/academia-qa/README.md` tem a ordem se você se perder na hora de apresentar."],
        ["Qual risco do oráculo você resolveu no espelho?"],
        "Portfolio e saída dos validadores.",
        "Aprovado se a lista de checkpoints é honesta e pelo menos bootstrap e catalog-api passam.",
        "[leitura-01-plataforma.md](leitura-01-plataforma.md)")

    leitura(12, "leitura-01-plataforma", "Leitura 12 — O que vem depois das 12 semanas", 30,
            "fim do ciclo",
            "O capstone não é uma plataforma de streaming. O roadmap mostra o próximo problema, não mais tarefa escondida.",
            [("Próximo problema", "Mais usuários, mais regiões, mídia grande, busca. Cada um pede medida nova."),
             ("O que você já sabe fazer", "Subir, inspecionar, integrar, automatizar, medir."),
             ("O que não copiar", "Achar que e-commerce e streaming têm o mesmo desenho. O método de estudo é que se repete.")],
            ["docs/academia-qa/alem/plataforma-de-streaming.md"],
            ["Qual risco você levaria para o próximo ciclo?"],
            "Fim da trilha obrigatória.")

    diagrama(12, "diagrama-01-ci", "Diagrama 12.1 — Pipeline",
             "sempre derruba",
             """```mermaid
flowchart TB
  Build[build] --> Up[compose up]
  Up --> Wait[espera health]
  Wait --> Smoke[smoke]
  Smoke --> E2E[playwright]
  E2E --> Down[down]
  Smoke -.-> Logs[logs se falhar]
  E2E -.-> Logs
```""",
             "A seta pontilhada acontece na falha. O down acontece sempre.",
             "[diagrama-02-cronjob.md](diagrama-02-cronjob.md)")

    diagrama(12, "diagrama-02-cronjob", "Diagrama 12.2 — Quartz versus CronJob",
             "dois relógios",
             """```mermaid
flowchart TB
  subgraph jvm [Dentro do servico]
    Q[Quartz intervalo curto]
  end
  subgraph k8s [No cluster]
    C[CronJob minuto ou hora]
  end
```""",
             "Prazo de dezenas de segundos fica no Quartz. Tarefa diária pode ser CronJob.",
             "Capstone.")
