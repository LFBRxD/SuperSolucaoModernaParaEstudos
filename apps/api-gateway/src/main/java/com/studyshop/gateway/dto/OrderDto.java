package com.studyshop.gateway.dto;

import java.util.List;

public record OrderDto(
        String orderId,
        String status,
        double total,
        String customerEmail,
        boolean forcePaymentFailure,
        String createdAt,
        String updatedAt,
        String statusReason,
        List<OrderItemDto> items
) {
    public record OrderItemDto(String productId, String productName, int quantity, double unitPrice) {
    }
}
