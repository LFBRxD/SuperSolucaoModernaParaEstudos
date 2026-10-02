# Checkpoints do espelho

O validador olha arquivos e o README. Ele não dá nota de estilo. `ACADEMY_PROJECT_DIR` aponta para a pasta do espelho.

| Id | O que prova, de forma grosseira |
|----|----------------------------------|
| `bootstrap` | Existem pom.xml e src/main/java no espelho. README cita a porta 11101. |
| `catalog-api` | GET de produtos documentado. Teste ou README mostra 200 e 404. |
| `orders-mongo` | URI do Mongo do espelho não é a porta 11008. Há coleção ou entidade de pedido. |
| `grpc-gateway` | Há arquivo .proto e mais de um processo descrito no README. |
| `kafka-events` | README ou código cita um tópico e eventType. |
| `saga` | Estados CONFIRMED e CANCELLED aparecem no README do espelho ou no código. |
| `scheduled-jobs` | Há Quartz ou dependência quartz e um @Scheduled. README explica a diferença. Há menção a idempotência do job. |
| `web-auth` | 401 e 403 documentados, ou filtro de segurança no código. |
| `observability` | README diz onde está o log ou o trace. |
| `automation-ci` | Há comando de teste no README (mvn test ou equivalente). |
| `platform` | Dockerfile ou compose do espelho, ou nota honesta de que ainda não há. |

```powershell
$env:ACADEMY_PROJECT_DIR = "E:\projetos\studyshop-do-zero"
.\scripts\academy\validate-checkpoint.ps1 -Checkpoint all
```

```bash
export ACADEMY_PROJECT_DIR=../studyshop-do-zero
./scripts/academy/validate-checkpoint.sh all
```
