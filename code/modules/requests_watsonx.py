import requests 
from .load_env import load_watson_x_env
from .requests_ibmcloud_token import get_token

def watsonx_simple_prompt(text, question):
    watsonx_env, verification = load_watson_x_env()

    prompt_context_replace_template="<<CONTEXT>>"
    prompt_question_replace_template="<<QUESTION>>"
    input_txt=""
    documents_txt=text
    
    if (verification):

        # 1. Load environment variables
        url = watsonx_env["WATSONX_URL"]
        print(f"***LOG: - url: {url}")

        # 2. Get access token
        token, verification = get_token()
        apikey = "Bearer " + token["result"]
        #print(f"***LOG: - API KEY: {apikey}")
        print(f"***LOG: - Verification: {verification}")

        if ( verification["status"] == True):
            apikey = "Bearer " + token["result"]
            model_id = watsonx_env["WATSONX_LLM_NAME"]
            print(f"***LOG: - Url: {model_id}")
            min_tokens = watsonx_env["WATSONX_MIN_NEW_TOKENS"]
            print(f"***LOG: - Min_tokens: {min_tokens}")
            max_tokens = watsonx_env["WATSONX_MAX_NEW_TOKENS"]
            print(f"***LOG: - Max_tokens: {max_tokens}")
            prompt = watsonx_env["WATSONX_PROMPT"]
            print(f"***LOG: - Prompt: {prompt}")
            project_id = watsonx_env["WATSONX_PROJECT_ID"]
            print(f"***LOG: - Project_id: {project_id}")
            version = watsonx_env["WATSONX_VERSION"]
            print(f"***LOG: version: {version}")

            # 3. Build the header with authenication       
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Authorization": apikey
            }

            # 4. Build the params
            params = {
                 "version": version
            }
        
            # 5. Build the prompt with context documents and question
            input_txt = prompt.replace(prompt_context_replace_template,documents_txt)
            data_input = input_txt.replace(prompt_question_replace_template,question)
        
            print(f"***LOG: - Prompt input: \n{data_input}\n\n")
        
            # 6. Create payload
            json_data = {
                    "model_id": model_id,
                    "input": data_input,
                    "parameters":{
                        "decoding_method": "greedy",
                        "min_new_tokens": int(min_tokens),
                        "max_new_tokens": int(max_tokens),
                        "beam_width": 1 
                    },
                     "project_id": project_id      
            }
     
            # 6. Invoke REST API
            response = requests.post(
                url,
                headers=headers,
                params=params,
                json=json_data
            )

            print(f"***LOG: Response: \n{response}\n\n")
                
            # 7. Verify result and extract answer from the return vaule
            if (response.status_code == 200):
                    data_all=response.json()
                    results = data_all["results"]
                    data = results[0]["generated_text"]
                    verification = True
            else:
                    verification = False
                    data=response.json()
    else:
        verification = False
        data="no access token available"

    return { "result": data} , {"status":verification} 

def watsonx_prompt(documents, question):
    watsonx_env, verification = load_watson_x_env()
    data={}
    
    prompt_context_replace_template="<<CONTEXT>>"
    prompt_question_replace_template="<<QUESTION>>"
    
    input_txt=""
    documents_txt=""

    info=documents["result"]
    print(f"***LOG: watsonx_prompt documents\n{info}\n\n")
    
    i = 0
    for item in documents["result"]:
                text_array = item["text"]
                text = text_array[0]
                documents_txt = documents_txt + " \n" +  text + " \n"
                i = i + 1
    
    print(f"***LOG: watsonx_prompt documents_txt \n{documents_txt}\n\n")
    print(f"***LOG: watsonx_prompt verification \n{verification}\n\n")

    if ( verification == True):
        
        # 1. Load environment variables
        url = watsonx_env["WATSONX_URL"]
        print(f"***LOG: - url: {url}")

        # 2. Get access token
        token, verification = get_token()
 
        print(f"***LOG: verification \n{verification}\n\n")
        print(f"***LOG: token \n{token}\n\n")

        if ( verification["status"] == True):
              
              apikey = "Bearer " + token["result"]
              model_id = watsonx_env["WATSONX_LLM_NAME"]
              min_tokens = watsonx_env["WATSONX_MIN_NEW_TOKENS"]
              max_tokens = watsonx_env["WATSONX_MAX_NEW_TOKENS"]
              prompt = watsonx_env["WATSONX_PROMPT"]
              project_id = watsonx_env["WATSONX_PROJECT_ID"]
              version = watsonx_env["WATSONX_VERSION"]

              # 3. Build the header with authenication       
              headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Authorization": apikey
              }
        
              # 4. Build the prompt with documents
              input_txt = prompt.replace(prompt_context_replace_template,documents_txt)
              data_input = input_txt.replace(prompt_question_replace_template,question)

              print(f"***LOG: watsonx_prompt Datadata_input\n{data_input}\n\n")

              # 5. Build the params
              params = {
                 "version": version
              }
        
              # 6. Create payload
              json_data = {
                "model_id": model_id,
                "input": data_input,
                "parameters":{
                    "decoding_method": "greedy",
                    "min_new_tokens": int(min_tokens),
                    "max_new_tokens": int(max_tokens),
                    "stop_sequences": [],
                    "repetition_penalty": 1,
                },
                "project_id": project_id                
              }
        
              # 7. Invoke REST API
              response = requests.post(
                url,
                headers=headers,
                params=params,
                json=json_data
              )

              print(f"***LOG: watsonx_prompt Answer response: \n{response}\n\n")
                
              # 8. Verify result and extract answer from the return value
              if (response.status_code == 200):
                    data_all=response.json()
                    results = data_all["results"]
                    data = results[0]["generated_text"]
                    verification = True
                    return {"result": data} , {"status":verification} 
              else:
                    verification = False
                    data="WATSONX DOESN'T PROVIDE AN ANSWER"
                    return {"result": data} , {"status":verification}             
    else:
        verification = False
        data = "no access token available"

    return {"result": data} , {"status":verification} 

