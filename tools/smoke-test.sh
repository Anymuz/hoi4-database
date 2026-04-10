#!/usr/bin/env bash
# HOI4 Database API - Smoke Test Script
# Run from WSL: bash tools/smoke-test.sh
# Assumes the API is running on localhost:8000

set -euo pipefail

BASE="http://localhost:8000"
PASS=0
FAIL=0

check() {
  local label="$1"
  local status="$2"
  local expected="${3:-200}"
  if [ "$status" -eq "$expected" ]; then
    echo "  PASS  $label (HTTP $status)"
    PASS=$((PASS + 1))
  else
    echo "  FAIL  $label (expected $expected, got $status)"
    FAIL=$((FAIL + 1))
  fi
}

echo "=== REST Smoke Tests ==="

check "GET /health" \
  "$(curl -s -o /dev/null -w '%{http_code}' "$BASE/health")"

check "GET /api/v1/countries?limit=5" \
  "$(curl -s -o /dev/null -w '%{http_code}' "$BASE/api/v1/countries?limit=5")"

check "GET /api/v1/countries/GER" \
  "$(curl -s -o /dev/null -w '%{http_code}' "$BASE/api/v1/countries/GER")"

check "GET /api/v1/countries/GER?date=1936-01-01" \
  "$(curl -s -o /dev/null -w '%{http_code}' "$BASE/api/v1/countries/GER?date=1936-01-01")"

check "GET /api/v1/countries/GER?date=1939-08-14" \
  "$(curl -s -o /dev/null -w '%{http_code}' "$BASE/api/v1/countries/GER?date=1939-08-14")"

check "GET /api/v1/states/64" \
  "$(curl -s -o /dev/null -w '%{http_code}' "$BASE/api/v1/states/64")"

check "GET /api/v1/technologies?folder=infantry" \
  "$(curl -s -o /dev/null -w '%{http_code}' "$BASE/api/v1/technologies?folder=infantry")"

check "GET /api/v1/countries/GER/characters" \
  "$(curl -s -o /dev/null -w '%{http_code}' "$BASE/api/v1/countries/GER/characters")"

check "GET /api/v1/countries/GER/divisions" \
  "$(curl -s -o /dev/null -w '%{http_code}' "$BASE/api/v1/countries/GER/divisions")"

check "GET /api/v1/countries/GER/naval" \
  "$(curl -s -o /dev/null -w '%{http_code}' "$BASE/api/v1/countries/GER/naval")"

check "GET /api/v1/countries/GER/air" \
  "$(curl -s -o /dev/null -w '%{http_code}' "$BASE/api/v1/countries/GER/air")"

check "GET /api/v1/focus-trees" \
  "$(curl -s -o /dev/null -w '%{http_code}' "$BASE/api/v1/focus-trees")"

check "GET /api/v1/equipment?is_archetype=true" \
  "$(curl -s -o /dev/null -w '%{http_code}' "$BASE/api/v1/equipment?is_archetype=true")"

check "GET /api/v1/ideas?slot=economy" \
  "$(curl -s -o /dev/null -w '%{http_code}' "$BASE/api/v1/ideas?slot=economy")"

check "GET /api/v1/mios" \
  "$(curl -s -o /dev/null -w '%{http_code}' "$BASE/api/v1/mios")"

check "GET /api/v1/operations" \
  "$(curl -s -o /dev/null -w '%{http_code}' "$BASE/api/v1/operations")"

check "GET /api/v1/bop" \
  "$(curl -s -o /dev/null -w '%{http_code}' "$BASE/api/v1/bop")"

echo ""
echo "=== GraphQL Smoke Test ==="

check "POST /graphql (country query)" \
  "$(curl -s -o /dev/null -w '%{http_code}' -X POST "$BASE/graphql" \
    -H "Content-Type: application/json" \
    -d '{"query": "{ country(tag: \"GER\") { tag stability ownedStates { stateId } } }"}')"

echo ""
echo "=== Annotations CRUD Lifecycle ==="

# Create
CREATE_RESP=$(curl -s -w '\n%{http_code}' -X POST "$BASE/api/v1/annotations" \
  -H "Content-Type: application/json" \
  -d '{"entity_type": "country", "entity_key": "GER", "note": "Smoke test annotation"}')
CREATE_STATUS=$(echo "$CREATE_RESP" | tail -1)
CREATE_BODY=$(echo "$CREATE_RESP" | sed '$d')
check "POST /api/v1/annotations (create)" "$CREATE_STATUS" 201

# Extract annotation_id
ANN_ID=$(echo "$CREATE_BODY" | grep -o '"annotation_id":[0-9]*' | grep -o '[0-9]*')

if [ -n "$ANN_ID" ]; then
  # Read back
  check "GET /api/v1/annotations/$ANN_ID (read)" \
    "$(curl -s -o /dev/null -w '%{http_code}' "$BASE/api/v1/annotations/$ANN_ID")"

  # Delete
  check "DELETE /api/v1/annotations/$ANN_ID" \
    "$(curl -s -o /dev/null -w '%{http_code}' -X DELETE "$BASE/api/v1/annotations/$ANN_ID")" 204

  # Verify gone
  check "GET /api/v1/annotations/$ANN_ID (verify deleted)" \
    "$(curl -s -o /dev/null -w '%{http_code}' "$BASE/api/v1/annotations/$ANN_ID")" 404
else
  echo "  FAIL  Could not extract annotation_id from create response"
  FAIL=$((FAIL + 3))
fi

echo ""
echo "==============================="
echo "  PASS: $PASS   FAIL: $FAIL"
echo "==============================="

[ "$FAIL" -eq 0 ] && exit 0 || exit 1
