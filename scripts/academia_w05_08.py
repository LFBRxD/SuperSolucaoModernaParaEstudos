# -*- coding: utf-8 -*-
from academia_render import meta, lab, leitura, diagrama

def build():
    meta(5, "meta-01-broker", "Meta 5.1 — O que é o broker Kafka", 70,
         "semana 4", "fila durável de eventos",
         "Kafka guarda mensagens em tópicos. Quem publica não chama quem consome. O processo que publica pode cair depois de gravar a mensagem. Quem consome lê no próprio ritmo. Isso é diferente de uma chamada gRPC, que espera a resposta na hora.",
         "A saga do pedido só anda porque existem tópicos. Se você só olha o HTTP, o status muda 'sozinho' e você não sabe por quê.",
         ["No Compose, ache o serviço `kafka` e a porta do host `11009`.",
          "Dentro da rede, os serviços usam `kafka:9092`. Do seu PC, a porta é `11009`.",
          "Abra a Kafka UI em http://localhost:11016 depois que o Compose subir com o serviço `kafka-ui`."],
         "A UI lista o cluster `studyshop` ou mostra os tópicos `orders.events`, `inventory.events`, `payments.events` depois de um pedido.",
         "Conectar a UI em `localhost:11009` de dentro do container da UI. A UI está na rede Docker e deve usar `kafka:9092`.",
         "https://kafka.apache.org/documentation/#gettingStarted",
         "Você explica broker, tópico e por que a porta do host não é a porta interna.",
         ["gRPC espera resposta. Kafka espera o quê do produtor?"],
         "[lab-01-kafka-ui.md](lab-01-kafka-ui.md)")

    meta(5, "meta-02-particao-offset", "Meta 5.2 — Partição, offset e chave", 70,
         "meta 5.1", "ordem e posição da mensagem",
         "Um tópico é dividido em partições. Cada mensagem numa partição tem um offset (um número crescente). A chave (no lab, em geral `orderId`) escolhe a partição. Mensagens da mesma chave tendem a ficar na mesma partição e, portanto, em ordem.",
         "Se dois eventos do mesmo pedido trocarem de ordem entre partições diferentes, a saga pode confirmar antes de reservar. A chave existe para reduzir essa chance.",
         ["Na Kafka UI, abra `orders.events` e veja o número de partições (o serviço declara 3).",
          "Depois de um pedido, abra uma mensagem e ache `eventType` e a chave.",
          "Anote o offset."],
         "Uma mensagem com `eventType` igual a `OrderCreated` e chave igual ao `orderId` da API.",
         "Achar que offset é o id do pedido. Offset é a posição na partição.",
         "https://kafka.apache.org/documentation/#intro_topics",
         "Você desenha tópico → partição → offset com um exemplo real.",
         ["Por que a chave é o orderId e não o e-mail?"],
         "[meta-03-consumer-group.md](meta-03-consumer-group.md)")

    meta(5, "meta-03-consumer-group", "Meta 5.3 — Consumer group e lag", 70,
         "meta 5.2", "quem já leu a mensagem",
         "Consumer group é o nome do grupo de leitores que dividem as partições. Cada grupo tem o próprio offset. `inventory-service` e `notifications-service` leem o mesmo tópico `orders.events` em grupos diferentes. Os dois recebem as mensagens. Lag é quantas mensagens o grupo ainda não processou.",
         "Lag alto significa que o consumidor está atrasado. O HTTP do pedido pode já ter respondido `CREATED` enquanto o estoque ainda não correu.",
         ["Na UI, abra Consumer Groups.",
          "Ache `inventory-service`, `orders-service`, `payments-service`, `notifications-service`.",
          "Anote o lag de um grupo depois de um pedido parado no meio, se conseguir."],
         "Pelo menos dois groups no tópico `orders.events`.",
         "Um único group para dois serviços: um 'rouba' a mensagem do outro e a saga perde um passo.",
         "https://kafka.apache.org/documentation/#intro_consumers",
         "Você explica por que notifications e inventory podem ler o mesmo evento.",
         ["Lag zero prova que a regra de negócio passou? Não. Por quê?"],
         "[lab-02-console-consumer.md](lab-02-console-consumer.md)")

    meta(5, "meta-04-pelo-menos-uma-vez", "Meta 5.4 — Entrega pelo menos uma vez", 60,
         "meta 5.3", "a mesma mensagem pode chegar duas vezes",
         "O consumidor pode processar a mensagem e falhar antes de gravar o offset. Kafka entrega de novo. O efeito (baixar estoque, criar notificação) precisa ser idempotente: fazer duas vezes não pode cobrar duas vezes.",
         "O oráculo não garante isso de ponta a ponta. É um risco. No espelho, você vai tratar isso nas semanas 7 e 9.",
         ["Leia o risco no hub `riscos-conhecidos.md`.",
          "Escreva um exemplo: `OrderCreated` processado duas vezes. O que aconteceria com o estoque se o código só fizesse `quantity - 1` sem checar o pedido.",
          "Não implemente a trava ainda."],
         "Um parágrafo seu sobre duplicata.",
         "Achar que Kafka entrega exatamente uma vez só porque 'é Kafka'. Não neste lab.",
         "https://kafka.apache.org/documentation/#semantics",
         "Você diz 'pelo menos uma vez' com um exemplo de estoque.",
         ["Onde você registraria que o orderId já foi reservado?"],
         "[lab-03-evento-no-espelho.md](lab-03-evento-no-espelho.md)")

    lab(5, "lab-01-kafka-ui", "Lab 5.1 — Ver tópicos na Kafka UI", 75,
        "meta 5.1", "inspeção visual",
        """```mermaid
flowchart LR
  QA[Voce] --> UI["kafka-ui :11016"]
  UI --> Broker["kafka:9092"]
  Prod[orders-service] --> Broker
```""",
        "Ver uma mensagem real sem usar só o log do Java.",
        ["O serviço `kafka-ui` já está no Compose do oráculo. Se a UI não abrir, suba de novo com `scripts/up`."],
        ["Crie um pedido pela web (login qa, um mouse) ou pelo Bruno.",
         "Abra http://localhost:11016.",
         "Abra o tópico `orders.events` e ache `OrderCreated` com o seu `orderId`."],
        ["Ache o mesmo `orderId` em `inventory.events` (`StockReserved` ou `StockRejected`).",
         "Se não aparecer em 30 segundos, olhe o lag do group `inventory-service` e o log do inventory."],
        ["Anote tópico, eventType e orderId. Isso vira assert na semana 10, não hoje."],
        ["Não apague tópico pela UI. Você quebraria o lab."],
        "Start-Process http://localhost:11016",
        "xdg-open http://localhost:11016 || true",
        ["UI vazia porque o pedido não foi criado (401).", "Olhar o tópico errado e achar que 'não houve evento'."],
        ["CLI equivalente está no lab seguinte, se a UI falhar."],
        ["A mensagem continua no tópico depois do consumidor ler?"],
        "Print ou texto com tópico, offset e orderId.",
        "Aprovado se você correlaciona API e mensagem pelo mesmo orderId.",
        "[lab-02-console-consumer.md](lab-02-console-consumer.md)")

    lab(5, "lab-02-console-consumer", "Lab 5.2 — Ler o tópico pela CLI", 70,
        "lab 5.1", "kafka-console-consumer",
        """```mermaid
flowchart LR
  Topic[orders.events] --> CLI[kafka-console-consumer]
  CLI --> Tela[seu terminal]
```""",
        "Não depender só da UI. O terminal mostra o JSON cru.",
        ["Não publique lixo no tópico."],
        ["No `infra`: o comando de consumer do lab de ferramentas (`docs/academia-qa/ferramentas/kafka-cli.md`).",
         "Deixe o consumer rodando, crie outro pedido, veja a linha aparecer.",
         "Pare o consumer com Ctrl+C. Ele é um group à parte se você não fixar `--group`; não use o group `inventory-service`."],
        ["Confira que o lag do `inventory-service` não disparou por sua causa.",
         "Se disparou, você usou o group errado. Anote o erro e não repita."],
        ["Salve um JSON de exemplo (sem dados pessoais; o e-mail do lab é fictício) no relatório."],
        ["Compare com a UI: os mesmos campos `eventType` e `orderId`."],
        "cd infra\ndocker compose exec kafka /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --list",
        "cd infra\ndocker compose exec kafka /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --list",
        ["`--group inventory-service` rouba mensagem do serviço.", "Esquecer `--from-beginning` e achar que o tópico está vazio (você só vê o que chegar depois)."],
        ["Use `--group qa-lab-leitura` para não colidir."],
        ["Por que o consumer de estudo precisa de outro group?"],
        "Uma linha JSON real no relatório.",
        "Aprovado se o group dos serviços não foi usado pelo seu consumer.",
        "[lab-03-evento-no-espelho.md](lab-03-evento-no-espelho.md)")

    lab(5, "lab-03-evento-no-espelho", "Lab 5.3 — Publicar um evento no espelho", 90,
        "labs 5.1 e 5.2", "primeiro produtor seu",
        """```mermaid
flowchart LR
  Api[seu catalogo ou orders minimo] --> Topic[seu topico pedidos]
  Topic --> UI[Kafka UI ou console]
```""",
        "Provar que o seu processo publica, antes de existir saga.",
        ["Suba um Kafka do espelho na porta 11109 ou use um tópico prefixado `lab.` no Kafka do oráculo. Prefira o broker separado se você já sofreu com group errado.",
         "Ao criar um produto ou um pedido mínimo, publique um JSON com `eventType` e id.",
         "Não implemente consumidor ainda, ou implemente um que só loga."],
        ["Leia a mensagem na UI ou no console.",
         "O id da API aparece na mensagem."],
        ["Reinicie o produtor. A mensagem antiga continua no tópico (log durável).",
         "Escreva isso no relatório."],
        ["Um teste que sobe broker é opcional. Mínimo: script que falha se o curl não devolver o id que você depois acha no tópico. Pode ser manual nesta semana, com o passo escrito."],
        ["Meça o tempo entre o HTTP 200 e a mensagem aparecer. Anote."],
        "# producer no espelho\n# consumer de leitura com group proprio",
        "# producer no espelho",
        ["Publicar no tópico `orders.events` do oráculo e confundir a saga real.", "Esquecer a chave e achar que a ordem será sempre global."],
        ["Tópico novo `lab.catalog.events` evita misturar com a saga."],
        ["A mensagem some quando o consumidor lê?"],
        "Id da API igual ao id na mensagem.",
        "Aprovado se você mostra os dois lados.",
        "[leitura-01-kafka.md](leitura-01-kafka.md)")

    leitura(5, "leitura-01-kafka", "Leitura 5 — Kafka para QA", 45,
            "semana 5",
            "Fixar o vocabulário que a UI mostrou.",
            [("Tópico", "Nome lógico. No lab: `orders.events`, `inventory.events`, `payments.events`."),
             ("Group", "Quem acompanha o próprio progresso. Dois groups leem tudo. Dois membros do mesmo group dividem partições."),
             ("Lag", "Atraso. Útil, mas não substitui olhar o status do pedido.")],
            ["https://kafka.apache.org/documentation/#gettingStarted"],
            ["Qual group lê `OrderCreated` para baixar estoque?",
             "O que você não deve passar em `--group` num consumer de estudo?"],
            "Semana 6.")

    diagrama(5, "diagrama-01-topico", "Diagrama 5.1 — Tópico, partição, offset",
             "anatomia",
             """```mermaid
flowchart TB
  Topic[orders.events]
  Topic --> P0[particao 0]
  Topic --> P1[particao 1]
  Topic --> P2[particao 2]
  P0 --> O0["offset 0 OrderCreated"]
  P0 --> O1["offset 1 OrderConfirmed"]
```""",
             "A ordem é garantida dentro da partição, não entre partições.",
             "[diagrama-02-groups.md](diagrama-02-groups.md)")

    diagrama(5, "diagrama-02-groups", "Diagrama 5.2 — Dois groups, um tópico",
             "fan-out",
             """```mermaid
flowchart LR
  T[orders.events] --> G1[group inventory-service]
  T --> G2[group notifications-service]
```""",
             "Os dois leem. Notifications só age em alguns `eventType`. Inventory só age em `OrderCreated`.",
             "Semana 6.")

    # semana 6
    meta(6, "meta-01-estados", "Meta 6.1 — Máquina de estados do pedido", 70,
         "semana 5", "status que você asserta",
         "O pedido não pula direto para confirmado. Ele passa por estados. O documento `docs/status-pedido.md` lista a cadeia. Estados intermediários podem durar milissegundos. Seu teste não pode exigir um único GET no meio do caminho.",
         "Flaky test nasce aqui: você lê `AWAITING_STOCK` e falha porque 'não está CONFIRMED', sem esperar.",
         ["Leia `docs/status-pedido.md` e desenhe os estados no papel.",
          "Marque os estados finais: `CONFIRMED` e `CANCELLED`.",
          "Marque os intermediários."],
         "Desenho com pelo menos os estados do arquivo.",
         "Tratar `AWAITING_PAYMENT` como erro. Ele é passagem.",
         "docs/status-pedido.md",
         "Você lista dois finais e dois intermediários de memória.",
         ["Por que um único GET logo após o POST é fraco?"],
         "[meta-02-eventual.md](meta-02-eventual.md)")

    meta(6, "meta-02-eventual", "Meta 6.2 — Consistência eventual", 60,
         "meta 6.1", "agora não é o estado final",
         "Consistência eventual significa: se nada der errado, em algum momento o estado esperado aparece. Não é instantâneo. O QA espera com timeout (por exemplo 60 segundos) e intervalo (por exemplo 1 segundo).",
         "A web faz polling de 2 segundos na tela de detalhe. A API não empurra websocket. Você repete o GET.",
         ["Abra um pedido e atualize até o status parar de mudar.",
          "Anote quantos segundos levou.",
          "Escreva o timeout que você usaria num script."],
         "Um pedido que chegou em estado final e o tempo anotado.",
         "Timeout de 1 segundo em máquina lenta e concluir que a saga está quebrada.",
         "https://martinfowler.com/articles/patterns-of-distributed-systems/ (visão geral; não leia o livro inteiro)",
         "Você tem um número de timeout justificado pelo que viu.",
         ["O que o teste deve dizer se o timeout estourar?"],
         "[lab-01-feliz.md](lab-01-feliz.md)")

    meta(6, "meta-03-pagamento-falho", "Meta 6.3 — Cancelar por pagamento", 60,
         "meta 6.2", "caminho negativo injetável",
         "O lab deixa você forçar falha de pagamento com `forcePaymentFailure: true` ou o header `X-Force-Payment-Failure: true`. O estado final é `CANCELLED`. O estoque, nesta versão, permanece decrementado. Isso está escrito de propósito. Não 'corrija' o oráculo achando que é distração.",
         "Você precisa reconhecer limitação de produto versus bug acidental. Aqui a limitação é didática e vira requisito do espelho na semana 7 (compensar).",
         ["Crie um pedido com a flag.",
          "Espere `CANCELLED`.",
          "Olhe a quantidade do produto antes e depois."],
         "Status CANCELLED e estoque que não voltou, anotado.",
         "Reportar bug sem ler o cenário 4 de `docs/cenarios-qa.md`.",
         "docs/cenarios-qa.md cenário 4",
         "Você descreve o comportamento sem chamar de surpresa.",
         ["No seu espelho, você vai compensar. O que precisa acontecer com o estoque?"],
         "[lab-02-falhas.md](lab-02-falhas.md)")

    meta(6, "meta-04-correlacao", "Meta 6.4 — Seguir o orderId", 70,
         "meta 6.3", "uma chave em todos os lugares",
         "O `orderId` liga API, documento no Mongo `orders`, mensagens nos três tópicos, pagamento e notificação. Sem ele você está olhando eventos de outra pessoa no lab.",
         "Investigação distribuída começa pela correlação, não pelo log inteiro.",
         ["Pegue um orderId finalizado.",
          "Ache-o na API, no mongosh do database `orders`, e em uma mensagem Kafka.",
          "Escreva os três lugares."],
         "Três evidências com o mesmo id.",
         "Filtrar Kafka por e-mail e misturar pedidos.",
         "docs/academia-qa/ferramentas/kafka-ui.md",
         "Os três lugares estão no relatório.",
         ["Qual lugar você olha primeiro quando o status não muda?"],
         "[lab-03-redesenhar.md](lab-03-redesenhar.md)")

    lab(6, "lab-01-feliz", "Lab 6.1 — Pedido feliz de ponta a ponta", 80,
        "semana 5 e meta 6.1", "CONFIRMED",
        """```mermaid
sequenceDiagram
  participant API as POST /api/orders
  participant O as orders.events
  participant I as inventory.events
  participant P as payments.events
  API->>O: OrderCreated
  O->>I: StockReserved
  I->>P: PaymentApproved
  P->>O: OrderConfirmed
```""",
        "Ver o estado final CONFIRMED e o estoque do mouse cair 1.",
        ["Use o oráculo. Não implemente a saga no espelho neste lab (isso é o lab 6.3)."],
        ["Anote o estoque de `prod-mouse`.",
         "Crie o pedido pela UI ou API.",
         "Faça polling até `CONFIRMED` ou até 60 segundos.",
         "Anote o estoque de novo."],
        ["Ache `OrderCreated`, `StockReserved`, `PaymentApproved`, `OrderConfirmed` na UI do Kafka.",
         "O mesmo orderId nos quatro."],
        ["Ainda não codifique o polling. Escreva o pseudocódigo: repetir GET, parar em CONFIRMED ou CANCELLED, falhar no timeout."],
        ["Se passou de 15 segundos, olhe o lag. Anote. Não otimize código do oráculo."],
        "curl.exe -s http://localhost:11001/api/health",
        "curl -s http://localhost:11001/api/health",
        ["Não esperar e fotografar AWAITING_PAYMENT como resultado final.", "Usar produto sem estoque e achar que o feliz quebrou."],
        ["A tela de detalhe já faz polling de 2s. Você pode só observar `order-status`."],
        ["Quais eventos são obrigatórios no feliz?"],
        "orderId, status final, estoque antes e depois.",
        "Aprovado se CONFIRMED e estoque caiu 1.",
        "[lab-02-falhas.md](lab-02-falhas.md)")

    lab(6, "lab-02-falhas", "Lab 6.2 — Pagamento e estoque", 80,
        "lab 6.1", "dois CANCELLED diferentes",
        """```mermaid
flowchart TB
  Pedido[pedido criado]
  Pedido --> Pag[forcePaymentFailure]
  Pedido --> Est[prod-raro quantidade 2]
  Pag --> C1[CANCELLED motivo pagamento]
  Est --> C2[CANCELLED motivo estoque]
```""",
        "Distinguir dois cancelamentos pelo motivo e pelo efeito no estoque.",
        ["Não altere Java do oráculo."],
        ["Pedido com `forcePaymentFailure` true. Espere CANCELLED. Anote estoque (não volta).",
         "Pedido `prod-raro` quantidade 2. Espere CANCELLED. Anote estoque do raro (não deve cair, porque a reserva falha antes).",
         "Se o raro já não tem estoque 1, peça ao admin para repor 1 antes."],
        ["No Kafka, o primeiro caminho tem `PaymentFailed`. O segundo tem `StockRejected` e não deve ter `PaymentApproved`.",
         "Escreva isso."],
        ["Pseudocódigo de dois asserts. Implementação na semana 10."],
        ["Escreva o bug que você abriria se o raro decrementasse mesmo rejeitado. Esse sim seria defeito."],
        "# ver docs/cenarios-qa.md cenarios 4 e 5",
        "# ver docs/cenarios-qa.md",
        ["Quantidade 2 no mouse (tem estoque) e achar que testou limite.", "Esquecer o Bearer e anotar 401 como CANCELLED."],
        ["Motivo fica em `statusReason` no JSON e em `order-status-reason` na tela."],
        ["Nos dois cancelamentos, o estoque se comporta igual?"],
        "Tabela com duas linhas: cenário, status, motivo, estoque antes, estoque depois, eventType decisivo.",
        "Aprovado se a tabela mostra comportamentos diferentes de estoque.",
        "[lab-03-redesenhar.md](lab-03-redesenhar.md)")

    lab(6, "lab-03-redesenhar", "Lab 6.3 — Redesenhar a saga e esboçar no espelho", 90,
        "lab 6.2", "você desenha antes de olhar",
        """```mermaid
stateDiagram-v2
  [*] --> CREATED
  CREATED --> AWAITING_STOCK
  AWAITING_STOCK --> AWAITING_PAYMENT
  AWAITING_STOCK --> CANCELLED
  AWAITING_PAYMENT --> CONFIRMED
  AWAITING_PAYMENT --> CANCELLED
```""",
        "Reconstruir o fluxo no papel e começar o esboço no espelho sem copiar as classes do oráculo.",
        ["Feche `docs/status-pedido.md` por 20 minutos e desenhe.",
         "Depois compare.",
         "No espelho, crie os nomes dos tópicos e dos eventTypes no README. Código mínimo: publicar `OrderCreated` ao criar um pedido em memória ou Mongo. Consumidor pode só logar nesta sessão."],
        ["Compare seu desenho com o arquivo oficial e liste o que esqueceu.",
         "Não apague o seu desenho. O esquecimento é o entregável."],
        ["O orderId do espelho aparece no log do consumidor.",
         "Ainda não precisa de pagamento real."],
        ["Guarde o desenho no relatório. O teste automático da saga completa fica para quando os três serviços existirem. Não finja que já existe."],
        ["Liste o que falta para o checkpoint `saga`: estoque, pagamento, estados finais."],
        "# desenho no relatorio",
        "# desenho no relatorio",
        ["Copiar o `SagaEventListener` do oráculo e não saber explicar uma linha.", "Desenho só com CONFIRMED, sem falhas."],
        ["Inclua os dois cancelamentos no desenho, mesmo que o espelho ainda não os rode."],
        ["Qual seta do seu desenho você não viu no Kafka do lab 6.1?"],
        "Desenho seu + lista de diferenças versus o doc.",
        "Aprovado se o desenho tem caminho feliz e os dois cancelamentos.",
        "[leitura-01-saga.md](leitura-01-saga.md)")

    leitura(6, "leitura-01-saga", "Leitura 6 — Saga em linguagem de teste", 40,
            "semana 6",
            "Nomear o que você já executou.",
            [("Saga", "Sequência de passos locais em serviços diferentes, ligada por eventos, com caminho de desfazer ou de desistir."),
             ("Por que não é uma transação só", "Mongo de orders e Mongo de inventory não compartilham uma transação. Ou cada um grava o seu, ou ninguém grava. O meio do caminho existe."),
             ("Compensação", "Desfazer a reserva se o pagamento falha. O oráculo não faz. O espelho deve fazer na semana 7.")],
            ["docs/status-pedido.md", "docs/arquitetura.md"],
            ["Qual estado é final?",
             "O que o teste faz se ficar em AWAITING_PAYMENT até o timeout?"],
            "Semana 7.")

    diagrama(6, "diagrama-01-feliz", "Diagrama 6.1 — Sequência feliz",
             "eventos em ordem",
             """```mermaid
sequenceDiagram
  participant O as orders
  participant I as inventory
  participant P as payments
  participant N as notifications
  O->>I: OrderCreated
  I->>O: StockReserved
  I->>P: StockReserved
  P->>O: PaymentApproved
  O->>N: OrderConfirmed
```""",
             "Notifications não entra no meio. Ela reage ao confirmado ou ao cancelado.",
             "[diagrama-02-falhas.md](diagrama-02-falhas.md)")

    diagrama(6, "diagrama-02-falhas", "Diagrama 6.2 — Duas falhas",
             "pagamento versus estoque",
             """```mermaid
flowchart TB
  subgraph pag [Pagamento falho]
    R1[StockReserved] --> F1[PaymentFailed] --> C1[OrderCancelled]
  end
  subgraph est [Estoque insuficiente]
    R2[StockRejected] --> C2[OrderCancelled]
  end
```""",
             "No primeiro, a reserva aconteceu. No segundo, não. O teste de estoque precisa dessa diferença.",
             "Semana 7.")

    # semana 7 quartz + webhook
    meta(7, "meta-01-notificacao", "Meta 7.1 — Notificação não é webhook", 60,
         "semana 6", "o que o oráculo faz hoje",
         "O notifications-service lê `OrderConfirmed` e `OrderCancelled`, grava um documento e expõe GET no gateway. Ninguém chama um sistema externo. Não há HTTP de saída. Webhook seria o contrário: o seu sistema chama uma URL de terceiro quando algo acontece.",
         "Quem testa 'se o e-mail saiu' neste oráculo não vai achar e-mail. Vai achar um documento e um GET.",
         ["Crie um pedido até o estado final.",
          "GET `http://localhost:11001/api/notifications/order/{orderId}` com Bearer.",
          "Veja também o Mongo do database `notifications`."],
         "Pelo menos uma notificação para o orderId.",
         "Procurar webhook no código do oráculo e achar que você está cego. Ele não existe. Você vai construir no espelho.",
         "apps/notifications-service NotificationController",
         "Você descreve a diferença em duas frases.",
         ["A UI mostra notificação? Não. Onde você olha então?"],
         "[lab-01-ver-notificacao.md](lab-01-ver-notificacao.md)")

    meta(7, "meta-02-webhook", "Meta 7.2 — Webhook com assinatura e retry", 75,
         "meta 7.1", "HTTP de saída",
         "Webhook é um POST seu para a URL do cliente, com corpo do evento e uma assinatura (HMAC) para o cliente saber que foi você. Timeout curto. Se falhar, tenta de novo poucas vezes. Sem assinatura, qualquer um forja o evento.",
         "Kafka não avisa um sistema que não é consumidor seu. Webhook avisa. Os dois podem coexistir.",
         ["Leia o desafio `docs/academia-qa/desafios/webhook.md` até a seção de contrato, sem implementar ainda.",
          "Desenhe: orders confirma → notificador → POST no receptor local.",
          "Anote o header de assinatura que você vai exigir."],
         "Desenho com timeout e número máximo de tentativas.",
         "Retry infinito. Isso derruba o receptor e o seu serviço.",
         "https://hookdeck.com/webhooks/guides/what-are-webhooks (conceito; ignore o produto)",
         "Você explica por que HMAC existe.",
         ["O que o receptor deve fazer se a assinatura não bater?"],
         "[meta-03-scheduled.md](meta-03-scheduled.md)")

    meta(7, "meta-03-scheduled", "Meta 7.3 — @Scheduled", 60,
         "meta 7.2", "o cron mais simples",
         "`@Scheduled` no Spring dispara um método de tempos em tempos dentro do mesmo processo. Serve para um lab de um processo só. Não lembra a última execução se o processo cai no meio, e dois processos disparam duas vezes.",
         "É o primeiro degrau. Você usa para um job óbvio e sente a limitação antes de ir ao Quartz.",
         ["Leia https://docs.spring.io/spring-framework/reference/integration/scheduling.html só a parte de @Scheduled e cron.",
          "Escreva um cron de laboratório de 15 segundos (não use isso em produção).",
          "Liste dois limites: sem cluster e difícil de inspecionar."],
         "Um cron escrito e dois limites no papel.",
         "Colocar regra de pedido dentro de `Thread.sleep` no request HTTP. Isso segura o usuário e não é agendamento.",
         "https://docs.spring.io/spring-framework/reference/integration/scheduling.html",
         "Você recusa sleep no request com uma frase.",
         ["Dois processos com o mesmo @Scheduled fazem o quê?"],
         "[meta-04-quartz.md](meta-04-quartz.md)")

    meta(7, "meta-04-quartz", "Meta 7.4 — Quartz: Job, Trigger, JobStore", 80,
         "meta 7.3", "agendamento que dá para inspecionar",
         "Job é o trabalho. Trigger é quando dispara (cron ou daqui a N segundos). JobStore é onde isso fica gravado. RAM some no restart. JDBC (ou o equivalente que você documentar) sobrevive. Misfire é 'deveria ter rodado e não rodou'. Cluster com JobStore compartilhado evita duas instâncias rodarem o mesmo disparo.",
         "Pedido preso em `AWAITING_PAYMENT` não se resolve com Kafka se o evento de pagamento nunca veio. Alguém precisa acordar e cancelar. Esse alguém é um job.",
         ["Leia o tutorial oficial do Quartz, seções de Job e Trigger: https://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/",
          "Desenhe Job `ExpireOrders` e Trigger de 20 segundos no lab.",
          "Decida o que fica inspecionável: log com jobName e orderId, ou um GET interno de jobs."],
         "Desenho Job + Trigger + onde você vai olhar.",
         "Cron de produção de madrugada no lab e você esperar horas. Use intervalo curto e documente que em produção o número muda.",
         "https://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/tutorial-lesson-01.html",
         "Você diferencia Job de Trigger sem olhar a página.",
         ["O que é misfire, com exemplo de notebook em sleep?"],
         "[lab-02-job-timeout.md](lab-02-job-timeout.md)")

    meta(7, "meta-05-outbox", "Meta 7.5 — Outbox e quando não usar job", 60,
         "meta 7.4", "não substituir Kafka por cron",
         "Outbox é gravar o evento na mesma transação do pedido e um poller publicar no Kafka. Job periódico varre o que ficou preso. Kafka continua sendo o caminho rápido. O job é a rede de segurança e o relógio (expirar, reconciliar, limpar).",
         "Quem troca a saga inteira por um cron de 1 minuto deixa o sistema lento e ainda perde ordem. Você precisa dos dois papéis claros.",
         ["Escreva três linhas: isto é evento, isto é job, isto é os dois.",
          "Exemplos do plano: OrderCreated é evento. Expirar pagamento é job. Retry de webhook pode ser job lendo uma tabela de tentativas.",
          "Não implemente outbox completo se o tempo estourar; implemente o job de expiração e deixe outbox como nota."],
         "Tabela de três linhas no relatório.",
         "Publicar no Kafka só de minuto em minuto 'para simplificar' e chamar de tempo real.",
         "https://microservices.io/patterns/data/transactional-outbox.html",
         "A tabela existe e o job de expiração está separado do evento de criação.",
         ["Retry de webhook é evento ou job? Defenda em uma frase."],
         "[lab-03-idempotencia-do-job.md](lab-03-idempotencia-do-job.md)")

    lab(7, "lab-01-ver-notificacao", "Lab 7.1 — Ver a notificação do oráculo", 60,
        "meta 7.1", "GET e Mongo",
        """```mermaid
flowchart LR
  Kafka[orders.events OrderConfirmed] --> NS[notifications-service]
  NS --> Mongo[(notifications)]
  QA[GET com Bearer] --> Gw[api-gateway]
  Gw --> NS
```""",
        "Provar que o estado final gerou registro, pela API e pelo banco.",
        ["Nada de webhook ainda."],
        ["Pedido CONFIRMED. GET de notificações por orderId.",
         "mongosh no database notifications.",
         "Pedido CANCELLED por pagamento. Deve haver notificação também."],
        ["O orderId da API, do Kafka e da notificação é o mesmo.",
         "A UI da web não lista isso. Escreva essa lacuna."],
        ["O smoke completo do repo passa a checar este GET. Leia `scripts/smoke.ps1` quando chegar na semana 10. Hoje, faça na mão."],
        ["A porta 11007 sem token também responde, porque o serviço não tem segurança própria. Anote como risco, não como feature para copiar."],
        "curl.exe -s http://localhost:11001/api/health",
        "curl -s http://localhost:11001/api/health",
        ["Esperar notificação de OrderCreated. O listener ignora esse tipo.", "Chamar a rota sem Bearer no gateway e anotar 401 como 'não gerou'."],
        ["Direto no serviço: http://localhost:11007/api/notifications — só para ver o risco."],
        ["Por que a UI não basta para testar notificação?"],
        "Dois GETs: um CONFIRMED e um CANCELLED, com os corpos.",
        "Aprovado se os dois existem e você cita o risco da porta 11007.",
        "[lab-02-job-timeout.md](lab-02-job-timeout.md)")

    lab(7, "lab-02-job-timeout", "Lab 7.2 — Job que cancela pedido parado", 100,
        "metas 7.3 a 7.5", "Quartz no espelho",
        """```mermaid
sequenceDiagram
  participant Pedido
  participant Quartz
  participant Log
  Pedido->>Pedido: AWAITING_PAYMENT
  Quartz->>Pedido: passou do prazo, cancela
  Quartz->>Log: jobName fireTime orderId
```""",
        "Um pedido que você deixou preso muda para cancelado sem você chamar outra API, depois do intervalo curto do lab.",
        ["No espelho, grave pedidos com status e `updatedAt`.",
         "Configure um job Quartz (não só @Scheduled) com intervalo de 15 a 30 segundos.",
         "Mantenha um @Scheduled separado que só loga 'estou vivo', para você sentir a diferença.",
         "O job de expiração cancela se o status for de espera e a idade passou do prazo do lab (também curto, 20 segundos).",
         "Log inclui `jobName`, `fireTime`, `orderId`."],
        ["Crie um pedido preso (sem publicar pagamento).",
         "Não chame cancelar na mão.",
         "Espere o intervalo e leia o status.",
         "Veja o log."],
        ["O orderId do log é o do GET.",
         "Se você tiver Kafka no espelho, o cancelamento também pode publicar `OrderCancelled`. Se ainda não tiver, o documento basta e você anota a dívida."],
        ["Rode o job duas vezes sobre o mesmo pedido já cancelado. A segunda execução não pode 'cancelar de novo' mudando motivo ou estoque duas vezes.",
         "Teste automatizado com intervalo curto ou relógio injetado."],
        ["Suba duas instâncias só se o JobStore for compartilhado; senão escreva que o cluster fica para a semana 11 e por quê."],
        "# espelho na porta combinada no README",
        "# espelho",
        ["Prazo de 1 hora no lab e você achar que o job não existe.", "Cancelar todo pedido, inclusive o CONFIRMED, porque a query esqueceu o status."],
        ["Filtro: status intermediário E idade > prazo."],
        ["O que prova que foi o job e não você?"],
        "Log + status final, e teste de rodar duas vezes.",
        "Aprovado se a segunda execução é inócua e o log tem os três campos.",
        "[lab-03-idempotencia-do-job.md](lab-03-idempotencia-do-job.md)")

    lab(7, "lab-03-idempotencia-do-job", "Lab 7.3 — Webhook local e retry", 90,
        "lab 7.2 e meta 7.2", "receptor na sua máquina",
        """```mermaid
sequenceDiagram
  participant S as seu notificador
  participant R as receptor local :11180
  S->>R: POST evento mais assinatura
  alt falhou
    S->>S: agenda retry
    S->>R: POST de novo
  end
```""",
        "Entregar um POST assinado num receptor seu e não entregar duas vezes o efeito quando o retry acontece.",
        ["Suba um receptor mínimo que grava os POSTs em memória e tem uma rota para listá-los.",
         "Uma flag de teste faz os dois primeiros POSTs falharem.",
         "O notificador tenta de novo com limite (por exemplo 3) e intervalo crescente.",
         "O receptor ignora assinatura inválida com 401."],
        ["Dispare um evento. Veja a lista do receptor.",
         "Force falha e veja mais de uma tentativa no log, e um único efeito se o receptor deduplica pelo id do evento."],
        ["O orderId está no corpo.",
         "Tentativa esgotada fica registrada para a DLQ da semana 9, mesmo que a DLQ ainda seja uma coleção `webhook_dead`."],
        ["Teste: assinatura errada não entra. Teste: duas entregas do mesmo id só criam um registro de negócio."],
        ["Não aponte o webhook para a internet. Só localhost."],
        "# receptor em 127.0.0.1:11180",
        "# receptor em 127.0.0.1:11180",
        ["Retry sem limite.", "Assinatura só no query string, vazando em log de proxy."],
        ["Header `X-Signature` com HMAC SHA-256 do corpo e um segredo de lab no YAML."],
        ["Qual id você usa para deduplicar: offset do Kafka ou id do evento de negócio?"],
        "Lista do receptor e um teste de assinatura inválida.",
        "Aprovado se o efeito de negócio aparece uma vez e a tentativa falha fica visível.",
        "[leitura-01-jobs.md](leitura-01-jobs.md)")

    leitura(7, "leitura-01-jobs", "Leitura 7 — @Scheduled, Quartz e CronJob", 40,
            "semana 7",
            "Comparar as três ferramentas depois de ter um job rodando.",
            [("@Scheduled", "Dentro da JVM, simples, sem memória de cluster."),
             ("Quartz", "Job, Trigger, JobStore, misfire, cluster se o store for compartilhado."),
             ("CronJob do Kubernetes", "A plataforma dispara um processo e mata. Você não segura thread. Entra na semana 12. Não substitui um trigger de segundos dentro da saga sem cuidado com sobreposição.")],
            ["https://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/tutorial-lesson-01.html",
             "https://docs.spring.io/spring-framework/reference/integration/scheduling.html"],
            ["Onde o misfire fica registrado no seu lab?",
             "Por que o oráculo precisa de um job que ele ainda não tem?"],
            "Semana 8.")

    diagrama(7, "diagrama-01-tres-caminhos", "Diagrama 7.1 — Kafka, webhook e job",
             "qual caminho para qual problema",
             """```mermaid
flowchart TB
  Fato[algo aconteceu]
  Fato --> K[Kafka para servicos internos]
  Fato --> W[Webhook para sistema externo]
  Relogio[tempo passou] --> J[Quartz ou Scheduled]
```""",
             "Evento não espera relógio. Relógio não substitui o evento rápido.",
             "[diagrama-02-quartz.md](diagrama-02-quartz.md)")

    diagrama(7, "diagrama-02-quartz", "Diagrama 7.2 — Job, Trigger, JobStore",
             "peças do Quartz",
             """```mermaid
flowchart LR
  Trigger[Trigger cron ou intervalo] --> Job[Job expirar pedido]
  Job --> Store[JobStore]
  Job --> Pedido[(pedido)]
  Job --> Log[log jobName fireTime orderId]
```""",
             "Você inspeciona o log e o status do pedido. Se usar JDBC, as tabelas QRTZ_ também contam.",
             "Semana 8.")

    # semana 8
    meta(8, "meta-01-401-403", "Meta 8.1 — 401 e 403", 60,
         "semana 4", "autenticar não é autorizar",
         "401: não sei quem você é (sem token ou token inválido). 403: sei quem você é e você não pode (USER no PUT de estoque). Os dois não são intercambiáveis. Teste que aceita 'erro' sem o número está frouxo.",
         "A matriz está em `docs/seguranca.md`. O gateway é quem aplica. A tela que esconde o menu não é segurança.",
         ["GET `/api/products` sem header. Espere 401.",
          "Login qa e PUT estoque. Espere 403.",
          "Login admin e o mesmo PUT. Espere 200."],
         "Os três status, anotados.",
         "Chamar 403 de 401 no bug. O desenvolvedor procura o filtro errado.",
         "https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status/401",
         "Você reproduz os três sem olhar o tutorial.",
         ["Esconder o botão na UI impede o PUT? Não. Como você prova?"],
         "[lab-01-matriz.md](lab-01-matriz.md)")

    meta(8, "meta-02-jwt", "Meta 8.2 — JWT local", 70,
         "meta 8.1", "o token do momento 1",
         "JWT é um token assinado em três partes. No momento 1 o gateway assina com segredo compartilhado (HS256). O payload traz `sub`, `roles`, `iss`, `exp`. Quem tem o segredo forja token. Por isso o segredo do lab não serve em produção.",
         "Você precisa ler o payload para ver se a role que a UI mostra é a role que a API acredita.",
         ["Siga `docs/tutoriais/01-jwt-local.md`.",
          "Cole o token no jwt.io só na sua máquina, em rede fechada. Não use token real de empresa.",
          "Anote `iss` e `roles`."],
         "Payload lido e uma frase sobre expiração.",
         "Achar que o token está criptografado. Ele está assinado. Dá para ler. Não dá para alterar sem invalidar a assinatura.",
         "https://jwt.io/introduction",
         "Você aponta a claim de role.",
         ["O que muda quando o exp passa?"],
         "[meta-03-oidc.md](meta-03-oidc.md)")

    meta(8, "meta-03-oidc", "Meta 8.3 — OIDC e PKCE", 75,
         "meta 8.2", "momento 2",
         "OIDC é login delegado. O Keycloak autentica e emite o token. PKCE impede que um código de autorização roubado no caminho seja trocado por token sem o verificador que ficou no browser. A UI redireciona; o gateway passa a validar pela chave pública (JWKS), não pelo segredo HS256.",
         "O mesmo RBAC (USER/ADMIN) continua. Muda quem emite o token.",
         ["Leia `docs/tutoriais/02-oidc-keycloak.md` até a metade.",
          "Suba o overlay só quando o lab mandar, para não misturar com o momento 1 no meio de outro teste.",
          "Anote a URL 11015."],
         "Você sabe qual porta é o Keycloak e qual claim a UI lê (`realm_access`).",
         "Deixar o overlay ligado e o Bruno antigo chamar `/api/auth/login`, que não existe no modo OIDC.",
         "https://oauth.net/2/pkce/",
         "Você explica PKCE em uma frase: segredo temporário criado pelo próprio browser.",
         ["Logout na UI apaga o token no Keycloak? Não neste lab. O que isso significa?"],
         "[lab-02-keycloak.md](lab-02-keycloak.md)")

    meta(8, "meta-04-cors", "Meta 8.4 — CORS", 50,
         "meta 8.1", "o browser e outra origem",
         "CORS é uma regra do browser. O browser pergunta com OPTIONS se pode chamar a API de outra origem. `curl` não faz essa pergunta. Por isso a API 'funciona no curl' e falha no browser de outra porta.",
         "O lab libera origem ampla de propósito. É risco, não modelo de produção.",
         ["Leia `CorsConfig` no gateway.",
          "No DevTools, ache um OPTIONS se você chamar a API de uma origem diferente. Se a web é same-origin via proxy, pode não haver preflight.",
          "Anote: same-origin no lab Docker (a web proxia `/api`)."],
         "Uma frase: de onde o browser chama e se houve OPTIONS.",
         "Concluir que a API está sem CORS porque o curl funcionou.",
         "https://developer.mozilla.org/pt-BR/docs/Web/HTTP/CORS",
         "Você distingue erro de CORS de 401.",
         ["Quem bloqueia CORS: o browser ou o curl?"],
         "[meta-05-mtls.md](meta-05-mtls.md)")

    meta(8, "meta-05-mtls", "Meta 8.5 — mTLS entre serviços", 70,
         "meta 8.2", "identidade do processo",
         "mTLS é TLS dos dois lados. O gateway prova que é o gateway e o orders prova que é o orders, com certificados. JWT continua provando o usuário. Um não substitui o outro.",
         "O momento 3 já existe no oráculo: `docs/tutoriais/03-mtls-grpc.md` e `infra/docker-compose.mtls.yml`. Você executa e quebra de propósito.",
         ["Leia o tutorial 03 inteiro antes de subir o overlay.",
          "Anote a diferença da tabela JWT versus certificado.",
          "Não apague a pasta `infra/certs`."],
         "Você explica as duas identidades com um exemplo cada.",
         "Desligar JWT porque 'agora tem mTLS' e deixar a API aberta para qualquer usuário na rede.",
         "docs/tutoriais/03-mtls-grpc.md",
         "A frase das duas identidades está no relatório.",
         ["Quem apresenta certificado: o browser ou o gateway?"],
         "[lab-03-quebrar-mtls.md](lab-03-quebrar-mtls.md)")

    lab(8, "lab-01-matriz", "Lab 8.1 — Executar a matriz", 70,
        "meta 8.1", "tabela rota × papel × status",
        """```mermaid
flowchart LR
  Sem[sem token] --> S401[401]
  User[USER] --> S403[403 no stock]
  Admin[ADMIN] --> S200[200 no stock]
```""",
        "Preencher a tabela da segurança com status reais.",
        ["Use Bruno ou curl. A coleção tem login, login-admin e os pedidos novos de 401."],
        ["Para cada linha de `docs/seguranca.md`, execute e escreva o status que voltou.",
         "Inclua notifications com e sem token.",
         "Na UI, esconda não é teste: chame o PUT como qa mesmo sem ver o menu."],
        ["O status da UI (menu oculto) e o status da API (403) contam histórias diferentes. Escreva as duas."],
        ["Rode `scripts/smoke.ps1`. Ele já cobre uma parte. A tabela completa continua manual nesta semana."],
        ["Não commite token no relatório. Status basta."],
        ".\\scripts\\smoke.ps1",
        "./scripts/smoke.sh",
        ["Token velho no Bruno e 401 falso.", "Testar stock sem Content-Type e anotar 415 como 403."],
        ["Olhe o corpo do 401. O gateway devolve JSON, não página HTML."],
        ["Qual linha da matriz o smoke ainda não cobre?"],
        "Tabela preenchida com status observados.",
        "Aprovado se 401, 403 e 200 do estoque estão corretos.",
        "[lab-02-keycloak.md](lab-02-keycloak.md)")

    lab(8, "lab-02-keycloak", "Lab 8.2 — Entrar pelo Keycloak", 80,
        "tutorial 02", "OIDC",
        """```mermaid
sequenceDiagram
  participant B as Browser
  participant K as Keycloak :11015
  participant G as gateway
  B->>K: login PKCE
  K-->>B: access token
  B->>G: API com Bearer
```""",
        "A mesma API de produtos aceita token do Keycloak quando o overlay está ligado.",
        ["Siga o tutorial 02 para subir o overlay. Não invente outro caminho.",
         "Volte ao modo local ao terminar, para os outros labs não quebrarem."],
        ["Abra a UI e use o botão Keycloak.",
         "Entre como qa.",
         "Abra um produto. A chamada tem Bearer.",
         "Decodifique o token e ache a role."],
        ["GET produtos com esse token retorna 200.",
         "PUT estoque com qa continua 403."],
        ["Não automatize OIDC nesta semana. Anote que o smoke padrão é do momento 1."],
        ["Pare o overlay e confirme que `/api/auth/login` voltou."],
        "# ver docs/tutoriais/02-oidc-keycloak.md",
        "# ver docs/tutoriais/02-oidc-keycloak.md",
        ["Esquecer de rebuild da web com VITE_AUTH_MODE=oidc e achar que o botão sumiu por bug do Keycloak.",
         "Bruno apontando para `/api/auth/login` durante o modo OIDC."],
        ["O tutorial diz como subir o compose com os dois arquivos `-f`."],
        ["O que mudou no `iss` do token em relação ao momento 1?"],
        "Frase comparando os dois `iss` e print do catálogo logado via Keycloak.",
        "Aprovado se produtos retornam 200 com token do Keycloak e você desligou o overlay no final.",
        "[lab-03-quebrar-mtls.md](lab-03-quebrar-mtls.md)")

    lab(8, "lab-03-quebrar-mtls", "Lab 8.3 — Quebrar a confiança do certificado", 80,
        "tutorial 03", "mTLS negativo",
        """```mermaid
flowchart LR
  Gw[gateway com cert] --> Ord[orders exige cliente]
  GwSem[gateway sem cert] --> Falha[gRPC falha]
  Falha --> Health[inventory-grpc DOWN ou 502]
```""",
        "Provar que sem certificado a chamada interna cai, e restaurar depois.",
        ["Siga o tutorial 03 ao pé da letra, inclusive a parte de restaurar.",
         "Não gere certificado novo se o de `infra/certs` já sobe."],
        ["Caminho feliz com mTLS: produtos 200 e health com gRPC UP.",
         "Quebre como o tutorial manda.",
         "Veja a falha.",
         "Restaure e veja 200 de novo."],
        ["JWT ainda é exigido na borda durante o teste feliz. mTLS não remove o 401.",
         "Anote os dois controles no relatório."],
        ["O validador `scripts/academy/validate-mtls.ps1` só checa se os arquivos do overlay existem no oráculo. A execução é sua."],
        ["Não commite chave privada nova. As de lab já estão versionadas de propósito."],
        "# ver docs/tutoriais/03-mtls-grpc.md",
        "# ver docs/tutoriais/03-mtls-grpc.md",
        ["Deixar o overlay quebrado e o próximo smoke falhar sem você lembrar.", "Apagar `ca.key`."],
        ["`openssl x509 -in infra/certs/orders.crt -noout -subject` mostra o nome do certificado."],
        ["mTLS substitui o login do qa?"],
        "Nota: feliz, quebrado, restaurado, com os status.",
        "Aprovado se você voltou ao estado em que o lab sobe de novo.",
        "[leitura-01-identidade.md](leitura-01-identidade.md)")

    leitura(8, "leitura-01-identidade", "Leitura 8 — Três provas diferentes", 35,
            "semana 8",
            "Não misturar usuário, provedor de login e serviço.",
            [("JWT local", "O próprio gateway emite e valida com segredo."),
             ("OIDC", "O Keycloak emite. O gateway confere a assinatura pela chave pública."),
             ("mTLS", "Certificado do processo na chamada gRPC. O usuário nem aparece nesse handshake.")],
            ["docs/seguranca.md", "https://oauth.net/2/pkce/"],
            ["Qual prova o browser apresenta?",
             "Qual prova o inventory exige no momento 3?"],
            "Semana 9.")

    diagrama(8, "diagrama-01-jwt-oidc-mtls", "Diagrama 8.1 — Três momentos",
             "quem prova o quê",
             """```mermaid
flowchart TB
  User[usuario qa] -->|JWT ou OIDC| Gw[api-gateway]
  Gw -->|mTLS| Ord[orders]
  Gw -->|mTLS| Inv[inventory]
```""",
             "A seta de cima identifica a pessoa. A de baixo identifica o processo.",
             "[diagrama-02-matriz.md](diagrama-02-matriz.md)")

    diagrama(8, "diagrama-02-matriz", "Diagrama 8.2 — 401, 403, 200",
             "estoque",
             """```mermaid
flowchart LR
  A[sem Authorization] --> R401[401]
  B[Bearer USER] --> R403[403 PUT stock]
  C[Bearer ADMIN] --> R200[200 PUT stock]
```""",
             "Produtos e pedidos aceitam USER. Stock não.",
             "Semana 9.")
