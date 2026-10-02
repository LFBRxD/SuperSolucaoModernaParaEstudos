# syntax=docker/dockerfile:1
FROM maven:3.9.9-eclipse-temurin-21 AS build
WORKDIR /workspace
COPY pom.xml .
COPY libs/proto libs/proto
COPY apps/orders-service apps/orders-service
COPY apps/inventory-service apps/inventory-service
COPY apps/payments-service apps/payments-service
COPY apps/notifications-service apps/notifications-service
COPY apps/api-gateway apps/api-gateway
RUN mvn -q -pl apps/payments-service -am package -DskipTests

FROM eclipse-temurin:21-jre
WORKDIR /app
ADD https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases/download/v2.10.0/opentelemetry-javaagent.jar /otel/opentelemetry-javaagent.jar
COPY --from=build /workspace/apps/payments-service/target/payments-service-*.jar app.jar
EXPOSE 11006
ENV JAVA_TOOL_OPTIONS="-javaagent:/otel/opentelemetry-javaagent.jar"
ENTRYPOINT ["java", "-jar", "app.jar"]
