# Kafka CLI

## O que ela enxerga

O mesmo dado da UI no terminal.

## Onde

dentro do container, localhost:9092

## Como usar neste lab

docker compose exec kafka /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --list

docker compose exec kafka /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic orders.events --from-beginning --group qa-lab-leitura

docker compose exec kafka /opt/kafka/bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --all-groups

## Fonte

https://kafka.apache.org/documentation/#basic_ops

## Não serve para

Substituir as outras ferramentas da [lista](README.md).
