package com.studyshop.inventory.events;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.studyshop.inventory.service.InventoryService;
import com.studyshop.inventory.service.InventoryService.ReservationItem;
import com.studyshop.inventory.service.InventoryService.ReservationResult;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Component;

@Component
public class OrderCreatedListener {

    public static final String INVENTORY_TOPIC = "inventory.events";
    private static final Logger log = LoggerFactory.getLogger(OrderCreatedListener.class);

    private final InventoryService inventoryService;
    private final KafkaTemplate<String, String> kafkaTemplate;
    private final ObjectMapper objectMapper;

    public OrderCreatedListener(
            InventoryService inventoryService,
            KafkaTemplate<String, String> kafkaTemplate,
            ObjectMapper objectMapper) {
        this.inventoryService = inventoryService;
        this.kafkaTemplate = kafkaTemplate;
        this.objectMapper = objectMapper;
    }

    @KafkaListener(topics = "orders.events", groupId = "inventory-service")
    public void onOrderEvent(String payload) {
        try {
            JsonNode node = objectMapper.readTree(payload);
            if (!"OrderCreated".equals(node.path("eventType").asText())) {
                return;
            }
            String orderId = node.path("orderId").asText();
            List<ReservationItem> items = new ArrayList<>();
            for (JsonNode item : node.path("items")) {
                items.add(new ReservationItem(item.path("productId").asText(), item.path("quantity").asInt()));
            }

            ReservationResult result = inventoryService.reserve(orderId, items);
            Map<String, Object> event;
            if (result.success()) {
                event = Map.of(
                        "eventType", "StockReserved",
                        "orderId", orderId,
                        "total", node.path("total").asDouble(),
                        "forcePaymentFailure", node.path("forcePaymentFailure").asBoolean(false),
                        "customerEmail", node.path("customerEmail").asText("")
                );
            } else {
                event = Map.of("eventType", "StockRejected", "orderId", orderId, "reason", result.reason());
            }

            String out = objectMapper.writeValueAsString(event);
            kafkaTemplate.send(INVENTORY_TOPIC, orderId, out);
            log.info("Published inventory event: {}", out);
        } catch (Exception e) {
            log.error("Failed to process order event: {}", payload, e);
        }
    }
}
