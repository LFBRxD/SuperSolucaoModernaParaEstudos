#!/usr/bin/env bash
# Apaga volumes do lab e sobe de novo. Pedidos somem; o seed volta.
set -euo pipefail
if [[ "${1:-}" != "--yes" ]]; then
  echo "Isto apaga o volume do Mongo do oraculo. Rode com --yes se for o que voce quer."
  exit 1
fi
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
"$ROOT/down.sh" --volumes
"$ROOT/up.sh"
