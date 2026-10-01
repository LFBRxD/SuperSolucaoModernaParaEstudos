package com.studyshop.gateway.web;

import com.studyshop.gateway.client.GrpcClients;
import com.studyshop.gateway.dto.CreateOrderRequestDto;
import com.studyshop.gateway.dto.OrderDto;
import com.studyshop.gateway.dto.ProductDto;
import com.studyshop.gateway.dto.UpdateStockRequestDto;
import com.studyshop.proto.inventory.ProductResponse;
import com.studyshop.proto.orders.CreateOrderRequest;
import com.studyshop.proto.orders.OrderItemInput;
import com.studyshop.proto.orders.OrderResponse;
import io.grpc.StatusRuntimeException;
import java.util.ArrayList;
import java.util.List;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.server.ResponseStatusException;

@RestController
@RequestMapping("/api")
public class ApiController {

    private final GrpcClients grpcClients;

    public ApiController(GrpcClients grpcClients) {
        this.grpcClients = grpcClients;
    }

    @GetMapping("/products")
    public List<ProductDto> listProducts() {
        return grpcClients.listProducts().stream().map(this::toProduct).toList();
    }

    @GetMapping("/products/{productId}")
    public ProductDto getProduct(@PathVariable String productId) {
        try {
            return toProduct(grpcClients.getProduct(productId));
        } catch (StatusRuntimeException e) {
            throw mapGrpc(e);
        }
    }

    @PutMapping("/products/{productId}/stock")
    public ProductDto updateStock(@PathVariable String productId, @RequestBody UpdateStockRequestDto body) {
        try {
            return toProduct(grpcClients.updateStock(productId, body.quantity()));
        } catch (StatusRuntimeException e) {
            throw mapGrpc(e);
        }
    }

    @PostMapping("/orders")
    public OrderDto createOrder(
            @RequestBody CreateOrderRequestDto body,
            @RequestHeader(value = "X-Force-Payment-Failure", required = false) String forceHeader) {
        try {
            boolean forceFailure = body.isForcePaymentFailure()
                    || "true".equalsIgnoreCase(forceHeader);

            CreateOrderRequest.Builder builder = CreateOrderRequest.newBuilder()
                    .setForcePaymentFailure(forceFailure)
                    .setCustomerEmail(body.getCustomerEmail() == null ? "" : body.getCustomerEmail());

            if (body.getItems() == null || body.getItems().isEmpty()) {
                throw new ResponseStatusException(HttpStatus.BAD_REQUEST, "Informe ao menos um item");
            }

            for (CreateOrderRequestDto.CreateOrderItemDto item : body.getItems()) {
                ProductResponse product = grpcClients.getProduct(item.getProductId());
                OrderItemInput input = grpcClients.toItemInput(
                        product.getProductId(),
                        product.getName(),
                        item.getQuantity(),
                        product.getPrice());
                builder.addItems(input);
            }

            return toOrder(grpcClients.createOrder(builder.build()));
        } catch (StatusRuntimeException e) {
            throw mapGrpc(e);
        }
    }

    @GetMapping("/orders")
    public List<OrderDto> listOrders(@RequestParam(required = false) String status) {
        return grpcClients.listOrders(status).stream().map(this::toOrder).toList();
    }

    @GetMapping("/orders/{orderId}")
    public OrderDto getOrder(@PathVariable String orderId) {
        try {
            return toOrder(grpcClients.getOrder(orderId));
        } catch (StatusRuntimeException e) {
            throw mapGrpc(e);
        }
    }

    private ProductDto toProduct(ProductResponse p) {
        return new ProductDto(
                p.getProductId(), p.getSku(), p.getName(), p.getDescription(), p.getPrice(), p.getQuantity());
    }

    private OrderDto toOrder(OrderResponse o) {
        List<OrderDto.OrderItemDto> items = new ArrayList<>();
        o.getItemsList().forEach(i -> items.add(new OrderDto.OrderItemDto(
                i.getProductId(), i.getProductName(), i.getQuantity(), i.getUnitPrice())));
        return new OrderDto(
                o.getOrderId(),
                o.getStatus(),
                o.getTotal(),
                o.getCustomerEmail(),
                o.getForcePaymentFailure(),
                o.getCreatedAt(),
                o.getUpdatedAt(),
                o.getStatusReason(),
                items
        );
    }

    private ResponseStatusException mapGrpc(StatusRuntimeException e) {
        return switch (e.getStatus().getCode()) {
            case NOT_FOUND -> new ResponseStatusException(HttpStatus.NOT_FOUND, e.getStatus().getDescription());
            case INVALID_ARGUMENT -> new ResponseStatusException(HttpStatus.BAD_REQUEST, e.getStatus().getDescription());
            default -> new ResponseStatusException(HttpStatus.BAD_GATEWAY, e.getStatus().getDescription());
        };
    }
}
