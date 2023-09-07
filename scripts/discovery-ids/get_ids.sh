#!/bin/bash

# Source: https://suedbroecker.net/2023/05/12/show-the-collection-ids-of-ibm-cloud-watson-discovery-projects-using-curl/
source ./.env

ibmcloud login (-sso)
ibmcloud target -r ${REGION} -g ${GROUP}

WATSON_DISCOVERY_INSTANCE_ID=$(ibmcloud resource service-instance ${DISCOVERY_SERVICE_NAME} | grep "GUID" | awk '{print $2;}')
OAUTHTOKEN=$(ibmcloud iam oauth-tokens | awk '{print $4;}')
 
DISCOVERY_URL="https://api.$REGION.discovery.watson.cloud.ibm.com/instances/$WATSON_DISCOVERY_INSTANCE_ID"
VERSION="2023-03-31"
curl -X GET -H "Authorization: Bearer $OAUTHTOKEN" "$DISCOVERY_URL/v2/projects?version=$VERSION"

OAUTHTOKEN=$(ibmcloud iam oauth-tokens | awk '{print $4;}')
 
echo "Enter the project id you want to use: "
read PROJECT_ID
 
curl -X GET -H "Authorization: Bearer $OAUTHTOKEN" "$DISCOVERY_URL/v2/projects/$PROJECT_ID/collections?version=$VERSION"



