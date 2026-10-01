package com.studyshop.payments.config;

import org.apache.kafka.clients.admin.NewTopic;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.kafka.config.TopicBuilder;

@Configuration
public class KafkaConfig {

    @Bean
    public NewTopic paymentsEventsTopic() {
        return TopicBuilder.name("payments.events").partitions(3).replicas(1).build();
    }
}
