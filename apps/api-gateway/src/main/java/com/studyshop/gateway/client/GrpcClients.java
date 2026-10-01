package com.studyshop.gateway.client;

import com.studyshop.proto.inventory.GetProductRequest;
import com.studyshop.proto.inventory.HealthRequest;
import com.studyshop.proto.inventory.InventoryServiceGrpc;
import com.studyshop.proto.inventory.ListProductsRequest;
import com.studyshop.proto.inventory.ProductResponse;
import com.studyshop.proto.inventory.UpdateStockRequest;
import com.studyshop.proto.orders.CreateOrderRequest;
import com.studyshop.proto.orders.GetOrderRequest;
import com.studyshop.proto.orders.ListOrdersRequest;
import com.studyshop.proto.orders.OrderItemInput;
import com.studyshop.proto.orders.OrderResponse;
import com.studyshop.proto.orders.OrderServiceGrpc;
import java.util.List;
import net.devh.boot.grpc.client.inject.GrpcClient;
import org.springframework.stereotype.Component;

@Component
public class GrpcClients {

    @GrpcClient("orders-service")
    private OrderServiceGrpc.OrderServiceBlockingStub ordersStub;

    @GrpcClient("inventory-service")
    private InventoryServiceGrpc.InventoryServiceBlockingStub inventoryStub;

    public OrderResponse createOrder(CreateOrderRequest request) {
        return ordersStub.createOrder(request);
    }

    public OrderResponse getOrder(String orderId) {
        return ordersStub.getOrder(GetOrderRequest.newBuilder().setOrderId(orderId).build());
    }

    public List<OrderResponse> listOrders(String status) {
        return ordersStub.listOrders(ListOrdersRequest.newBuilder()
                .setStatus(status == null ? "" : status)
                .build()).getOrdersList();
    }

    public List<ProductResponse> listProducts() {
        return inventoryStub.listProducts(ListProductsRequest.getDefaultInstance()).getProductsList();
    }

    public ProductResponse getProduct(String productId) {
        return inventoryStub.getProduct(GetProductRequest.newBuilder().setProductId(productId).build());
    }

    public ProductResponse updateStock(String productId, int quantity) {
        return inventoryStub.updateStock(UpdateStockRequest.newBuilder()
                .setProductId(productId)
                .setQuantity(quantity)
                .build());
    }

    public boolean inventoryUp() {
        try {
            return "UP".equals(inventoryStub.getHealth(HealthRequest.getDefaultInstance()).getStatus());
        } catch (Exception e) {
            return false;
        }
    }

    public OrderItemInput toItemInput(String productId, String productName, int quantity, double unitPrice) {
        return OrderItemInput.newBuilder()
                .setProductId(productId)
                .setProductName(productName)
                .setQuantity(quantity)
                .setUnitPrice(unitPrice)
                .build();
    }
}
