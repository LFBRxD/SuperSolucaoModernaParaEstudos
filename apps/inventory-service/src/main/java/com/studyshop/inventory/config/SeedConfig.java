package com.studyshop.inventory.config;

import com.studyshop.inventory.domain.Product;
import com.studyshop.inventory.domain.ProductRepository;
import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class SeedConfig {

    @Bean
    CommandLineRunner seedProducts(ProductRepository repository) {
        return args -> {
            if (repository.count() > 0) {
                return;
            }
            repository.save(new Product(
                    "prod-notebook", "NB-001", "Notebook Study Pro",
                    "Notebook 16GB RAM para estudos de QA", 4599.90, 10));
            repository.save(new Product(
                    "prod-mouse", "MS-001", "Mouse Ergonômico",
                    "Mouse silencioso para longas sessões de teste", 149.90, 50));
            repository.save(new Product(
                    "prod-headset", "HS-001", "Headset QA Focus",
                    "Headset com cancelamento de ruído", 399.00, 25));
            repository.save(new Product(
                    "prod-teclado", "KB-001", "Teclado Mecânico",
                    "Teclado mecânico switch brown", 529.00, 15));
            repository.save(new Product(
                    "prod-raro", "RA-001", "Item Escasso",
                    "Produto com estoque baixo para testes negativos", 99.00, 1));
        };
    }
}
