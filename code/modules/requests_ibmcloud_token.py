import requests 
from .load_env import load_ibmcloud_env

# curl -X POST 'https://iam.cloud.ibm.com/identity/token' -H 'Content-Type: application/x-www-form-urlencoded' -d 'grant_type=urn:ibm:params:oauth:grant-type:apikey&apikey=MY_APIKEY'
def get_token():
    ibmcloud_env, verification = load_ibmcloud_env()

    # 1. Load environment variables
    ibmcloud_apikey = ibmcloud_env["IBMCLOUD_APIKEY"]
    ibmcloud_url = ibmcloud_env["IBMCLOUD_URL"]

    #print(f"***LOG:\n get_token - ibmcloud_apikey: \n{ibmcloud_apikey}\n\n")
    
    # 2. Build endpoint
    endpoint = ibmcloud_url

    # 3. Define header
    headers = {
        "Content-Type":"application/x-www-form-urlencoded"
    }

    # 4. Create payload
    payload = 'grant_type=urn:ibm:params:oauth:grant-type:apikey&apikey=' + ibmcloud_apikey

    # 5. Create response
    response = requests.post( endpoint, headers=headers, data=payload)

    #print(f"***LOG:\n get_token - response: \n{response}\n\n")

    if (response.status_code == 200):
            data_all=response.json()
            #print(f"***LOG: IBM Cloud data: {data_all}")
            data = data_all["access_token"]
            verification = True
    else:
            verification = False
            data= "NO TOKEN AVAILABLE"

    return {"result": data} , {"status": verification} 



 



