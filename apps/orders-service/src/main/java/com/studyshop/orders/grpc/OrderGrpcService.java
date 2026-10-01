package com.studyshop.orders.grpc;

import com.studyshop.orders.domain.Order;
import com.studyshop.orders.domain.OrderItem;
import com.studyshop.orders.service.OrderService;
import com.studyshop.proto.orders.CreateOrderRequest;
import com.studyshop.proto.orders.GetOrderRequest;
import com.studyshop.proto.orders.ListOrdersRequest;
import com.studyshop.proto.orders.ListOrdersResponse;
import com.studyshop.proto.orders.OrderResponse;
import com.studyshop.proto.orders.OrderServiceGrpc;
import io.grpc.Status;
import io.grpc.stub.StreamObserver;
import java.util.List;
import net.devh.boot.grpc.server.service.GrpcService;

@GrpcService
public class OrderGrpcService extends OrderServiceGrpc.OrderServiceImplBase {

    private final OrderService orderService;

    public OrderGrpcService(OrderService orderService) {
        this.orderService = orderService;
    }

    @Override
    public void createOrder(CreateOrderRequest request, StreamObserver<OrderResponse> responseObserver) {
        try {
            List<OrderItem> items = request.getItemsList().stream()
                    .map(i -> new OrderItem(
                            i.getProductId(),
                            i.getProductName(),
                            i.getQuantity(),
                            i.getUnitPrice()))
                    .toList();
            Order order = orderService.create(items, request.getCustomerEmail(), request.getForcePaymentFailure());
            responseObserver.onNext(toResponse(order));
            responseObserver.onCompleted();
        } catch (IllegalArgumentException e) {
            responseObserver.onError(Status.INVALID_ARGUMENT.withDescription(e.getMessage()).asRuntimeException());
        } catch (Exception e) {
            responseObserver.onError(Status.INTERNAL.withDescription(e.getMessage()).asRuntimeException());
        }
    }

    @Override
    public void getOrder(GetOrderRequest request, StreamObserver<OrderResponse> responseObserver) {
        try {
            Order order = orderService.get(request.getOrderId());
            responseObserver.onNext(toResponse(order));
            responseObserver.onCompleted();
        } catch (IllegalArgumentException e) {
            responseObserver.onError(Status.NOT_FOUND.withDescription(e.getMessage()).asRuntimeException());
        }
    }

    @Override
    public void listOrders(ListOrdersRequest request, StreamObserver<ListOrdersResponse> responseObserver) {
        List<Order> orders = orderService.list(request.getStatus());
        ListOrdersResponse.Builder builder = ListOrdersResponse.newBuilder();
        orders.forEach(o -> builder.addOrders(toResponse(o)));
        responseObserver.onNext(builder.build());
        responseObserver.onCompleted();
    }

    static OrderResponse toResponse(Order order) {
        OrderResponse.Builder builder = OrderResponse.newBuilder()
                .setOrderId(order.getId())
                .setStatus(order.getStatus().name())
                .setTotal(order.getTotal())
                .setCustomerEmail(nullToEmpty(order.getCustomerEmail()))
                .setForcePaymentFailure(order.isForcePaymentFailure())
                .setCreatedAt(order.getCreatedAt().toString())
                .setUpdatedAt(order.getUpdatedAt().toString())
                .setStatusReason(nullToEmpty(order.getStatusReason()));

        order.getItems().forEach(item -> builder.addItems(
                com.studyshop.proto.orders.OrderItem.newBuilder()
                        .setProductId(item.getProductId())
                        .setProductName(nullToEmpty(item.getProductName()))
                        .setQuantity(item.getQuantity())
                        .setUnitPrice(item.getUnitPrice())
                        .build()
        ));
        return builder.build();
    }

    private static String nullToEmpty(String value) {
        return value == null ? "" : value;
    }
}
