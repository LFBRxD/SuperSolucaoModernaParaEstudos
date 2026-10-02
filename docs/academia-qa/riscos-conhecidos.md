# Riscos conhecidos do oráculo

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
