package com.studyshop.payments.events;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.studyshop.payments.domain.Payment;
import com.studyshop.payments.domain.PaymentRepository;
import java.util.Map;
import java.util.UUID;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Component;

@Component
public class StockReservedListener {

    public static final String PAYMENTS_TOPIC = "payments.events";
    private static final Logger log = LoggerFactory.getLogger(StockReservedListener.class);

    private final PaymentRepository paymentRepository;
    private final KafkaTemplate<String, String> kafkaTemplate;
    private final ObjectMapper objectMapper;

    public StockReservedListener(
            PaymentRepository paymentRepository,
            KafkaTemplate<String, String> kafkaTemplate,
            ObjectMapper objectMapper) {
        this.paymentRepository = paymentRepository;
        this.kafkaTemplate = kafkaTemplate;
        this.objectMapper = objectMapper;
    }

    @KafkaListener(topics = "inventory.events", groupId = "payments-service")
    public void onInventoryEvent(String payload) {
        try {
            JsonNode node = objectMapper.readTree(payload);
            if (!"StockReserved".equals(node.path("eventType").asText())) {
                return;
            }

            String orderId = node.path("orderId").asText();
            double total = node.path("total").asDouble();
            boolean forceFailure = node.path("forcePaymentFailure").asBoolean(false);

            Payment payment = new Payment();
            payment.setId(UUID.randomUUID().toString());
            payment.setOrderId(orderId);
            payment.setAmount(total);

            Map<String, Object> event;
            if (forceFailure) {
                payment.setStatus("FAILED");
                payment.setReason("Falha injetada via forcePaymentFailure (cenário QA)");
                event = Map.of(
                        "eventType", "PaymentFailed",
                        "orderId", orderId,
                        "paymentId", payment.getId(),
                        "reason", payment.getReason()
                );
            } else {
                payment.setStatus("APPROVED");
                payment.setReason("Pagamento aprovado");
                event = Map.of(
                        "eventType", "PaymentApproved",
                        "orderId", orderId,
                        "paymentId", payment.getId(),
                        "amount", total
                );
            }

            paymentRepository.save(payment);
            String out = objectMapper.writeValueAsString(event);
            kafkaTemplate.send(PAYMENTS_TOPIC, orderId, out);
            log.info("Published payment event: {}", out);
        } catch (Exception e) {
            log.error("Failed to process inventory event: {}", payload, e);
        }
    }
}
