#!/bin/bash
cat <<EOF
# Configuration for QA services
export GLOBAL_HOME_PATH=${HOME_PATH}
export GLOBAL_QA_SERVICE_API_URL=${QA_SERVICE_API_URL}
EOF