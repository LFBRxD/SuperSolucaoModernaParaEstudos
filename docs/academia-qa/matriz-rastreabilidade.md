# Matriz de rastreabilidade

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
