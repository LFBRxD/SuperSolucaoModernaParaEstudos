#!/usr/bin/env bash
# Sobe a stack Docker Compose do StudyShop.
# Preferência de estudo: rode os comandos deste script manualmente (ver docs/comandos-linux-wsl.md).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT/infra"

echo "==> StudyShop up"
echo "    comando: docker compose up -d --build"
docker compose up -d --build

echo ""
echo "Servicos (portas a partir de 11000):"
echo "  Web:           http://localhost:11000"
echo "  API Gateway:   http://localhost:11001"
echo "  Swagger:       http://localhost:11001/swagger-ui.html"
echo "  Health:        http://localhost:11001/api/health"
echo "  Grafana:       http://localhost:11010  (admin/admin)"
echo "  Jaeger:        http://localhost:11011"
echo "  Prometheus:    http://localhost:11012"
echo ""
echo "Smoke: ./scripts/smoke.sh"
echo "Docs:  docs/comandos-linux-wsl.md"
