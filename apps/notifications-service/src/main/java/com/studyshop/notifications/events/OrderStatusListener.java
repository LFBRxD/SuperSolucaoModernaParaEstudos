package com.studyshop.notifications.events;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.studyshop.notifications.domain.Notification;
import com.studyshop.notifications.domain.NotificationRepository;
import java.util.UUID;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Component;

@Component
public class OrderStatusListener {

    private static final Logger log = LoggerFactory.getLogger(OrderStatusListener.class);

    private final NotificationRepository notificationRepository;
    private final ObjectMapper objectMapper;

    public OrderStatusListener(NotificationRepository notificationRepository, ObjectMapper objectMapper) {
        this.notificationRepository = notificationRepository;
        this.objectMapper = objectMapper;
    }

    @KafkaListener(topics = "orders.events", groupId = "notifications-service")
    public void onOrderEvent(String payload) {
        try {
            JsonNode node = objectMapper.readTree(payload);
            String type = node.path("eventType").asText();
            if (!"OrderConfirmed".equals(type) && !"OrderCancelled".equals(type)) {
                return;
            }

            Notification notification = new Notification();
            notification.setId(UUID.randomUUID().toString());
            notification.setOrderId(node.path("orderId").asText());
            notification.setType(type);
            notification.setRecipient(node.path("customerEmail").asText("aluno@studyshop.local"));
            notification.setMessage("OrderConfirmed".equals(type)
                    ? "Seu pedido foi confirmado com sucesso."
                    : "Seu pedido foi cancelado: " + node.path("reason").asText());
            notificationRepository.save(notification);
            log.info("Notification saved: type={} orderId={} to={}",
                    type, notification.getOrderId(), notification.getRecipient());
        } catch (Exception e) {
            log.error("Failed to process order event: {}", payload, e);
        }
    }
}
