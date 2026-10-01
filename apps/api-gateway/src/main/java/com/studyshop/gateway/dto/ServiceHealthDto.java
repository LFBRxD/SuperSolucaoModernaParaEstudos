package com.studyshop.gateway.dto;

import java.util.List;

public record ServiceHealthDto(String service, String status, String detail) {
    public record HealthOverviewDto(String overall, List<ServiceHealthDto> services) {
    }
}
