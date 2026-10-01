#!/usr/bin/env bash
# Smoke test com curl/jq — bons comandos para estudar API.
# Uso:
#   ./scripts/smoke.sh
#   BASE_URL=http://localhost:10001 ./scripts/smoke.sh
set -euo pipefail

BASE_URL="${BASE_URL:-http://localhost:10001}"

if ! command -v curl >/dev/null 2>&1; then
  echo "curl é obrigatório"
  exit 1
fi

echo "==> Smoke StudyShop ($BASE_URL)"
echo ""

echo "[1/3] GET /api/health"
echo "      curl -s $BASE_URL/api/health"
HEALTH="$(curl -sf "$BASE_URL/api/health")"
echo "$HEALTH"
if command -v jq >/dev/null 2>&1; then
  OVERALL="$(echo "$HEALTH" | jq -r '.overall')"
  echo "      overall=$OVERALL"
  if [[ "$OVERALL" != "UP" ]]; then
    echo "Health DEGRADED/DOWN — abortando create order."
    exit 1
  fi
fi

echo ""
echo "[2/3] GET /api/products"
echo "      curl -s $BASE_URL/api/products"
PRODUCTS="$(curl -sf "$BASE_URL/api/products")"
echo "$PRODUCTS" | head -c 500
echo ""
PRODUCT_ID="prod-mouse"
if command -v jq >/dev/null 2>&1; then
  COUNT="$(echo "$PRODUCTS" | jq 'length')"
  echo "      produtos=$COUNT"
  if [[ "$COUNT" -lt 1 ]]; then
    echo "Nenhum produto retornado"
    exit 1
  fi
fi

echo ""
echo "[3/3] POST /api/orders"
BODY=$(cat <<EOF
{"customerEmail":"smoke@studyshop.local","forcePaymentFailure":false,"items":[{"productId":"$PRODUCT_ID","quantity":1}]}
EOF
)
echo "      curl -s -X POST $BASE_URL/api/orders -H 'Content-Type: application/json' -d '...'"
ORDER="$(curl -sf -X POST "$BASE_URL/api/orders" \
  -H "Content-Type: application/json" \
  -d "$BODY")"
echo "$ORDER"

ORDER_ID=""
if command -v jq >/dev/null 2>&1; then
  ORDER_ID="$(echo "$ORDER" | jq -r '.orderId')"
  echo "      orderId=$ORDER_ID status=$(echo "$ORDER" | jq -r '.status')"
else
  # fallback grosseiro sem jq
  ORDER_ID="$(echo "$ORDER" | sed -n 's/.*"orderId"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' | head -1)"
fi

if [[ -n "$ORDER_ID" && "$ORDER_ID" != "null" ]]; then
  echo ""
  echo "GET /api/orders/$ORDER_ID"
  echo "    curl -s $BASE_URL/api/orders/$ORDER_ID"
  curl -sf "$BASE_URL/api/orders/$ORDER_ID"
  echo ""
fi

echo ""
echo "Smoke OK."
echo "Dica: instale jq para JSON legível (sudo apt install jq)."
