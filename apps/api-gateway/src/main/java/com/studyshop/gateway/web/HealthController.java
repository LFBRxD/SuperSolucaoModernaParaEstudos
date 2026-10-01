package com.studyshop.gateway.web;

import com.studyshop.gateway.client.GrpcClients;
import com.studyshop.gateway.dto.ServiceHealthDto;
import com.studyshop.gateway.dto.ServiceHealthDto.HealthOverviewDto;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestClient;

@RestController
@RequestMapping("/api/health")
public class HealthController {

    private final GrpcClients grpcClients;
    private final RestClient restClient = RestClient.create();

    @Value("${studyshop.health.orders-url:http://localhost:8081/actuator/health}")
    private String ordersHealthUrl;

    @Value("${studyshop.health.inventory-url:http://localhost:8082/actuator/health}")
    private String inventoryHealthUrl;

    @Value("${studyshop.health.payments-url:http://localhost:8083/actuator/health}")
    private String paymentsHealthUrl;

    @Value("${studyshop.health.notifications-url:http://localhost:8084/actuator/health}")
    private String notificationsHealthUrl;

    public HealthController(GrpcClients grpcClients) {
        this.grpcClients = grpcClients;
    }

    @GetMapping
    public HealthOverviewDto overview() {
        List<ServiceHealthDto> services = new ArrayList<>();
        services.add(new ServiceHealthDto("api-gateway", "UP", "local"));
        services.add(checkHttp("orders-service", ordersHealthUrl));
        services.add(checkHttp("inventory-service", inventoryHealthUrl));
        services.add(checkHttp("payments-service", paymentsHealthUrl));
        services.add(checkHttp("notifications-service", notificationsHealthUrl));
        services.add(new ServiceHealthDto(
                "inventory-grpc",
                grpcClients.inventoryUp() ? "UP" : "DOWN",
                "gRPC health"));

        boolean allUp = services.stream().allMatch(s -> "UP".equals(s.status()));
        return new HealthOverviewDto(allUp ? "UP" : "DEGRADED", services);
    }

    @SuppressWarnings("unchecked")
    private ServiceHealthDto checkHttp(String name, String url) {
        try {
            Map<String, Object> body = restClient.get().uri(url).retrieve().body(Map.class);
            String status = body != null && body.get("status") != null ? String.valueOf(body.get("status")) : "UNKNOWN";
            return new ServiceHealthDto(name, status, url);
        } catch (Exception e) {
            return new ServiceHealthDto(name, "DOWN", e.getMessage());
        }
    }
}
