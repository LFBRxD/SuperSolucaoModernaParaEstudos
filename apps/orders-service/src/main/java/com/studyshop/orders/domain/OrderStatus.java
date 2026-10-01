package com.studyshop.orders.domain;

public enum OrderStatus {
    CREATED,
    AWAITING_STOCK,
    STOCK_RESERVED,
    STOCK_REJECTED,
    AWAITING_PAYMENT,
    PAYMENT_APPROVED,
    PAYMENT_FAILED,
    CONFIRMED,
    CANCELLED
}
