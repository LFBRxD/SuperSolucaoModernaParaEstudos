#!/usr/bin/env bash
# Smoke test autenticado (JWT local).
# Uso:
#   ./scripts/smoke.sh
#   BASE_URL=http://localhost:11001 ./scripts/smoke.sh
set -euo pipefail

BASE_URL="${BASE_URL:-http://localhost:11001}"
QA_USER="${QA_USER:-qa}"
QA_PASS="${QA_PASS:-qa123}"
ADMIN_USER="${ADMIN_USER:-admin}"
ADMIN_PASS="${ADMIN_PASS:-admin123}"

if ! command -v curl >/dev/null 2>&1; then
  echo "curl é obrigatório"
  exit 1
fi

if ! command -v jq >/dev/null 2>&1; then
  echo "jq é obrigatório para smoke autenticado (sudo apt install jq)"
  exit 1
fi

echo "==> Smoke StudyShop ($BASE_URL)"
echo ""

echo "[1/9] GET /api/health (público)"
HEALTH="$(curl -sf "$BASE_URL/api/health")"
echo "$HEALTH" | jq -c .
OVERALL="$(echo "$HEALTH" | jq -r '.overall')"
if [[ "$OVERALL" != "UP" ]]; then
  echo "Health DEGRADED/DOWN — abortando."
  exit 1
fi

echo ""
echo "[2/9] GET /api/products sem token (esperado 401)"
CODE_ANON="$(curl -s -o /dev/null -w "%{http_code}" "$BASE_URL/api/products")"
echo "      HTTP $CODE_ANON"
if [[ "$CODE_ANON" != "401" ]]; then
  echo "Esperado 401 sem token"
  exit 1
fi

echo ""
echo "[3/9] POST /api/auth/login (qa)"
LOGIN_QA="$(curl -sf -X POST "$BASE_URL/api/auth/login" \
  -H "Content-Type: application/json" \
  -d "{\"username\":\"$QA_USER\",\"password\":\"$QA_PASS\"}")"
TOKEN_QA="$(echo "$LOGIN_QA" | jq -r '.accessToken')"
if [[ -z "$TOKEN_QA" || "$TOKEN_QA" == "null" ]]; then
  echo "Login qa falhou"
  exit 1
fi
echo "      token qa ok (roles=$(echo "$LOGIN_QA" | jq -c '.roles'))"

echo ""
echo "[4/9] GET /api/products (Bearer qa)"
PRODUCTS="$(curl -sf "$BASE_URL/api/products" -H "Authorization: Bearer $TOKEN_QA")"
COUNT="$(echo "$PRODUCTS" | jq 'length')"
echo "      produtos=$COUNT"
if [[ "$COUNT" -lt 1 ]]; then
  echo "Nenhum produto retornado"
  exit 1
fi
PRODUCT_ID="prod-mouse"

echo ""
echo "[5/9] POST /api/orders (Bearer qa)"
BODY=$(cat <<EOF
{"customerEmail":"smoke@studyshop.local","forcePaymentFailure":false,"items":[{"productId":"$PRODUCT_ID","quantity":1}]}
EOF
)
ORDER="$(curl -sf -X POST "$BASE_URL/api/orders" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN_QA" \
  -d "$BODY")"
ORDER_ID="$(echo "$ORDER" | jq -r '.orderId')"
echo "      orderId=$ORDER_ID status=$(echo "$ORDER" | jq -r '.status')"

wait_status() {
  local id="$1" token="$2" expected="$3" i status body
  for i in $(seq 1 60); do
    body="$(curl -sf "$BASE_URL/api/orders/$id" -H "Authorization: Bearer $token")"
    status="$(echo "$body" | jq -r '.status')"
    echo "      poll $id -> $status"
    if [[ "$status" == "$expected" ]]; then
      LAST_ORDER="$body"
      return 0
    fi
    if [[ "$status" == "CONFIRMED" || "$status" == "CANCELLED" ]]; then
      echo "Estado final inesperado: $status (esperado $expected)"
      echo "$body" | jq -c '{orderId,status,statusReason}'
      return 1
    fi
    sleep 1
  done
  echo "Timeout esperando $expected; ultimo status=${status:-desconhecido}"
  return 1
}

echo "      esperando CONFIRMED (ate 60s)"
wait_status "$ORDER_ID" "$TOKEN_QA" "CONFIRMED"

echo ""
echo "[6/9] PUT stock: qa=403, admin=200"
CODE_QA="$(curl -s -o /dev/null -w "%{http_code}" -X PUT "$BASE_URL/api/products/$PRODUCT_ID/stock" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN_QA" \
  -d '{"quantity":50}')"
echo "      qa PUT stock -> HTTP $CODE_QA (esperado 403)"
if [[ "$CODE_QA" != "403" ]]; then
  echo "Esperado 403 para USER no stock"
  exit 1
fi

LOGIN_ADMIN="$(curl -sf -X POST "$BASE_URL/api/auth/login" \
  -H "Content-Type: application/json" \
  -d "{\"username\":\"$ADMIN_USER\",\"password\":\"$ADMIN_PASS\"}")"
TOKEN_ADMIN="$(echo "$LOGIN_ADMIN" | jq -r '.accessToken')"
STOCK="$(curl -sf -X PUT "$BASE_URL/api/products/$PRODUCT_ID/stock" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN_ADMIN" \
  -d '{"quantity":50}')"
echo "      admin PUT stock -> $(echo "$STOCK" | jq -c '{productId,quantity}')"

echo ""
echo "[7/9] POST pedido com falha de pagamento -> CANCELLED"
FAIL_BODY='{"customerEmail":"smoke-fail@studyshop.local","forcePaymentFailure":true,"items":[{"productId":"prod-mouse","quantity":1}]}'
FAIL_ORDER="$(curl -sf -X POST "$BASE_URL/api/orders" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN_QA" \
  -d "$FAIL_BODY")"
FAIL_ID="$(echo "$FAIL_ORDER" | jq -r '.orderId')"
wait_status "$FAIL_ID" "$TOKEN_QA" "CANCELLED"
echo "      motivo=$(echo "$LAST_ORDER" | jq -r '.statusReason')"

echo ""
echo "[8/9] POST prod-raro quantidade 2 -> CANCELLED"
curl -sf -X PUT "$BASE_URL/api/products/prod-raro/stock" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN_ADMIN" \
  -d '{"quantity":1}' >/dev/null
RARE_BODY='{"customerEmail":"smoke-rare@studyshop.local","forcePaymentFailure":false,"items":[{"productId":"prod-raro","quantity":2}]}'
RARE_ORDER="$(curl -sf -X POST "$BASE_URL/api/orders" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN_QA" \
  -d "$RARE_BODY")"
RARE_ID="$(echo "$RARE_ORDER" | jq -r '.orderId')"
wait_status "$RARE_ID" "$TOKEN_QA" "CANCELLED"
echo "      motivo=$(echo "$LAST_ORDER" | jq -r '.statusReason')"

echo ""
echo "[9/9] GET notificacao do pedido confirmado"
NOTES="$(curl -sf "$BASE_URL/api/notifications/order/$ORDER_ID" -H "Authorization: Bearer $TOKEN_QA")"
NOTE_COUNT="$(echo "$NOTES" | jq 'length')"
echo "      notificacoes=$NOTE_COUNT"
if [[ "$NOTE_COUNT" -lt 1 ]]; then
  echo "Esperada ao menos uma notificacao para $ORDER_ID"
  exit 1
fi

echo ""
echo "Smoke OK."
