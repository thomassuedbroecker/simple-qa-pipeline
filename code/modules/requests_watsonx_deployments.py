import requests
from fastapi.exceptions import ResponseValidationError

from .requests_ibmcloud_token import get_token
from .load_env import load_watsonx_deployment_env

def get_answer_from_watsonx_deployment( context , question ):
    
    token, verification_token = get_token()
    apikey = "Bearer " + token["result"]
    
    
    if (verification_token):
        watsonx_deployment, verification_watsonx_deployment = load_watsonx_deployment_env()
        version = watsonx_deployment["WATSONX_DEPLOYMENT_VERSION"]
        url = watsonx_deployment['WATSONX_DEPLOYMENT_URL']

        if (verification_watsonx_deployment):

            try:
                print(f"***LOG: verification_watsonx_deployment: {verification_watsonx_deployment}")

                headers = { "Content-Type": "application/json", 
                            "Authorization": apikey }
                
                payload = {"input_data":[{ "fields":[ context ],
                                           "values":[ [ question ] ]
                                         }]}
                
                params = {
                    "version": version
                }
                
                print(f"*** LOG: header\n{headers}")
                print(f"*** LOG: payload\n{payload}")
                print(f"*** LOG: url\n{url}\n")
                        
                response = requests.post( url, 
                                          json=payload,
                                          params=params,
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

            except Exception as e:
                error = {"Exception": e }                  
                response = str(error)
                verification = False
                return { "result": response }, {"status":verification}  
    
    else:
        verification = False
        data="no access token available"

    return { "result": str(data)} , {"status":verification} 