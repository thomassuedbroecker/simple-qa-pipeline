#!/bin/bash
cat <<EOF
DISCOVERY_API_KEY=${DISCOVERY_API_KEY:-''}
DISCOVERY_URL=${DISCOVERY_URL:-''}
DISCOVERY_COLLECTION_ID=${DISCOVERY_COLLECTION_ID:-''}
DISCOVERY_PROJECT=${DISCOVERY_PROJECT:-''}
DISCOVERY_INSTANCE=${DISCOVERY_INSTANCE:-''}
WATSONX_URL=${WATSONX_URL:-''}
WATSONX_LLM_NAME=${WATSONX_LLM_NAME:-''}
WATSONX_MIN_NEW_TOKENS=${WATSONX_MIN_NEW_TOKENS:-''}
WATSONX_MAX_NEW_TOKENS=${WATSONX_MAX_NEW_TOKENS:-''}
WATSONX_PROMPT=${WATSONX_PROMPT:-''}
WATSONX_PROJECT_ID=${WATSONX_PROJECT_ID:-''}
WATSONX_VERSION=${WATSONX_VERSION:-''}
IBMCLOUD_APIKEY=${IBMCLOUD_APIKEY:-''}
IBMCLOUD_URL=${IBMCLOUD_URL:-''}
APP_USER=${APP_USER:-''}
APP_APIKEY=${APP_APIKEY:-''}
EOF