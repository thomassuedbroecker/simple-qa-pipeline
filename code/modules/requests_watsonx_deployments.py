import requests

from .requests_ibmcloud_token import get_token
from .load_env import load_watsonx_deployment_env

def get_answer_from_watsonx_deployment( context , question ):
    
    token, verification_token = get_token()
    apikey = "Bearer " + token["result"]
    
    if (verification_token):
        watsonx_deployment, verification_watsonx_deployment = load_watsonx_deployment_env()

        if (verification_watsonx_deployment):

            print(f" verification_watsonx_deployment: {verification_watsonx_deployment}")


            headers = {"Content-Type": "application/json", 
                       "Accept":"application/json", 
                       "Authorization": apikey }
            
            payload = {"input_data":[{"fields":[ context ],
                                      "values": [ question ]
                                     }]}
            
            print(f"*** LOG: payload {payload}")
            print(f"*** LOG:  url {watsonx_deployment['WATSONX_DEPLOYMENT_URL']}")
                      
            response = requests.post({watsonx_deployment['WATSONX_DEPLOYMENT_URL']}, 
                                     json=payload,
                                     headers=headers)
            
            print(f"*** LOG: {response.content}")

            # Verify result and extract answer from the return vaule
            if (response.status_code == 200):
                    data = response.json()
                    print(f"***LOG: Scoring response")
                    print(f"***LOG: {response.json()}")
                    verification = True
            else:
                    verification = False
                    data=response.json()
    else:
        verification = False
        data="no access token available"

    return { "result": data} , {"status":verification} 