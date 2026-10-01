#!/usr/bin/env bash
# Derruba a stack Docker Compose do StudyShop.
# Uso:
#   ./scripts/down.sh
#   ./scripts/down.sh --volumes   # apaga volumes (mongo/grafana)
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT/infra"

echo "==> StudyShop down"

if [[ "${1:-}" == "--volumes" || "${1:-}" == "-v" ]]; then
  echo "    comando: docker compose down -v"
  docker compose down -v
else
  echo "    comando: docker compose down"
  docker compose down
fi

echo "Stack parada."
