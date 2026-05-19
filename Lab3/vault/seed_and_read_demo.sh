#!/usr/bin/env bash
set -euo pipefail

export VAULT_ADDR="${VAULT_ADDR:-http://127.0.0.1:8200}"
export VAULT_TOKEN="${VAULT_TOKEN:-root}"

echo "Writing demo secret to Vault..."
curl --fail --silent --show-error \
  --header "X-Vault-Token: ${VAULT_TOKEN}" \
  --request POST \
  --data '{"data":{"DEPLOY_API_TOKEN":"vault-demo-token-123","REGISTRY_PASSWORD":"vault-demo-registry-password"}}' \
  "${VAULT_ADDR}/v1/secret/data/clouds/prod" > /dev/null

echo "Reading demo secret from Vault..."
curl --fail --silent \
  --header "X-Vault-Token: ${VAULT_TOKEN}" \
  "${VAULT_ADDR}/v1/secret/data/clouds/prod" | python3 -m json.tool
