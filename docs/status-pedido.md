# Status do pedido

Fluxo da saga (Kafka):

```
CREATED
  -> AWAITING_STOCK
       -> STOCK_RESERVED -> AWAITING_PAYMENT
            -> PAYMENT_APPROVED -> CONFIRMED
            -> PAYMENT_FAILED   -> CANCELLED
       -> STOCK_REJECTED -> CANCELLED
```

Eventos:
- `orders.events`: OrderCreated, OrderConfirmed, OrderCancelled
- `inventory.events`: StockReserved, StockRejected
- `payments.events`: PaymentApproved, PaymentFailed

Falhas injetáveis (QA):
- Header `X-Force-Payment-Failure: true` ou body `forcePaymentFailure: true`
- Estoque baixo via Admin (`/admin/stock`) ou produto `prod-raro`
