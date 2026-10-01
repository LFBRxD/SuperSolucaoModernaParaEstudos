package com.studyshop.orders.events;

public record OrderStatusChangedEvent(
        String eventType,
        String orderId,
        String status,
        String reason,
        String customerEmail
) {
    public static final String CONFIRMED = "OrderConfirmed";
    public static final String CANCELLED = "OrderCancelled";
}
