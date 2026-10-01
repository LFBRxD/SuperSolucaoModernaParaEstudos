package com.studyshop.gateway.dto;

import java.util.List;

public class CreateOrderRequestDto {
    private List<CreateOrderItemDto> items;
    private boolean forcePaymentFailure;
    private String customerEmail;

    public List<CreateOrderItemDto> getItems() {
        return items;
    }

    public void setItems(List<CreateOrderItemDto> items) {
        this.items = items;
    }

    public boolean isForcePaymentFailure() {
        return forcePaymentFailure;
    }

    public void setForcePaymentFailure(boolean forcePaymentFailure) {
        this.forcePaymentFailure = forcePaymentFailure;
    }

    public String getCustomerEmail() {
        return customerEmail;
    }

    public void setCustomerEmail(String customerEmail) {
        this.customerEmail = customerEmail;
    }

    public static class CreateOrderItemDto {
        private String productId;
        private int quantity;

        public String getProductId() {
            return productId;
        }

        public void setProductId(String productId) {
            this.productId = productId;
        }

        public int getQuantity() {
            return quantity;
        }

        public void setQuantity(int quantity) {
            this.quantity = quantity;
        }
    }
}
