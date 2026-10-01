package com.studyshop.orders.service;

import com.studyshop.orders.domain.Order;
import com.studyshop.orders.domain.OrderItem;
import com.studyshop.orders.domain.OrderRepository;
import com.studyshop.orders.domain.OrderStatus;
import com.studyshop.orders.events.OrderCreatedEvent;
import com.studyshop.orders.events.OrderEventPublisher;
import com.studyshop.orders.events.OrderStatusChangedEvent;
import java.util.List;
import java.util.UUID;
import org.springframework.stereotype.Service;

@Service
public class OrderService {

    private final OrderRepository orderRepository;
    private final OrderEventPublisher eventPublisher;

    public OrderService(OrderRepository orderRepository, OrderEventPublisher eventPublisher) {
        this.orderRepository = orderRepository;
        this.eventPublisher = eventPublisher;
    }

    public Order create(List<OrderItem> items, String customerEmail, boolean forcePaymentFailure) {
        if (items == null || items.isEmpty()) {
            throw new IllegalArgumentException("Pedido deve conter ao menos um item");
        }

        Order order = new Order();
        order.setId(UUID.randomUUID().toString());
        order.setItems(items);
        order.setCustomerEmail(customerEmail == null || customerEmail.isBlank() ? "aluno@studyshop.local" : customerEmail);
        order.setForcePaymentFailure(forcePaymentFailure);
        order.setTotal(items.stream().mapToDouble(i -> i.getUnitPrice() * i.getQuantity()).sum());
        order.setStatus(OrderStatus.CREATED);
        order.setStatusReason("Pedido criado");
        orderRepository.save(order);

        order.setStatus(OrderStatus.AWAITING_STOCK);
        order.setStatusReason("Aguardando reserva de estoque");
        orderRepository.save(order);

        List<OrderCreatedEvent.OrderItemEvent> eventItems = items.stream()
                .map(i -> new OrderCreatedEvent.OrderItemEvent(
                        i.getProductId(), i.getProductName(), i.getQuantity(), i.getUnitPrice()))
                .toList();

        eventPublisher.publish(order.getId(), new OrderCreatedEvent(
                OrderCreatedEvent.TYPE,
                order.getId(),
                order.getCustomerEmail(),
                order.getTotal(),
                order.isForcePaymentFailure(),
                eventItems
        ));

        return order;
    }

    public Order get(String orderId) {
        return orderRepository.findById(orderId)
                .orElseThrow(() -> new IllegalArgumentException("Pedido não encontrado: " + orderId));
    }

    public List<Order> list(String status) {
        if (status == null || status.isBlank()) {
            return orderRepository.findAll();
        }
        return orderRepository.findByStatus(OrderStatus.valueOf(status.toUpperCase()));
    }

    public void confirm(Order order) {
        order.setStatus(OrderStatus.CONFIRMED);
        order.setStatusReason("Pedido confirmado");
        orderRepository.save(order);
        eventPublisher.publish(order.getId(), new OrderStatusChangedEvent(
                OrderStatusChangedEvent.CONFIRMED,
                order.getId(),
                order.getStatus().name(),
                order.getStatusReason(),
                order.getCustomerEmail()
        ));
    }

    public void cancel(Order order, OrderStatus intermediateStatus, String reason) {
        order.setStatus(intermediateStatus);
        order.setStatusReason(reason);
        orderRepository.save(order);
        order.setStatus(OrderStatus.CANCELLED);
        order.setStatusReason(reason);
        orderRepository.save(order);
        eventPublisher.publish(order.getId(), new OrderStatusChangedEvent(
                OrderStatusChangedEvent.CANCELLED,
                order.getId(),
                order.getStatus().name(),
                reason,
                order.getCustomerEmail()
        ));
    }
}
