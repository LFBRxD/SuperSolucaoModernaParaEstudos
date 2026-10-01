package com.studyshop.orders.events;

import java.util.List;

public record OrderCreatedEvent(
        String eventType,
        String orderId,
        String customerEmail,
        double total,
        boolean forcePaymentFailure,
        List<OrderItemEvent> items
) {
    public static final String TYPE = "OrderCreated";

    public record OrderItemEvent(String productId, String productName, int quantity, double unitPrice) {
    }
}
