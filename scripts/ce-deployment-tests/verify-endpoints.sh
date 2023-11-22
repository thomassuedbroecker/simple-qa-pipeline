#!/bin/bash

# IBM Cloud - variables
source ./.env

# Input variables
LOG_FILE=${1}
CSV_FILE=${2}
ERROR_LOG_FILE=${3}

# Local variables
j=0
CSV_HEADER=1
TMP_FILE=tmp.json

# **********************************************************************************
# Functions definition
# **********************************************************************************

function login_to_ibm_cloud () {
    
    echo ""
    echo "*********************"
    echo "Log in to IBM Cloud"
    echo "*********************"
    echo ""

    ibmcloud login --apikey $IBM_CLOUD_API_KEY
    ibmcloud target -r $IBM_CLOUD_REGION
    ibmcloud target -g $IBM_CLOUD_RESOURCE_GROUP
}

function connect_ce_project() {
  echo "**********************************"
  echo " Using following project: $CODEENGINE_PROJECT_NAME" 
  echo "**********************************"

  # 1. Connect to IBM Cloud Code Engine project
  ibmcloud ce project select -n $CODEENGINE_PROJECT_NAME
  
  # 2. Get the kubecfg to connect to the related cluster
  ibmcloud ce project select -n $CODEENGINE_PROJECT_NAME --kubecfg

  # 3. Get the project namespace
  CODEENGINE_PROJECT_NAMESPACE=$(ibmcloud ce project get --name $CODEENGINE_PROJECT_NAME --output json | grep "namespace" | awk '{print $2;}' | sed 's/"//g' | sed 's/,//g')
  echo "Code Engine project namespace: $CODEENGINE_PROJECT_NAMESPACE"

  # 4. List all running pods
  kubectl get pods -n $CODEENGINE_PROJECT_NAMESPACE

}

# **** Kubernetes CLI ****

function kube_information(){

    echo "************************************"
    echo " Kubernetes info '$CODEENGINE_APP_NAME': pods, deployments and configmaps details "
    echo "************************************"
    
    kubectl get pods -n $CODEENGINE_PROJECT_NAMESPACE
    kubectl get deployments -n $CODEENGINE_PROJECT_NAMESPACE
    kubectl get configmaps -n $CODEENGINE_PROJECT_NAMESPACE

}

function kube_pod_log(){

    echo "************************************"
    echo " Kubernetes $CODEENGINE_APP_NAME: log"
    echo "************************************"
    
    # 1. Find the first pod for the application
    FIND="$CODEENGINE_APP_NAME"
    echo "Get pod: ${FIND}"
    APP_POD=$(kubectl get pod -n $CODEENGINE_PROJECT_NAMESPACE | grep ${FIND} | awk '{print $1}')
    echo "************************************"
    echo "Show log for the pod: $APP_POD"
    echo "************************************"
    # 2. Show the logs for this pod
    kubectl logs --since=10m $APP_POD
}

function ce_log () {
    echo "************************************"
    echo "Show log for the CE application: $CODEENGINE_APP_NAME"
    echo "************************************"
    
    ibmcloud ce application logs --application $CODEENGINE_APP_NAME --all-containers
}

#**********************************************************************************
# Execution
# *********************************************************************************

login_to_ibm_cloud
connect_ce_project

# Init output files
echo "Run,Endpoint,Question,API_call,Start_time,Duration,Response" > ${LOG_FILE}
echo "Errorfile endpoint verification" > ${ERROR_LOG_FILE}

while IFS=',' read -r CE_HOST QUESTION API_CALL API_KEY;
do  
    start_time=$(date "+%s")   
    ((j++))
    RUN=$((j-1))
    if [[ $j -eq $CSV_HEADER ]]; then
        echo "---------------------------"
        echo "CSV Header:"
        echo "${CE_HOST} ${QUESTION} ${API_CALL} ${API_KEY}"
        echo ""
    else
        curl -X POST -u "apikey:${API_KEY}" --header "Content-Type: application/json" --data "{ \"query\": \"${QUESTION}\" }" "https://${CE_HOST}/${API_CALL}" | jq '.' > ./${TMP_FILE}
        OUTPUT=$(cat ./${TMP_FILE} | jq -r '.TOBE.REPLACED')
        OUTPUT_RAW=$(cat ./${TMP_FILE})
        #echo "OUTPUT: ${OUTPUT}"
        #echo "---------------------------"
        #echo "OUTPUT_RAW:"
        #cat ${OUTPUT_RAW}


        if [ "${OUTPUT}" = "${OUTPUT_CHECK}" ]; then
            VERIFY="valid response content"
        else
            VERIFY="invalid response content"          
            echo "----------------------------"
            log_date=$(date +'%F %H:%M:%S')
            echo "${log_date} Error" >> ${ERROR_LOG_FILE}
            echo ""
            echo "Run: ${RUN}" >> ${ERROR_LOG_FILE}
            echo "Endpoint: ${CE_HOST}" >> ${ERROR_LOG_FILE}
            echo "" >> ${ERROR_LOG_FILE}
            echo "----- Command ----" >> ${ERROR_LOG_FILE}
            echo "curl -X POST -u \"apikey:${API_KEY}\" --header \"Content-Type: application/json\" --data \"{ \"query\": \"text:${QUESTION}\" }\" \"https://${CE_HOST}/${API_CALL}\"" >> ${ERROR_LOG_FILE}
            echo "----- Output ----" >> ${ERROR_LOG_FILE}
            echo "" >> ${ERROR_LOG_FILE}
            echo "${OUTPUT_RAW}" >> ${ERROR_LOG_FILE}
            echo "" >> ${ERROR_LOG_FILE}
            CODEENGINE_APP_NAME=${CE_HOST%${CE_DOMAIN}}
            echo "CE APP: ${CODEENGINE_APP_NAME}"
            echo "--- CE APP: ${CODEENGINE_APP_NAME} ---" >> ${ERROR_LOG_FILE}
            echo "" >> ${ERROR_LOG_FILE}
            #echo "all namespace kubectl information"
            #echo ""
            #kube_information >> ${ERROR_LOG_FILE}
            #echo ""
            echo "--- kubectl first pod information ---" >> ${ERROR_LOG_FILE}
            kube_pod_log >> ${ERROR_LOG_FILE}
            echo "--- CE app log ---" >> ${ERROR_LOG_FILE}
            ce_log >> ${ERROR_LOG_FILE}
        fi
        
        end_time=$(date "+%s") 
        duration_time=$(( end_time - start_time))
        log_date=$(date +'%F %H:%M:%S')
        echo "${log_date}"
        echo "Run: ${RUN} Endpoint: ${CE_HOST} Duration: ${duration_time} Response: ${VERIFY}"
        echo "------------------------------------------------------------------------"
        echo "${RUN},${CE_HOST},${QUESTION},${API_CALL},${start_time},${duration_time},\"${VERIFY}\"" >> ${LOG_FILE}
    fi
done < ${CSV_FILE}
rm $TMP_FILE


