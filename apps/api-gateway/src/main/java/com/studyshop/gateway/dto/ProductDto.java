package com.studyshop.gateway.dto;

public record ProductDto(
        String productId,
        String sku,
        String name,
        String description,
        double price,
        int quantity
) {
}
