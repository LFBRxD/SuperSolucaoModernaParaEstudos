#!/usr/bin/env bash
# Uso: ACADEMY_PROJECT_DIR=../studyshop-do-zero ./scripts/academy/validate-checkpoint.sh all
set -euo pipefail
CHECKPOINT="${1:-all}"
DIR="${ACADEMY_PROJECT_DIR:-}"
if [[ -z "$DIR" || ! -d "$DIR" ]]; then
  echo "Defina ACADEMY_PROJECT_DIR para a pasta do espelho."
  exit 1
fi

has_text() {
  grep -R -l -F "$1" "$DIR" --include='*.md' --include='*.java' --include='*.yml' --include='*.yaml' --include='*.xml' --include='*.proto' >/dev/null 2>&1
}

run_one() {
  local name="$1" ok=1
  case "$name" in
    bootstrap) [[ -f "$DIR/pom.xml" && -d "$DIR/src/main/java" ]] || ok=0 ;;
    catalog-api) has_text "11101" || has_text "/api/products" || ok=0 ;;
    orders-mongo) has_text "11108" && ! has_text "localhost:11008" || ok=0 ;;
    grpc-gateway) find "$DIR" -name '*.proto' | grep -q . || ok=0 ;;
    kafka-events) has_text "eventType" || has_text ".events" || ok=0 ;;
    saga) has_text "CONFIRMED" || ok=0 ;;
    scheduled-jobs) has_text "quartz" && has_text "@Scheduled" || ok=0 ;;
    web-auth) has_text "401" || has_text "SecurityFilterChain" || ok=0 ;;
    observability) has_text "otel" || has_text "log" || ok=0 ;;
    automation-ci) has_text "mvn test" || ok=0 ;;
    platform) find "$DIR" \( -name Dockerfile -o -name 'compose*.yml' \) | grep -q . || has_text "Dockerfile" || ok=0 ;;
    *) echo "Checkpoint desconhecido: $name"; return 1 ;;
  esac
  if [[ "$ok" -eq 1 ]]; then echo "OK  $name"; else echo "FALHOU  $name"; return 1; fi
}

names=(bootstrap catalog-api orders-mongo grpc-gateway kafka-events saga scheduled-jobs web-auth observability automation-ci platform)
if [[ "$CHECKPOINT" != "all" ]]; then names=("$CHECKPOINT"); fi
failed=0
for n in "${names[@]}"; do
  run_one "$n" || failed=$((failed + 1))
done
if [[ "$failed" -gt 0 ]]; then exit 1; fi
echo "Checkpoints verdes: ${#names[@]}"
