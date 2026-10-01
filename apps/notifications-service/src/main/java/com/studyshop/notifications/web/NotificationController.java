package com.studyshop.notifications.web;

import com.studyshop.notifications.domain.Notification;
import com.studyshop.notifications.domain.NotificationRepository;
import java.util.List;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/notifications")
@CrossOrigin(origins = "*")
public class NotificationController {

    private final NotificationRepository notificationRepository;

    public NotificationController(NotificationRepository notificationRepository) {
        this.notificationRepository = notificationRepository;
    }

    @GetMapping
    public List<Notification> list() {
        return notificationRepository.findAll();
    }

    @GetMapping("/order/{orderId}")
    public List<Notification> byOrder(@PathVariable String orderId) {
        return notificationRepository.findByOrderIdOrderByCreatedAtDesc(orderId);
    }
}
