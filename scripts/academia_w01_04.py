# -*- coding: utf-8 -*-
from academia_render import meta, lab, leitura, diagrama

def build():
    # ---------- SEMANA 1 ----------
    meta(1, "meta-01-o-que-e-o-laboratorio", "Meta 1.1 — O que é este laboratório", 60,
         "nenhum", "conhecer o sistema antes de operar",
         "O StudyShop é um e-commerce de estudo. Não é uma loja real. Ele existe para você ver, quebrar e reconstruir as peças que um QA encontra em sistemas distribuídos: site, API, banco, mensagens, segurança e telas de diagnóstico.",
         "Você vai usar a solução pronta como prova dos nove. O projeto que você criar do zero (pasta irmã `studyshop-do-zero`) tem que chegar a um comportamento parecido. Se você só clicar na tela pronta, não aprende a construir.",
         ["Abra o README na raiz do repositório e anote as portas que começam em 11000.",
          "Abra `docs/arquitetura.md` e copie, com suas palavras, a lista de serviços.",
          "Abra `docs/glossario.md` e marque três palavras que você ainda não sabe explicar."],
         "Uma lista sua com: nome do serviço, porta, e uma frase do que ele faz. Sem copiar a tabela inteira do README.",
         "Achar que precisa entender Kafka hoje. Nesta semana Kafka só existe no mapa. Você ainda não precisa consumir mensagem.",
         "README do repositório e https://docs.docker.com/get-started/overview/ (só a ideia de container).",
         "Você consegue apontar, sem abrir o README, quem fala HTTP com o browser e quem guarda o catálogo.",
         ["Qual serviço o browser chama primeiro?", "O que é o oráculo neste curso?", "Onde ficará o seu projeto do zero?"],
         "[lab-01-subir-a-stack.md](lab-01-subir-a-stack.md)")

    meta(1, "meta-02-processo-porta-e-http", "Meta 1.2 — Processo, porta e HTTP", 70,
         "meta 1.1", "uma requisição HTTP",
         "Um processo é um programa em execução. Uma porta é o número da porta de entrada desse processo na máquina (ou no container). HTTP é o texto do pedido e da resposta: método (`GET`, `POST`), caminho (`/api/health`), cabeçalhos e corpo.",
         "Quase todo bug de 'não abre' neste lab é porta errada, processo morto ou HTTP 401 porque faltou o token. Se você não distingue isso, vai culpar o código.",
         ["No PowerShell: `curl.exe -i http://localhost:11001/api/health`.",
          "Leia a primeira linha da resposta (código HTTP) e o corpo JSON.",
          "Repita com a porta 11000 e anote que a resposta é HTML, não JSON."],
         "Status HTTP 200 no health e um JSON com `overall`. Na porta 11000, HTML da web.",
         "Usar `curl` do PowerShell sem `.exe` pode ser um alias que esconde o código HTTP. Prefira `curl.exe -i`.",
         "https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Overview",
         "Você explica a diferença entre porta 11000 e 11001 sem olhar a tabela.",
         ["O que é um código 200?", "Por que health e a página web não são a mesma porta?"],
         "[lab-02-health-web-e-api.md](lab-02-health-web-e-api.md)")

    meta(1, "meta-03-container-e-compose", "Meta 1.3 — Container e Docker Compose", 75,
         "meta 1.2", "vários processos sob o Compose",
         "Um container é um processo isolado com seu próprio sistema de arquivos e sua própria rede. O Docker Compose sobe vários containers a partir de um arquivo `infra/docker-compose.yml`. O nome `localhost` dentro de um container não é o seu Windows.",
         "Os serviços se acham por nome (`kafka`, `mongodb`), não por `localhost`. Quando um log diz 'connection refused' em `localhost:11009` dentro do container, o endereço está errado para aquele mundo.",
         ["Abra `infra/docker-compose.yml` e encontre o serviço `api-gateway`.",
          "Anote a porta publicada (`11001:11001`) e uma variável `ORDERS_GRPC_ADDRESS`.",
          "Rode `docker compose ps` dentro de `infra` e veja a coluna STATUS."],
         "Serviços com status running ou healthy. A porta da esquerda é a do seu computador; a da direita é a de dentro do container.",
         "Rodar `docker compose` fora da pasta `infra` e o Docker não achar o arquivo. Entre na pasta ou use `-f`.",
         "https://docs.docker.com/compose/intro/features-uses/",
         "Você aponta um `depends_on` e diz qual serviço espera o outro.",
         ["Por que o gateway usa `orders-service:11003` e não `localhost:11003`?"],
         "[diagrama-01-stack-e-portas.md](diagrama-01-stack-e-portas.md)")

    meta(1, "meta-04-health-agregado", "Meta 1.4 — Health agregado", 60,
         "meta 1.3", "saber se o sistema está no ar",
         "Health é uma resposta curta que diz se o processo consegue trabalhar. O gateway junta o health de orders, inventory, payments, notifications e ainda pergunta o gRPC do estoque. O campo `overall` só fica `UP` se as partes importantes responderem.",
         "Antes de testar pedido, você prova que a base está viva. Um pedido que falha com a stack caída não ensina saga.",
         ["Abra http://localhost:11000/health (pode pedir login em algumas rotas; health da API é público).",
          "Chame `GET http://localhost:11001/api/health` sem token.",
          "Compare a lista de serviços com o Compose."],
         "`overall` igual a `UP` e cada serviço listado como `UP`, incluindo `inventory-grpc`.",
         "Subir o Compose e testar em 5 segundos. Java ainda está iniciando. Espere e repita.",
         "https://docs.spring.io/spring-boot/reference/actuator/endpoints.html",
         "Você sabe qual URL é pública e qual tela da web mostra o mesmo dado.",
         ["Health 200 prova que um pedido vai confirmar?", "Não. Por quê?"],
         "[lab-03-devtools.md](lab-03-devtools.md)")

    meta(1, "meta-05-devtools", "Meta 1.5 — DevTools do navegador", 70,
         "meta 1.4", "ver a request que a tela fez",
         "O DevTools é o inspetor do navegador. A aba Network mostra cada pedido HTTP: URL, método, status, cabeçalhos e corpo. A aba Application mostra o que ficou gravado no navegador (neste lab, o token em localStorage).",
         "A tela pode mentir por cache ou por estado velho. A aba Network mostra o que realmente foi para o gateway.",
         ["Abra http://localhost:11000, F12, aba Network, marque Preserve log.",
          "Faça login `qa` / `qa123`.",
          "Clique no pedido `login` e leia o status e o JSON (não copie o token para lugar público)."],
         "Um POST `/api/auth/login` com 200 e, nas chamadas seguintes, o cabeçalho `Authorization: Bearer ...`.",
         "Filtrar só por Img e achar que a API não foi chamada. Filtre por Fetch/XHR.",
         "https://developer.chrome.com/docs/devtools/network",
         "Você acha o login na Network e diz se a próxima chamada de produtos levou o token.",
         ["Onde o browser guarda o token neste lab?", "O que acontece se você apagar o localStorage e atualizar a página?"],
         "[lab-04-desenhar-o-caminho.md](lab-04-desenhar-o-caminho.md)")

    lab(1, "lab-01-subir-a-stack", "Lab 1.1 — Subir a stack e ler o status", 80,
        "metas 1.1 a 1.3", "Compose no ar",
        """```mermaid
flowchart LR
  Voce[Voce] --> Script["scripts/up.ps1"]
  Script --> Compose["infra/docker-compose.yml"]
  Compose --> Mongo[mongodb]
  Compose --> Kafka[kafka]
  Compose --> Apps[servicos Java e web]
```""",
        "Subir o laboratório e saber se cada container está de pé antes de testar regra de negócio.",
        ["Não escreva código nesta sessão. O 'implementar' aqui é operar o ambiente que já existe.",
         "Leia o início de `scripts/up.ps1` e veja que ele entra em `infra` e chama `docker compose up -d --build`."],
        ["No PowerShell, na raiz do repo: `.\\scripts\\up.ps1`.",
         "Espere o comando terminar. Depois: `cd infra; docker compose ps`.",
         "Anote containers que não estão `running` ou `healthy`."],
        ["Confira se `api-gateway` publica 11001 e `web` publica 11000.",
         "Abra dois logs: `docker compose logs --tail=30 api-gateway` e `orders-service`.",
         "Procure a linha de Tomcat/Netty dizendo que a porta subiu. Se não achar, o processo ainda não escutou."],
        ["O atalho já existe: `scripts/up.ps1` e `scripts/up.sh`.",
         "Nesta semana você não cria teste novo. Você anota o comando que vai repetir amanhã."],
        ["Se um serviço falhar sempre no mesmo ponto, copie as últimas 40 linhas do log para o seu relatório.",
         "Não 'otimize' o Compose ainda. Primeiro ele precisa subir igual para todo mundo."],
        "cd E:\\projetos\\SuperSolucaoModernaParaEstudos\n.\\scripts\\up.ps1\ncd infra\ndocker compose ps",
        "cd /mnt/e/projetos/SuperSolucaoModernaParaEstudos\n./scripts/up.sh\ncd infra\ndocker compose ps",
        ["Docker Desktop parado.", "Porta 11001 ocupada por outro projeto.", "Build Maven falhou e a imagem não foi criada."],
        ["`docker compose logs --tail=80 <nome-do-servico>`", "No Windows, `netstat -ano | findstr 11001` mostra quem segurou a porta."],
        ["Qual container precisa estar healthy antes do orders-service, segundo o Compose?"],
        "Print ou texto de `docker compose ps` no relatório da semana.",
        "Aprovado se todos os serviços do Compose estão running/healthy e você nomeia um log que leu.",
        "[lab-02-health-web-e-api.md](lab-02-health-web-e-api.md)")

    lab(1, "lab-02-health-web-e-api", "Lab 1.2 — Health na web e na API", 70,
        "lab 1.1", "health UP",
        """```mermaid
flowchart LR
  Browser[Browser :11000] --> Web[web]
  Web --> Gw[api-gateway :11001]
  Gw --> Ord[orders actuator]
  Gw --> Inv[inventory actuator]
  Gw --> Pay[payments actuator]
  Gw --> Notif[notifications actuator]
  Gw --> Grpc[inventory gRPC health]
```""",
        "Provar que o health agregado está UP pela tela e pelo HTTP, sem token.",
        ["Nada de código. Você executa o que o gateway já faz em `HealthController`."],
        ["Abra http://localhost:11000/health e clique em atualizar.",
         "No PowerShell: `curl.exe -s http://localhost:11001/api/health`.",
         "Confira os nomes: api-gateway, orders-service, inventory-service, payments-service, notifications-service, inventory-grpc."],
        ["Se um serviço está DOWN, abra o log dele antes de reiniciar tudo.",
         "Health público não pede `Authorization`. Se você recebeu 401, a URL não é `/api/health`."],
        ["O smoke já cobre este passo: `.\\scripts\\smoke.ps1` (ele também faz login; se falhar no health, pare aqui).",
         "Guarde o JSON do health no relatório."],
        ["Anote quanto tempo o health levou para ficar UP depois do `up`. Esse número vira timeout de CI mais tarde."],
        "curl.exe -s http://localhost:11001/api/health",
        "curl -s http://localhost:11001/api/health | jq",
        ["Testar `/health` no gateway em vez de `/api/health`.", "Achar que a página web na porta 11001 existe. A web é 11000."],
        ["Swagger também existe: http://localhost:11001/swagger-ui.html"],
        ["Por que `inventory-grpc` aparece separado de `inventory-service`?"],
        "JSON do health com `overall` UP colado no relatório.",
        "Aprovado se os seis nomes esperados estão UP.",
        "[lab-03-devtools.md](lab-03-devtools.md)")

    lab(1, "lab-03-devtools", "Lab 1.3 — Seguir o login no DevTools", 75,
        "meta 1.5", "Network do login",
        """```mermaid
sequenceDiagram
  participant B as Browser
  participant W as web :11000
  participant G as api-gateway :11001
  B->>W: GET /
  B->>W: POST /api/auth/login
  W->>G: POST /api/auth/login
  G-->>B: 200 accessToken
```""",
        "Ver com os próprios olhos o login e o token nas chamadas seguintes.",
        ["Não altere o frontend. Observe."],
        ["F12, Network, Preserve log, limpe a lista.",
         "Login `qa` / `qa123`.",
         "Abra o POST de login. Status 200. Veja que a resposta tem `accessToken` e `roles`.",
         "Abra Application, Local Storage, e ache a chave do token (não publique o valor)."],
        ["Navegue ao catálogo. A chamada `/api/products` deve ir com Bearer.",
         "Se a chamada de produtos foi para `localhost:11000/api/...`, o proxy da web encaminhou ao gateway. Isso é esperado."],
        ["Anote método, caminho e status. Isso vira o primeiro teste Playwright na semana 10.",
         "Ainda não escreva o teste."],
        ["Saia (`btn-logout`) e entre como `admin`. Veja se o menu Estoque aparece (`nav-admin-stock`)."],
        "# navegador\n# http://localhost:11000/login",
        "# navegador\n# http://localhost:11000/login",
        ["Olhar a chamada e não rolar até Request Headers.", "Achar 401 em produtos porque o login foi na UI errada (OIDC vs local)."],
        ["Se o botão diz Keycloak, a stack subiu no modo OIDC. Volte ao Compose padrão ou siga o tutorial 02 mais tarde."],
        ["O token prova o usuário ou o serviço?"],
        "Três linhas: status do login, se produtos levou Bearer, se admin vê o menu Estoque.",
        "Aprovado se as três linhas estão corretas.",
        "[lab-04-desenhar-o-caminho.md](lab-04-desenhar-o-caminho.md)")

    lab(1, "lab-04-desenhar-o-caminho", "Lab 1.4 — Desenhar o caminho da web até o gateway", 70,
        "labs anteriores da semana", "mapa que você mesmo desenha",
        """```mermaid
flowchart LR
  Browser --> Web
  Web --> Gateway
  Gateway --> Orders
  Gateway --> Inventory
```""",
        "Fechar a semana desenhando o caminho sem copiar o diagrama pronto.",
        ["Abra um editor de texto vazio. Não abra `docs/arquitetura.md` nos primeiros 15 minutos."],
        ["Liste o que você clicou hoje e a URL que apareceu.",
         "Desenhe caixas: browser, web, gateway. Ligue com setas e escreva a porta."],
        ["Agora abra o diagrama da arquitetura e marque em vermelho o que você esqueceu (Kafka, Mongo, observabilidade).",
         "Não se cobre de Kafka ainda. Só registre que ele existe e que não foi usado nesta semana."],
        ["Salve o desenho em Mermaid no seu relatório. Um bloco de 8 linhas basta."],
        ["Acrescente uma nota: o que você testaria amanhã se o health estivesse DOWN."],
        "# sem comando obrigatorio\n# opcional: Start-Process http://localhost:11000",
        "# sem comando obrigatorio",
        ["Desenhar tudo que você leu, sem ter visto. O desenho desta semana é só o que você operou."],
        ["Modelo mínimo: Browser -->|HTTP| web:11000 --> gateway:11001"],
        ["Qual caixa você não consegue explicar ainda?"],
        "Um Mermaid seu no relatório da semana 1.",
        "Aprovado se o desenho tem portas e você lista uma dúvida honesta.",
        "[leitura-01-http-e-compose.md](leitura-01-http-e-compose.md)")

    leitura(1, "leitura-01-http-e-compose", "Leitura 1 — HTTP e Compose, só o que o lab usa", 50,
            "fechar a semana 1",
            "Você já operou. Esta leitura dá nome ao que você viu, para a semana 2 não começar no escuro.",
            [("HTTP", "Método diz a intenção. `GET` lê. `POST` cria. `PUT` substitui. O status diz o resultado: 200 ok, 401 não autenticado, 403 autenticado porém sem permissão, 404 não achei, 500 o servidor quebrou. Cabeçalho `Authorization` carrega o token. Corpo JSON carrega os dados."),
             ("Compose", "O arquivo declara serviços, imagens, portas, variáveis e volumes. `up -d` sobe em segundo plano. `ps` lista. `logs` mostra a saída do processo. `down` para. `down -v` apaga também os dados do Mongo."),
             ("O que ainda não é sua função", "Não decore gRPC nem Kafka nesta leitura. Só saiba que o gateway esconde esses detalhes da tela.")],
            ["https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status",
             "https://docs.docker.com/compose/intro/compose-application-model/"],
            ["Qual status você espera sem token em `/api/products`? Você ainda não testou; chute e anote para a semana 8.",
             "O que `down -v` apaga que `down` não apaga?"],
            "Semana 2, [meta-01-jvm-e-maven.md](../semana-02/meta-01-jvm-e-maven.md)")

    diagrama(1, "diagrama-01-stack-e-portas", "Diagrama 1.1 — Stack e portas",
             "portas do host",
             """```mermaid
flowchart TB
  subgraph host [Seu computador]
    Web["web :11000"]
    Gw["api-gateway :11001"]
    Ord["orders :11002 HTTP :11003 gRPC"]
    Inv["inventory :11004 HTTP :11005 gRPC"]
    Pay["payments :11006"]
    Noti["notifications :11007"]
    Mongo["mongodb :11008"]
    Kafka["kafka :11009"]
    Graf["grafana :11010"]
    Jaeger["jaeger :11011"]
    Prom["prometheus :11012"]
    Kui["kafka-ui :11016"]
  end
  Web --> Gw
  Gw --> Ord
  Gw --> Inv
  Gw --> Noti
```""",
             "A porta da esquerda na publicação Docker é a que você digita no browser. Kafka UI entra na semana 5; a porta 11016 já fica reservada.",
             "[diagrama-02-health.md](diagrama-02-health.md)")

    diagrama(1, "diagrama-02-health", "Diagrama 1.2 — Health agregado",
             "quem o gateway consulta",
             """```mermaid
sequenceDiagram
  participant Q as QA
  participant G as api-gateway
  participant O as orders
  participant I as inventory
  participant P as payments
  participant N as notifications
  Q->>G: GET /api/health
  G->>O: actuator/health
  G->>I: actuator/health e gRPC health
  G->>P: actuator/health
  G->>N: actuator/health
  G-->>Q: overall UP ou não
```""",
             "Uma seta falha e o overall deixa de ser UP. Anote qual seta quebrou quando isso acontecer.",
             "Semana 2.")

    # ---------- SEMANA 2 ----------
    meta(2, "meta-01-jvm-e-maven", "Meta 2.1 — JVM e Maven", 70,
         "semana 1 concluída", "como um projeto Java nasce",
         "A JVM executa bytecode Java. O Maven compila, baixa bibliotecas e empacota um jar. O arquivo `pom.xml` é a lista de ingredientes. `mvn package` produz o jar. Sem isso, não existe serviço Spring.",
         "Na semana 2 você cria o projeto espelho do zero. O oráculo já tem um `pom.xml` na raiz. O seu projeto começa menor: um único módulo.",
         ["Na raiz do oráculo, abra `pom.xml` e leia `java.version` e a lista de `<module>`.",
          "Rode `java -version` e `mvn -version` no terminal. Se faltar, instale JDK 21 e Maven antes de continuar.",
          "Não rode o build completo ainda se a stack Docker já está no ar; só confirme as versões."],
         "Java 21 e Maven reconhecidos pelo terminal.",
         "Ter só o JRE e não o JDK: compila nada. `javac` precisa existir.",
         "https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html",
         "Você diz, com suas palavras, o que o `pom.xml` declara.",
         ["O que é um módulo Maven neste repo?", "Por que o projeto do zero começa com um módulo só?"],
         "[meta-02-spring-boot.md](meta-02-spring-boot.md)")

    meta(2, "meta-02-spring-boot", "Meta 2.2 — O que o Spring Boot sobe", 70,
         "meta 2.1", "a aplicação que escuta HTTP",
         "Spring Boot sobe um servidor HTTP (Tomcat) e registra seus controllers. A classe com `@SpringBootApplication` é o começo. Uma porta em `application.yml` (`server.port`) é onde ele escuta.",
         "Quando você não sabe 'onde o programa começa', qualquer erro vira mágica. O começo é a classe `main` e o `application.yml`.",
         ["No oráculo, ache `ApiGatewayApplication.java` e a porta em `apps/api-gateway/src/main/resources/application.yml`.",
          "Anote `server.port`.",
          "Não copie essa classe para o projeto espelho. Só reconheça o formato."],
         "Você encontra a classe `main` e o número da porta no YAML.",
         "Procurar a porta só no Compose e ignorar o YAML. Os dois precisam concordar.",
         "https://spring.io/guides/gs/spring-boot",
         "Você aponta o arquivo que liga a porta 11001 no gateway do oráculo.",
         ["O que acontece se o YAML diz 8080 e o Compose publica 11001:11001?"],
         "[meta-03-controller.md](meta-03-controller.md)")

    meta(2, "meta-03-controller", "Meta 2.3 — Controller, serviço e repositório", 75,
         "meta 2.2", "caminho dentro do processo",
         "Controller recebe HTTP e devolve HTTP. Serviço aplica regra. Repositório fala com o banco. Nesta semana o repositório pode ser uma lista em memória. O banco entra na semana 3.",
         "Se tudo fica no controller, o teste vira um teste de HTTP para uma regra que deveria ser uma função. Separar agora evita reescrever depois.",
         ["No oráculo, abra `ApiController.java` e veja que ele chama clientes gRPC, não o Mongo direto.",
          "No seu projeto espelho, planeje três classes: `ProductController`, `ProductService`, `ProductRepository` em memória.",
          "Escreva no papel os campos de um produto: id, nome, preço, quantidade."],
         "Um desenho de três caixas com uma seta HTTP só na primeira.",
         "Colocar regra de estoque dentro do controller 'porque é pequeno'. O lab pede a separação mesmo assim.",
         "https://spring.io/guides/gs/rest-service",
         "Você descreve quem pode conhecer HTTP e quem não pode.",
         ["O controller deve saber o formato do Mongo?", "Não nesta semana. Por quê?"],
         "[lab-01-criar-o-projeto.md](lab-01-criar-o-projeto.md)")

    meta(2, "meta-04-erro-http", "Meta 2.4 — Erro HTTP de propósito", 60,
         "meta 2.3", "404 e 400 que você controla",
         "Um erro bom diz o que faltou sem despejar stack trace no cliente. Produto inexistente vira 404. Quantidade negativa vira 400. Erro inesperado vira 500 e deve aparecer no log, não como texto cru na API se você tratar.",
         "QA vive de casos negativos. Se a API só tem caminho feliz, você não tem o que assertar.",
         ["Defina dois casos no papel: id que não existe; quantidade menor que zero.",
          "Escreva o status esperado ao lado de cada caso.",
          "No oráculo, um produto inexistente no gateway tende a virar erro gRPC mapeado. Você ainda não precisa reproduzir gRPC."],
         "Tabela de três linhas: caso, status, corpo mínimo (`message` ou vazio documentado).",
         "Devolver 200 com `{ \"error\": true }`. Isso esconde a falha de quem automatiza pelo status.",
         "https://datatracker.ietf.org/doc/html/rfc9110#name-status-codes",
         "Sua API de catálogo em memória tem pelo menos um 404 testado à mão.",
         ["400 e 404 respondem problemas diferentes. Qual é qual?"],
         "[lab-02-endpoint-catalogo.md](lab-02-endpoint-catalogo.md)")

    meta(2, "meta-05-teste-junit", "Meta 2.5 — O primeiro teste automatizado", 70,
         "meta 2.4", "repetir o que a mão já viu",
         "JUnit roda métodos de teste. `spring-boot-starter-test` sobe o suficiente para chamar o controller sem Docker. Assert é a frase 'o status tem que ser 200' escrita em código.",
         "Automatizar antes de ver com a mão gera teste que você não sabe depurar. Você já vai ter visto o curl. O teste só congela esse curl.",
         ["Escreva em português o assert: GET /api/products devolve 200 e uma lista não vazia.",
          "Só depois procure `@SpringBootTest` ou `MockMvc` no guia do Spring.",
          "Um teste. Não uma suíte."],
         "Um teste verde no `mvn test` do projeto espelho.",
         "Teste que sobe Mongo sem você ter Mongo. Nesta semana o repositório é memória, então o teste não precisa de Docker.",
         "https://docs.spring.io/spring-boot/reference/testing/spring-boot-applications.html",
         "`mvn test` passa e você sabe qual request ele faz.",
         ["O que o teste não cobre ainda? (resposta esperada: banco, gRPC, Kafka)"],
         "[lab-03-ver-no-swagger.md](lab-03-ver-no-swagger.md)")

    lab(2, "lab-01-criar-o-projeto", "Lab 2.1 — Criar o projeto espelho vazio", 90,
        "metas 2.1 e 2.2", "pasta irmã studyshop-do-zero",
        """```mermaid
flowchart LR
  Oraculo[StudyShop oraculo] -. compara comportamento .-> Espelho[studyshop-do-zero]
  Espelho --> Pom[pom.xml]
  Espelho --> Main[classe main]
  Espelho --> Yml[application.yml porta 11101]
```""",
        "Ter um Spring Boot que sobe sozinho, numa porta que não briga com o oráculo (11101).",
        ["Crie a pasta `../studyshop-do-zero` ao lado deste repo, não dentro dele.",
         "Use https://start.spring.io com Maven, Java 21, dependências Spring Web e Validation.",
         "Em `application.yml`, `server.port: 11101`.",
         "Rode `mvn spring-boot:run` e pare com Ctrl+C depois de ver a porta."],
        ["`curl.exe -i http://localhost:11101/api/products` pode dar 404. Isso é sucesso desta sessão: o processo escuta e ainda não tem rota.",
         "Confirme que o oráculo na 11001 continua no ar, se você o deixou ligado."],
        ["Anote no README do espelho: porta, comando de subir, e a frase 'ainda não há catálogo'.",
         "Não copie controllers do oráculo."],
        ["Ainda não há teste. O critério automático desta sessão é o processo subir.",
         "O validador `bootstrap` em `scripts/academy` olha se existem `pom.xml` e `src/main/java`."],
        ["Escolha um nome de pacote estável, por exemplo `com.studyshop.catalog`. Mudar depois quebra import."],
        "cd ..\\studyshop-do-zero\nmvn spring-boot:run",
        "cd ../studyshop-do-zero\nmvn spring-boot:run",
        ["Criar o projeto dentro do oráculo e misturar os poms.", "Usar a porta 11001 e derrubar o gateway sem perceber."],
        ["start.spring.io já gera a classe main. Não escreva o main na mão na primeira vez."],
        ["Por que a porta do espelho não é 11001?"],
        "README do espelho com o comando e a porta. Saída do validador bootstrap.",
        "Aprovado se a aplicação sobe na 11101 e o oráculo, se estiver ligado, continua na 11001.",
        "[lab-02-endpoint-catalogo.md](lab-02-endpoint-catalogo.md)")

    lab(2, "lab-02-endpoint-catalogo", "Lab 2.2 — API de catálogo em memória", 90,
        "lab 2.1", "GET e GET por id",
        """```mermaid
sequenceDiagram
  participant C as curl
  participant K as ProductController
  participant S as ProductService
  participant R as Lista em memoria
  C->>K: GET /api/products
  K->>S: listar
  S->>R: listar
  R-->>C: JSON
```""",
        "Devolver pelo menos dois produtos fixos e 404 para id desconhecido.",
        ["Crie os três tipos: controller, service, repositório em memória com dois produtos (`p-1`, `p-2`).",
         "GET `/api/products` e GET `/api/products/{id}`.",
         "Id ausente: 404 com JSON `message`."],
        ["Suba o espelho. `curl.exe http://localhost:11101/api/products`.",
         "Chame um id que existe e um que não existe.",
         "Anote os três status."],
        ["Reinicie o processo e chame de novo. A lista volta igual, porque está no código, não no disco. Escreva isso no relatório: ainda não há persistência.",
         "Não envolva o gateway do oráculo. Este lab é o processo novo sozinho."],
        ["Escreva um teste MockMvc: lista 200 e id `nao-existe` 404.",
         "`mvn test` verde."],
        ["Acrescente validação: se você criar POST depois, quantidade negativa é 400. Se não houver POST, documente que o catálogo é só leitura nesta semana."],
        "curl.exe -i http://localhost:11101/api/products\ncurl.exe -i http://localhost:11101/api/products/nao-existe",
        "curl -i http://localhost:11101/api/products\ncurl -i http://localhost:11101/api/products/nao-existe",
        ["404 do Spring em HTML porque faltou tratar a exceção. Force um `@ControllerAdvice` ou `ResponseStatusException`.",
         "Esquecer `@RestController` e receber corpo vazio."],
        ["`ResponseStatusException(HttpStatus.NOT_FOUND, \"produto nao encontrado\")` resolve o 404 sem framework extra."],
        ["O que se perde quando você reinicia o processo?"],
        "Teste verde e os três curls anotados.",
        "Aprovado se 200, 200 por id e 404 estão vistos à mão e no JUnit.",
        "[lab-03-ver-no-swagger.md](lab-03-ver-no-swagger.md)")

    lab(2, "lab-03-ver-no-swagger", "Lab 2.3 — Ver o contrato no Swagger do oráculo", 60,
        "lab 2.2", "comparar o seu contrato com o oráculo",
        """```mermaid
flowchart LR
  Espelho["seu GET /api/products :11101"] --> Compara[comparar campos]
  Oraculo["oraculo GET /api/products :11001"] --> Compara
```""",
        "Entender o que o catálogo do oráculo devolve a mais que o seu.",
        ["Não copie o DTO. Liste diferenças."],
        ["Abra http://localhost:11001/swagger-ui.html no oráculo.",
         "Faça login no Swagger (Authorize com Bearer) ou use o curl autenticado da semana 8 se o Swagger pedir token.",
         "Anote campos de produto: id, nome, preço, estoque. Compare com os seus."],
        ["Escreva uma tabela: campo no oráculo, campo no espelho, igual ou ausente.",
         "Se o seu nomeou `id` e o oráculo `productId`, isso é decisão. Documente. O validador de comportamento aceita os dois se você declarar o mapa no README."],
        ["O teste do espelho continua valendo para o seu contrato. Não quebre o teste para imitar nome de campo sem atualizar o assert."],
        ["Decida se vai alinhar os nomes agora ou na semana 4. Escreva a decisão."],
        "curl.exe -s http://localhost:11001/api/health",
        "curl -s http://localhost:11001/api/health",
        ["Chamar `/api/products` do oráculo sem token e achar que a API está quebrada. Ela exige login. Health não exige."],
        ["O tutorial `docs/tutoriais/01-jwt-local.md` mostra o login. Você aprofunda isso na semana 8; hoje basta um token para olhar o JSON."],
        ["Qual campo seu está com outro nome?"],
        "Tabela de campos no relatório.",
        "Aprovado se a tabela existe e o teste do espelho segue verde.",
        "[leitura-01-spring.md](leitura-01-spring.md)")

    leitura(2, "leitura-01-spring", "Leitura 2 — Spring Boot só até o primeiro REST", 45,
            "depois dos labs da semana 2",
            "Fixar o vocabulário que você acabou de usar no projeto espelho.",
            [("Stereotypes", "`@RestController` marca a classe HTTP. `@Service` marca a regra. `@Repository` marca o acesso a dados. São anotações. O Spring cria os objetos e liga um no outro (injeção)."),
             ("Configuração", "`application.yml` guarda porta, URL de banco e flags. O que muda entre máquinas fica aqui, não espalhado no Java."),
             ("Teste de fatia", "MockMvc chama o controller sem abrir porta de verdade. Serve para status e JSON. Não serve para provar Docker.")],
            ["https://spring.io/guides/gs/rest-service",
             "https://docs.spring.io/spring-boot/reference/testing/spring-boot-applications.html"],
            ["Quem pode lançar 404: o controller ou o repositório?",
             "Por que o teste desta semana não sobe Kafka?"],
            "Semana 3.")

    diagrama(2, "diagrama-01-ciclo-maven", "Diagrama 2.1 — Do código ao processo",
             "build",
             """```mermaid
flowchart LR
  Src[src/main/java] --> Mvn["mvn package"]
  Mvn --> Jar[jar]
  Jar --> Java["java -jar ou spring-boot:run"]
  Java --> Porta["porta 11101"]
```""",
             "Se o curl falha com connection refused, o processo não está na porta. Se falha com 404, o processo está no ar e a rota não existe.",
             "[diagrama-02-antes-depois.md](diagrama-02-antes-depois.md)")

    diagrama(2, "diagrama-02-antes-depois", "Diagrama 2.2 — Espelho vazio e com catálogo",
             "checkpoint catalog-api",
             """```mermaid
flowchart TB
  subgraph antes [Antes do lab 2.2]
    A1[processo na 11101]
    A2[sem rota de produtos]
  end
  subgraph depois [Depois do lab 2.2]
    B1[GET /api/products 200]
    B2[GET id ausente 404]
    B3[teste MockMvc verde]
  end
  antes --> depois
```""",
             "Este é o primeiro antes/depois do projeto espelho. Os próximos checkpoints seguem o mesmo desenho.",
             "Semana 3.")

    # ---------- SEMANA 3 ----------
    meta(3, "meta-01-documento-mongodb", "Meta 3.1 — Documento e coleção", 70,
         "semana 2", "dado que sobrevive ao restart",
         "MongoDB guarda documentos JSON em coleções. Não há tabela rígida como em SQL, mas o seu código precisa de um formato estável. No oráculo, cada serviço tem um database: `orders`, `inventory`, `payments`, `notifications`, todos no mesmo servidor (porta 11008 no host).",
         "A lista em memória da semana 2 morre quando o processo cai. Pedido de verdade precisa continuar lá depois do restart. QA precisa olhar o banco para ver se a API mentiu.",
         ["Com a stack no ar: `docker compose exec mongodb mongosh --eval \"show dbs\"` a partir de `infra`.",
          "Entre no database `inventory` e rode `db.products.find().limit(2)` ou `db.product.find()` se o nome da coleção vier no plural da entidade.",
          "Anote um produto seed: id e quantidade."],
         "Pelo menos um documento de produto com quantidade numérica.",
         "O nome da coleção pode ser `product` (classe) e não `products`. Se `find` voltar vazio, rode `show collections`.",
         "https://www.mongodb.com/docs/manual/core/document/",
         "Você mostra um documento real, não o JSON da API.",
         ["Qual a diferença entre o JSON da API e o documento no Mongo?"],
         "[lab-01-mongosh.md](lab-01-mongosh.md)")

    meta(3, "meta-02-seed-e-estado", "Meta 3.2 — Seed e estado do lab", 60,
         "meta 3.1", "dados iniciais conhecidos",
         "Seed é a carga inicial. O inventory cria cinco produtos na primeira subida, entre eles `prod-mouse` e `prod-raro` (estoque baixo). Sem seed, o catálogo abre vazio e os cenários de QA não têm massa.",
         "Teste que depende de 'o que estava ontem' falha no dia seguinte. Você precisa saber resetar.",
         ["Leia `docs/cenarios-qa.md` cenário 2 e liste os cinco ids.",
          "Veja no Mongo se `prod-raro` tem quantidade 1.",
          "Leia o que `scripts/down.ps1 -Volumes` faz: apaga o volume e o seed roda de novo na próxima subida."],
         "Os cinco ids no banco ou na API autenticada.",
         "Resetar volume no meio de um teste e achar que o estoque 'voltou sozinho' por bug.",
         "Código `SeedConfig` do inventory no oráculo.",
         "Você explica como voltar ao estoque inicial de propósito.",
         ["Quando você NÃO deve apagar o volume?"],
         "[meta-03-equivalencia.md](meta-03-equivalencia.md)")

    meta(3, "meta-03-equivalencia", "Meta 3.3 — Classes de equivalência e limites", 70,
         "meta 3.2", "escolher poucos testes que representam muitos",
         "Classe de equivalência é um grupo de entradas que o sistema trata igual. Limite é a borda: estoque 1 com quantidade 1 passa; quantidade 2 não. Testar 3, 4 e 5 não ensina mais se a regra é 'maior que o estoque'.",
         "`prod-raro` existe para o limite. Quantidade 2 é o caso de estoque insuficiente. Quantidade 1 é o feliz. Zero e negativo são inválidos se a API validar.",
         ["Escreva uma tabela: quantidade 1, 2, 0, -1 para `prod-raro`.",
          "Marque o resultado que você espera (ainda pode chutar o 0 e o -1).",
          "Não dispare os pedidos da saga ainda; isso é semana 6. Aqui o foco é o desenho dos casos."],
         "Tabela com quatro linhas e uma coluna 'já executei? não'.",
         "Testar só o caminho feliz e achar que cobriu o estoque.",
         "https://en.wikipedia.org/wiki/Equivalence_partitioning",
         "A tabela existe no relatório antes de você automatizar.",
         ["Por que quantidade 3 no `prod-raro` não é um caso novo se 2 já rejeita?"],
         "[lab-02-persistir-no-espello.md](lab-02-persistir-no-espello.md)")

    meta(3, "meta-04-isolamento", "Meta 3.4 — Isolar a massa de teste", 60,
         "meta 3.3", "um teste não suja o outro",
         "Isolamento significa que o teste N começa de um estado conhecido, não do lixo do teste N-1. No lab, ou você reseta o volume, ou você usa dados que o teste cria e apaga, ou você aceita que o estoque só cai (o oráculo não devolve estoque se o pagamento falha — isso é um risco conhecido).",
         "Sem isolamento, o smoke fica verde na segunda-feira e vermelho na terça porque o mouse acabou.",
         ["Leia o risco em `docs/academia-qa/riscos-conhecidos.md` quando ele existir, ou em `docs/cenarios-qa.md` cenário 4: estoque não volta após falha de pagamento.",
          "No espelho, decida: cada teste sobe um Mongo descartável ou limpa a coleção no `@BeforeEach`.",
          "Escreva a decisão em uma frase."],
         "Uma frase de estratégia de limpeza no README do espelho.",
         "Apagar o database de produção por engano. Neste curso só existe lab local. Mesmo assim, o comando de reset fica no script, não num `drop` solto sem nome do database.",
         "https://www.mongodb.com/docs/manual/reference/method/db.collection.deleteMany/",
         "Você aponta como o próximo teste encontra o estoque previsível.",
         ["O oráculo compensa estoque hoje? Não. O que isso muda no seu teste?"],
         "[lab-03-teste-com-mongo.md](lab-03-teste-com-mongo.md)")

    lab(3, "lab-01-mongosh", "Lab 3.1 — Inspecionar o Mongo do oráculo", 80,
        "meta 3.1", "mongosh",
        """```mermaid
flowchart LR
  API["GET /api/products"] --> Gw[api-gateway]
  Gw --> Inv[inventory-service]
  Inv --> Col["coleção no database inventory"]
  QA[mongosh] --> Col
```""",
        "Ver o mesmo produto pela API e pelo banco.",
        ["Não altere documentos nesta sessão. Só leitura."],
        ["`cd infra` e `docker compose exec mongodb mongosh --eval \"show dbs\"`.",
         "`docker compose exec mongodb mongosh inventory --eval \"show collections\"`.",
         "Faça `find` limitado a 5 e copie um documento para o relatório (sem senha; não há senha neste lab)."],
        ["Faça login na API e `GET /api/products`.",
         "Confira se o id e a quantidade batem com o documento.",
         "Se a quantidade divergir, você está olhando outra coleção ou outro ambiente."],
        ["Anote o comando mongosh no seu caderno. Ele volta na semana 6 para ver o pedido.",
         "Não automatize mongosh ainda."],
        ["Escreva o que um QA não deve fazer: update manual para 'fazer o teste passar' sem registrar."],
        "cd infra\ndocker compose exec mongodb mongosh inventory --eval \"show collections\"",
        "cd infra\ndocker compose exec mongodb mongosh inventory --eval 'show collections'",
        ["PowerShell come as aspas. Use aspas simples no bash e aspas escapadas no PowerShell, como no exemplo.",
         "Conectar em `localhost:27017` em vez de `11008` a partir do host."],
        ["Do host, se tiver mongosh instalado: `mongosh mongodb://localhost:11008/inventory`."],
        ["A API e o documento precisam ter a mesma quantidade. Se não tiverem, qual dos dois você acredita primeiro e por quê?"],
        "Um documento colado e o JSON correspondente da API.",
        "Aprovado se os dois lados mostram o mesmo id e a mesma quantidade.",
        "[lab-02-persistir-no-espello.md](lab-02-persistir-no-espello.md)")

    lab(3, "lab-02-persistir-no-espello", "Lab 3.2 — Trocar a lista em memória por Mongo", 90,
        "lab 2.2 e meta 3.1", "persistência no projeto espelho",
        """```mermaid
flowchart LR
  subgraph antes [Semana 2]
    Mem[lista na RAM]
  end
  subgraph depois [Semana 3]
    MongoE["Mongo do espelho"]
  end
  antes --> depois
```""",
        "Reiniciar o processo do espelho e ainda ver os produtos.",
        ["Suba um Mongo só do espelho na porta 11108 para não usar o volume do oráculo: `docker run --name espelho-mongo -p 11108:27017 -d mongo:7`.",
         "Adicione Spring Data MongoDB no `pom.xml` e a URI `mongodb://localhost:11108/catalog`.",
         "Grave dois produtos na subida se a coleção estiver vazia.",
         "GET continua igual para o cliente."],
        ["Crie ou liste. Pare o Java. Suba de novo. GET de novo. Os produtos continuam.",
         "Abra `mongosh mongodb://localhost:11108/catalog` e dê `find`."],
        ["O teste de API e o documento contam a mesma quantidade de itens.",
         "Não aponte o espelho para `localhost:11008`. Esse é o oráculo."],
        ["Atualize o teste: ou sobe com Testcontainers, ou usa um perfil que limpa a coleção. Se Testcontainers for pesado demais nesta semana, documente um `@BeforeEach` que apaga a coleção num Mongo local de teste.",
         "`mvn test` verde."],
        ["Anote o tempo de subida. Se passar de um minuto, você vai sentir isso no CI."],
        "docker run --name espelho-mongo -p 11108:27017 -d mongo:7\ncurl.exe -s http://localhost:11101/api/products",
        "docker run --name espelho-mongo -p 11108:27017 -d mongo:7\ncurl -s http://localhost:11101/api/products",
        ["URI sem nome do database.", "Esquecer de parar o container e achar que os dados sumiram por bug da API."],
        ["`spring.data.mongodb.uri` no YAML do espelho."],
        ["O que mudou no JSON público em relação à semana 2?"],
        "Print do find depois de reiniciar o Java.",
        "Aprovado se o dado sobrevive ao restart e o teste verde não depende do Mongo do oráculo.",
        "[lab-03-teste-com-mongo.md](lab-03-teste-com-mongo.md)")

    lab(3, "lab-03-teste-com-mongo", "Lab 3.3 — Teste de integração do catálogo", 80,
        "lab 3.2", "teste que olha API e efeito no banco",
        """```mermaid
sequenceDiagram
  participant T as JUnit
  participant API as catalogo
  participant DB as Mongo de teste
  T->>API: GET /api/products
  API->>DB: find
  DB-->>T: documentos
```""",
        "Um teste que falha se o repositório não grava.",
        ["Escreva o teste que sobe o contexto Spring e chama GET.",
         "Se a lista vier vazia, o seed do teste não rodou: falhe com mensagem clara."],
        ["Rode `mvn test` e leia o relatório surefire se falhar.",
         "Rode o mesmo GET com curl contra o processo manual, para não confundir porta de teste com porta 11101."],
        ["O teste não pode usar a porta 11008.",
         "Depois do teste, a coleção de teste está limpa ou o database de teste é outro."],
        ["O comando único é `mvn test`. Coloque-o no README."],
        ["Se o teste ficar lento, meça. Não paralelize ainda."],
        "mvn test",
        "mvn test",
        ["Teste verde porque leu a lista em memória antiga e você esqueceu de remover o repositório da semana 2.",
         "Dois beans de repositório e o Spring não sabe qual usar."],
        ["Apague a implementação em memória ou marque uma delas com `@Profile`."],
        ["O teste prova persistência ou só o JSON?"],
        "Saída de `mvn test` verde no relatório.",
        "Aprovado se o teste quebra quando você aponta para um Mongo vazio sem seed.",
        "[leitura-01-mongodb.md](leitura-01-mongodb.md)")

    leitura(3, "leitura-01-mongodb", "Leitura 3 — MongoDB para quem testa API", 40,
            "semana 3",
            "Você já viu um documento. A leitura evita confundir coleção, database e o JSON da API.",
            [("Database e coleção", "O servidor tem databases. Cada database tem coleções. Cada coleção tem documentos. No oráculo o servidor é um só e os databases separam os serviços. Um serviço não deve ler o database do outro."),
             ("O que o QA confere", "Id, quantidade, status do pedido, e-mail. Não precisa virar administrador de índice nesta semana."),
             ("Cuidado", "Atualizar documento na mão muda o que a API mostra e esconde bug. Use só para investigar e desfaça ou resete.")],
            ["https://www.mongodb.com/docs/manual/core/databases-and-collections/",
             "https://www.mongodb.com/docs/mongodb-shell/"],
            ["Por que orders e inventory não compartilham a mesma coleção?",
             "O que `down -v` faz com o seed?"],
            "Semana 4.")

    diagrama(3, "diagrama-01-documento", "Diagrama 3.1 — API, serviço e documento",
             "write path do catálogo",
             """```mermaid
flowchart LR
  Http[HTTP JSON] --> Svc[inventory ou catalogo]
  Svc --> Doc[documento Mongo]
  Doc --> Svc
  Svc --> Http
```""",
             "O formato do documento pode ter campos a mais (`_id`). O JSON público é uma escolha do controller.",
             "[diagrama-02-isolamento.md](diagrama-02-isolamento.md)")

    diagrama(3, "diagrama-02-isolamento", "Diagrama 3.2 — Dois Mongos",
             "não misturar oráculo e espelho",
             """```mermaid
flowchart TB
  Oraculo[apps do oraculo] --> P11008["Mongo host 11008"]
  Espelho[catalogo do espelho] --> P11108["Mongo host 11108"]
```""",
             "Seta cruzada é bug de configuração. Se o espelho gravar no 11008, você contaminou o lab.",
             "Semana 4.")

    # ---------- SEMANA 4 ----------
    meta(4, "meta-01-protobuf", "Meta 4.1 — O que é um .proto", 70,
         "semana 3", "contrato entre processos",
         "Protobuf é um formato de contrato. O arquivo `.proto` descreve mensagens e métodos. O compilador gera código Java. Quem chama e quem atende precisam usar o mesmo contrato, senão a chamada nem deserializa.",
         "No oráculo, o browser não fala protobuf. O gateway traduz REST para gRPC. O contrato está em `libs/proto/src/main/proto/`.",
         ["Abra `inventory.proto` e `orders.proto`.",
          "Anote um método de cada (`ListProducts` ou equivalente, `CreateOrder`).",
          "Não gere código ainda. Só leia os nomes dos campos."],
         "Uma lista de métodos RPC que você consegue ler em voz alta.",
         "Achar que o JSON do Swagger é o contrato interno. Ele é o contrato da borda. O `.proto` é o contrato entre gateway e serviço.",
         "https://protobuf.dev/getting-started/javatutorial/",
         "Você aponta o arquivo .proto de estoque sem procurar mais de um minuto.",
         ["Quem edita o .proto: o frontend ou o time dos dois serviços?"],
         "[meta-02-grpc.md](meta-02-grpc.md)")

    meta(4, "meta-02-grpc", "Meta 4.2 — Chamada gRPC", 70,
         "meta 4.1", "RPC com deadline e status",
         "gRPC é uma chamada de função pela rede. O cliente tem um stub (objeto gerado). O servidor implementa o método. Status não é HTTP: `NOT_FOUND`, `INVALID_ARGUMENT`, `DEADLINE_EXCEEDED`, `UNAVAILABLE`. O gateway transforma isso em 404, 400, 504, 502.",
         "Quando a tela mostra 502, o browser não chegou no estoque. O gateway não conseguiu completar a chamada interna. Você precisa saber em qual trecho olhar.",
         ["No oráculo, ache `GrpcClients.java` e veja os endereços.",
          "No Compose, confirme `ORDERS_GRPC_ADDRESS` e `INVENTORY_GRPC_ADDRESS`.",
          "Leia um método do `ApiController` que chama o stub."],
         "Você descreve: HTTP entra no gateway, gRPC sai para o inventory.",
         "Tratar 502 como 'estoque vazio'. 502 é falha de chamar o serviço, não regra de negócio.",
         "https://grpc.io/docs/what-is-grpc/core-concepts/",
         "Você diferencia 404 de produto e 502 de serviço caído.",
         ["O que é deadline?", "O que o cliente deve fazer se o prazo estoura?"],
         "[lab-01-ler-o-proto.md](lab-01-ler-o-proto.md)")

    meta(4, "meta-03-gateway", "Meta 4.3 — Por que existe gateway", 60,
         "meta 4.2", "uma porta HTTP para o QA",
         "O gateway é a única porta HTTP de negócio para a tela e para o Bruno. Ele autentica, junta dados e traduz erros. Os serviços de orders e inventory não precisam conhecer o browser.",
         "Teste de UI sempre passa por ele. Teste do proto pode passar direto no gRPC, mas isso é outro contrato. Não misture as falhas.",
         ["Liste as rotas em `docs/seguranca.md`.",
          "Marque quais o gateway atende sozinho (login, health) e quais ele repassa.",
          "Notificações são HTTP por trás, não gRPC. Anote essa exceção."],
         "Tabela rota → destino (gRPC orders, gRPC inventory, HTTP notifications, local).",
         "Chamar orders na porta 11002 e achar que é a API do produto. 11002 é actuator/HTTP interno, não o contrato do Bruno.",
         "https://grpc.io/docs/guides/",
         "Você explica por que o Bruno aponta para 11001 e não para 11003.",
         ["O que quebra se o gateway cai e os outros serviços continuam de pé?"],
         "[lab-02-separar-servicos.md](lab-02-separar-servicos.md)")

    meta(4, "meta-04-mapeamento-de-erro", "Meta 4.4 — Mapear status gRPC para HTTP", 65,
         "meta 4.3", "o QA vê HTTP, a causa pode ser gRPC",
         "Uma tabela de mapeamento evita discussão. `NOT_FOUND` → 404. `INVALID_ARGUMENT` → 400. `UNAVAILABLE` → 502. `DEADLINE_EXCEEDED` → 504. O corpo deve dizer qual serviço falhou, senão você só vê 'erro'.",
         "No espelho você vai separar catálogo e um segundo processo. Sem essa tabela, o teste de contrato fica instável.",
         ["Escreva a tabela acima no README do espelho antes de codar.",
          "No oráculo, force um caso: pare o inventory (`docker compose stop inventory-service`) e chame produtos autenticado. Anote o HTTP. Suba de novo.",
          "Não deixe o serviço parado."],
         "Um status anotado com o inventory parado, e a stack saudável de novo no final.",
         "Esquecer de `docker compose start inventory-service` e achar que 'o lab quebrou' no dia seguinte.",
         "https://grpc.io/docs/guides/status-codes/",
         "A tabela está escrita e você viu pelo menos um erro de verdade.",
         ["504 e 502. Qual sugere timeout e qual sugere serviço inalcançável?"],
         "[lab-03-contrato.md](lab-03-contrato.md)")

    lab(4, "lab-01-ler-o-proto", "Lab 4.1 — Ler o contrato e achar o método na chamada", 70,
        "metas 4.1 e 4.2", "proto do oráculo",
        """```mermaid
flowchart LR
  Proto["libs/proto/*.proto"] --> Gerado[classes geradas]
  Gerado --> Stub[stub no gateway]
  Gerado --> Impl[serviço inventory ou orders]
```""",
        "Ligar um campo do `.proto` a um campo do JSON público.",
        ["Não altere o proto do oráculo nesta sessão."],
        ["Abra `inventory.proto`. Escolha um campo de produto.",
         "Ache o mesmo conceito no JSON de `GET /api/products` (com token).",
         "Escreva: nome no proto, nome no JSON, igual ou traduzido."],
        ["Se os nomes diferem, o lugar da tradução é o gateway ou o mapper. Procure no `ApiController` ou DTO.",
         "Anote o arquivo."],
        ["Não gere teste ainda. A evidência é a tabela de três colunas."],
        ["Se quiser, instale `grpcurl` depois. Não é obrigatório para passar."],
        "cd infra\ndocker compose ps inventory-service",
        "cd infra && docker compose ps inventory-service",
        ["Editar o proto 'para aprender' e quebrar o build do time.", "Comparar com a API sem token e anotar 401 como se fosse o formato do produto."],
        ["Login está em `docs/tutoriais/01-jwt-local.md`."],
        ["Quem traduz o nome do campo?"],
        "Tabela proto × JSON × arquivo de tradução.",
        "Aprovado se a tabela cita arquivo real do repositório.",
        "[lab-02-separar-servicos.md](lab-02-separar-servicos.md)")

    lab(4, "lab-02-separar-servicos", "Lab 4.2 — Dois processos no espelho", 100,
        "lab 3.2", "catálogo gRPC e um gateway mínimo",
        """```mermaid
sequenceDiagram
  participant C as curl :11101
  participant G as gateway espelho
  participant I as inventory espelho gRPC :11105
  C->>G: GET /api/products
  G->>I: RPC listar
  I-->>G: mensagens
  G-->>C: JSON
```""",
        "O curl continua na porta do gateway. O catálogo deixa de ser o processo que você chamava direto, ou você documenta uma fase intermediária com os dois.",
        ["Crie um segundo módulo ou segundo projeto `inventory` com gRPC na porta 11105.",
         "Mova a leitura dos produtos para lá.",
         "O processo da 11101 só encaminha.",
         "Comece pelo guia oficial de gRPC Java. Não copie o módulo `libs/proto` inteiro; um proto com um método basta."],
        ["Suba os dois processos. Curl no gateway.",
         "Pare só o inventory. Curl de novo. Anote 502 ou equivalente.",
         "Suba o inventory. Curl volta a 200."],
        ["Log dos dois processos no momento do 200.",
         "O Mongo do catálogo continua o da 11108, atrás do inventory, não atrás do gateway."],
        ["Teste de contrato: gateway devolve 200 quando o inventory está no ar. Pode ser teste manual scriptado em `scripts/check-catalog.sh` dentro do espelho.",
         "Um assert automático que sobe os dois é ótimo; se não conseguir nesta semana, entregue o script e marque a dívida no README."],
        ["Acrescente deadline de 2 segundos no stub. Documente o que acontece se o inventory dorme."],
        "# dois terminais no espelho\n# inventory gRPC 11105\n# gateway 11101",
        "# dois terminais no espelho",
        ["Gateway falar com `localhost:11005` (oráculo) em vez de `11105`.",
         "Esquecer de gerar as classes do proto e importar pacote que não existe."],
        ["Plugin `protobuf-maven-plugin` no pom do módulo proto pequeno. O oráculo tem um exemplo em `libs/proto/pom.xml` — leia, não copie o arquivo inteiro."],
        ["Com o inventory parado, o status é regra de negócio ou falha de rede?"],
        "Notas dos dois curls (no ar e parado) e o proto novo no espelho.",
        "Aprovado se o 200 depende do segundo processo e você provou isso parando-o.",
        "[lab-03-contrato.md](lab-03-contrato.md)")

    lab(4, "lab-03-contrato", "Lab 4.3 — Automatizar o contrato mínimo", 70,
        "lab 4.2", "teste repetível do gateway",
        """```mermaid
flowchart LR
  Teste[script ou JUnit] --> Gw[gateway :11101]
  Gw --> Inv[inventory :11105]
```""",
        "Um comando só que falha se a lista não voltar.",
        ["Escreva o teste ou o script que faz GET e exige status 200 e pelo menos um item.",
         "Mensagem de falha deve dizer a porta e o corpo recebido."],
        ["Rode o comando duas vezes. O resultado é o mesmo.",
         "Rode com o inventory parado e veja a falha falhar pelo motivo certo."],
        ["O comando não chama a porta 11001.",
         "Documente a ordem de subir: Mongo, inventory, gateway, teste."],
        ["Coloque o comando no README do espelho como 'contrato do catálogo'."],
        ["Se o teste levar mais que 10 segundos sem Testcontainers, explique o porquê."],
        "mvn test",
        "mvn test",
        ["Assert só no tamanho da lista e ignorar 500 com corpo HTML.", "Hardcode de porta sem documentar."],
        ["Imprima `status` e os primeiros 200 caracteres do corpo quando falhar."],
        ["O que este teste ainda não prova? (saga, auth, estoque)"],
        "Comando único no README e uma execução verde.",
        "Aprovado se a falha com inventory parado é óbvia na mensagem.",
        "[leitura-01-grpc.md](leitura-01-grpc.md)")

    leitura(4, "leitura-01-grpc", "Leitura 4 — gRPC em uma página", 40,
            "semana 4",
            "Dar nome a stub, status e deadline depois de você ter visto a chamada quebrar.",
            [("Stub", "Classe gerada que parece um método local e esconde o socket."),
             ("Status", "O erro semântico do RPC. O gateway é quem decide o HTTP."),
             ("Deadline", "Tempo máximo que o cliente espera. Sem deadline, uma chamada presa segura a thread do gateway.")],
            ["https://grpc.io/docs/what-is-grpc/core-concepts/",
             "https://grpc.io/docs/guides/status-codes/"],
            ["Por que o browser não chama gRPC neste lab?",
             "Qual status gRPC você mapearia para HTTP 404?"],
            "Semana 5.")

    diagrama(4, "diagrama-01-rest-grpc", "Diagrama 4.1 — REST na borda, gRPC por dentro",
             "uma request de catálogo",
             """```mermaid
sequenceDiagram
  participant B as Browser ou Bruno
  participant G as api-gateway
  participant I as inventory-service
  B->>G: HTTP GET /api/products
  G->>I: gRPC
  I-->>G: Product
  G-->>B: JSON
```""",
             "Se o HTTP nem sai do browser, o problema é a web. Se o HTTP chega e o gRPC não, o problema é o endereço do stub.",
             "[diagrama-02-erros.md](diagrama-02-erros.md)")

    diagrama(4, "diagrama-02-erros", "Diagrama 4.2 — Onde o erro nasce",
             "mapa de falhas da chamada síncrona",
             """```mermaid
flowchart TB
  A[sem token] --> H401[HTTP 401]
  B[produto ausente] --> H404[HTTP 404]
  C[inventory parado] --> H502[HTTP 502]
  D[deadline estourou] --> H504[HTTP 504]
```""",
             "Cada caixa da esquerda é uma causa diferente. Não as trate como 'deu erro'.",
             "Semana 5.")
