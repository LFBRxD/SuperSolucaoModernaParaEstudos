package com.studyshop.orders.events;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.studyshop.orders.domain.Order;
import com.studyshop.orders.domain.OrderRepository;
import com.studyshop.orders.domain.OrderStatus;
import com.studyshop.orders.service.OrderService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Component;

@Component
public class SagaEventListener {

    private static final Logger log = LoggerFactory.getLogger(SagaEventListener.class);

    private final OrderRepository orderRepository;
    private final OrderService orderService;
    private final ObjectMapper objectMapper;

    public SagaEventListener(OrderRepository orderRepository, OrderService orderService, ObjectMapper objectMapper) {
        this.orderRepository = orderRepository;
        this.orderService = orderService;
        this.objectMapper = objectMapper;
    }

    @KafkaListener(topics = "inventory.events", groupId = "orders-service")
    public void onInventoryEvent(String payload) {
        try {
            JsonNode node = objectMapper.readTree(payload);
            String type = node.path("eventType").asText();
            String orderId = node.path("orderId").asText();
            log.info("Inventory event type={} orderId={}", type, orderId);

            Order order = orderRepository.findById(orderId).orElse(null);
            if (order == null) {
                log.warn("Order not found: {}", orderId);
                return;
            }

            if ("StockReserved".equals(type)) {
                order.setStatus(OrderStatus.STOCK_RESERVED);
                order.setStatusReason("Estoque reservado");
                orderRepository.save(order);
                order.setStatus(OrderStatus.AWAITING_PAYMENT);
                order.setStatusReason("Aguardando pagamento");
                orderRepository.save(order);
            } else if ("StockRejected".equals(type)) {
                String reason = node.path("reason").asText("Estoque insuficiente");
                orderService.cancel(order, OrderStatus.STOCK_REJECTED, reason);
            }
        } catch (Exception e) {
            log.error("Failed to process inventory event: {}", payload, e);
        }
    }

    @KafkaListener(topics = "payments.events", groupId = "orders-service")
    public void onPaymentEvent(String payload) {
        try {
            JsonNode node = objectMapper.readTree(payload);
            String type = node.path("eventType").asText();
            String orderId = node.path("orderId").asText();
            log.info("Payment event type={} orderId={}", type, orderId);

            Order order = orderRepository.findById(orderId).orElse(null);
            if (order == null) {
                log.warn("Order not found: {}", orderId);
                return;
            }

            if ("PaymentApproved".equals(type)) {
                order.setStatus(OrderStatus.PAYMENT_APPROVED);
                order.setStatusReason("Pagamento aprovado");
                orderRepository.save(order);
                orderService.confirm(order);
            } else if ("PaymentFailed".equals(type)) {
                String reason = node.path("reason").asText("Pagamento recusado");
                orderService.cancel(order, OrderStatus.PAYMENT_FAILED, reason);
            }
        } catch (Exception e) {
            log.error("Failed to process payment event: {}", payload, e);
        }
    }
}
