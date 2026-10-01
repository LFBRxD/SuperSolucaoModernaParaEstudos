package com.studyshop.inventory.grpc;

import com.studyshop.inventory.domain.Product;
import com.studyshop.inventory.service.InventoryService;
import com.studyshop.proto.inventory.GetProductRequest;
import com.studyshop.proto.inventory.HealthRequest;
import com.studyshop.proto.inventory.HealthResponse;
import com.studyshop.proto.inventory.InventoryServiceGrpc;
import com.studyshop.proto.inventory.ListProductsRequest;
import com.studyshop.proto.inventory.ListProductsResponse;
import com.studyshop.proto.inventory.ProductResponse;
import com.studyshop.proto.inventory.UpdateStockRequest;
import io.grpc.Status;
import io.grpc.stub.StreamObserver;
import net.devh.boot.grpc.server.service.GrpcService;

@GrpcService
public class InventoryGrpcService extends InventoryServiceGrpc.InventoryServiceImplBase {

    private final InventoryService inventoryService;

    public InventoryGrpcService(InventoryService inventoryService) {
        this.inventoryService = inventoryService;
    }

    @Override
    public void listProducts(ListProductsRequest request, StreamObserver<ListProductsResponse> responseObserver) {
        ListProductsResponse.Builder builder = ListProductsResponse.newBuilder();
        inventoryService.listProducts().forEach(p -> builder.addProducts(toResponse(p)));
        responseObserver.onNext(builder.build());
        responseObserver.onCompleted();
    }

    @Override
    public void getProduct(GetProductRequest request, StreamObserver<ProductResponse> responseObserver) {
        try {
            Product product = inventoryService.getProduct(request.getProductId());
            responseObserver.onNext(toResponse(product));
            responseObserver.onCompleted();
        } catch (IllegalArgumentException e) {
            responseObserver.onError(Status.NOT_FOUND.withDescription(e.getMessage()).asRuntimeException());
        }
    }

    @Override
    public void updateStock(UpdateStockRequest request, StreamObserver<ProductResponse> responseObserver) {
        try {
            Product product = inventoryService.updateStock(request.getProductId(), request.getQuantity());
            responseObserver.onNext(toResponse(product));
            responseObserver.onCompleted();
        } catch (IllegalArgumentException e) {
            responseObserver.onError(Status.INVALID_ARGUMENT.withDescription(e.getMessage()).asRuntimeException());
        }
    }

    @Override
    public void getHealth(HealthRequest request, StreamObserver<HealthResponse> responseObserver) {
        responseObserver.onNext(HealthResponse.newBuilder()
                .setStatus("UP")
                .setService("inventory-service")
                .build());
        responseObserver.onCompleted();
    }

    private ProductResponse toResponse(Product product) {
        return ProductResponse.newBuilder()
                .setProductId(product.getId())
                .setSku(nullToEmpty(product.getSku()))
                .setName(nullToEmpty(product.getName()))
                .setDescription(nullToEmpty(product.getDescription()))
                .setPrice(product.getPrice())
                .setQuantity(product.getQuantity())
                .build();
    }

    private static String nullToEmpty(String value) {
        return value == null ? "" : value;
    }
}
