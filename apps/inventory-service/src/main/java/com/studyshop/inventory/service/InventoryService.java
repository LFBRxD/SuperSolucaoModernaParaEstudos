package com.studyshop.inventory.service;

import com.studyshop.inventory.domain.Product;
import com.studyshop.inventory.domain.ProductRepository;
import java.util.List;
import org.springframework.stereotype.Service;

@Service
public class InventoryService {

    private final ProductRepository productRepository;

    public InventoryService(ProductRepository productRepository) {
        this.productRepository = productRepository;
    }

    public List<Product> listProducts() {
        return productRepository.findAll();
    }

    public Product getProduct(String productId) {
        return productRepository.findById(productId)
                .orElseThrow(() -> new IllegalArgumentException("Produto não encontrado: " + productId));
    }

    public Product updateStock(String productId, int quantity) {
        if (quantity < 0) {
            throw new IllegalArgumentException("Quantidade não pode ser negativa");
        }
        Product product = getProduct(productId);
        product.setQuantity(quantity);
        return productRepository.save(product);
    }

    public synchronized ReservationResult reserve(String orderId, List<ReservationItem> items) {
        for (ReservationItem item : items) {
            Product product = productRepository.findById(item.productId()).orElse(null);
            if (product == null) {
                return ReservationResult.rejected(orderId, "Produto não encontrado: " + item.productId());
            }
            if (product.getQuantity() < item.quantity()) {
                return ReservationResult.rejected(orderId,
                        "Estoque insuficiente para " + product.getName()
                                + " (disponível=" + product.getQuantity()
                                + ", solicitado=" + item.quantity() + ")");
            }
        }

        for (ReservationItem item : items) {
            Product product = getProduct(item.productId());
            product.setQuantity(product.getQuantity() - item.quantity());
            productRepository.save(product);
        }
        return ReservationResult.reserved(orderId);
    }

    public record ReservationItem(String productId, int quantity) {
    }

    public record ReservationResult(boolean success, String orderId, String reason) {
        public static ReservationResult reserved(String orderId) {
            return new ReservationResult(true, orderId, null);
        }

        public static ReservationResult rejected(String orderId, String reason) {
            return new ReservationResult(false, orderId, reason);
        }
    }
}
