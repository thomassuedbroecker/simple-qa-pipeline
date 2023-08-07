#!/bin/bash

# **************** Global variables
export HOME_PATH=$(pwd)

# **********************************************************************************
# Functions definition
# **********************************************************************************

function check_docker () {
    ERROR=$(docker ps 2>&1)
    RESULT=$(echo $ERROR | grep 'Cannot' | awk '{print $1;}')
    VERIFY="Cannot"
    if [ "$RESULT" == "$VERIFY" ]; then
        echo "Docker is not running. Stop script execution."
        exit 1 
    fi
}

#**********************************************************************************
# Execution
# *********************************************************************************

echo "************************************"
echo " Build and start containers with Docker compose " 
echo "- 'QA-Service'"
echo "************************************"

check_docker

# 1. set needed common environment
echo "Home path:    $HOME_PATH"
"/bin/sh" "${HOME_PATH}"/env_profile_generate.sh > ~/.env_profile

# 2. load application environment configurations
source $(pwd)/../../code/.env

# 3. set qa service docker context
cd $HOME_PATH/../../code
export QA_SERVICE_DOCKER_CONTEXT="$(pwd)"
cd $HOME_PATH

# 9. Start compose
docker compose version
echo "**************** BUILD ******************" 
docker compose -f ./docker_compose.yaml build
echo "**************** START ******************" 
docker compose -f ./docker_compose.yaml up # --detach

#docker compose -f ./docker_compose.yaml stop