package com.studyshop.gateway.web;

import java.util.List;
import java.util.Map;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.core.ParameterizedTypeReference;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestClient;

@RestController
@RequestMapping("/api/notifications")
public class NotificationsProxyController {

    private final RestClient restClient = RestClient.create();

    @Value("${studyshop.notifications-base-url:http://localhost:10007}")
    private String notificationsBaseUrl;

    @GetMapping
    public List<Map<String, Object>> list() {
        List<Map<String, Object>> body = restClient.get()
                .uri(notificationsBaseUrl + "/api/notifications")
                .retrieve()
                .body(new ParameterizedTypeReference<List<Map<String, Object>>>() {
                });
        return body == null ? List.of() : body;
    }

    @GetMapping("/order/{orderId}")
    public List<Map<String, Object>> byOrder(@PathVariable String orderId) {
        List<Map<String, Object>> body = restClient.get()
                .uri(notificationsBaseUrl + "/api/notifications/order/" + orderId)
                .retrieve()
                .body(new ParameterizedTypeReference<List<Map<String, Object>>>() {
                });
        return body == null ? List.of() : body;
    }
}
