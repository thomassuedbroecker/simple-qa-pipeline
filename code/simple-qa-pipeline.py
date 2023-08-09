from fastapi import Depends, HTTPException, FastAPI
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.status import HTTP_401_UNAUTHORIZED
##################################
# Custom modules
from modules.load_env import load_watson_discovery_env, load_apikey_env, load_watson_x_env
from modules.requests_discovery import discovery_query
from modules.requests_watsonx import watsonx_prompt, watsonx_simple_prompt
from modules.requests_ibmcloud_token import get_token, load_ibmcloud_env
from modules.apis_payload import Watsonx_simple_question, Discovery_question, Pipeline_question
from modules.apis_response_format import Get_access_token, Get_discovery_config,Get_ibmcloud_config, Get_pipeline_answer, Get_simple_answer, Run_discovery_query, Health

from typing import Any

##################################
# Set basic auth as security
security = HTTPBasic()
def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    data, verification = load_apikey_env()
    apikey = data["APIKEY"]
    user = data["USER"]
  
    if ((credentials.username != user) or (credentials.password != apikey)):
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED,
                            detail="incorrect user or apikey",
                            headers={"WWW-Authenticate":"Basic"})    
    return credentials.username

##################################
# Create APIs
app = FastAPI(dependencies=[Depends(authenticate)])
#app.debug = True

##################################
# Endpoints
@app.get("/")
def root_show_configuration_status():
    config, validation = load_watson_discovery_env()
    if (validation):
        status = "configured"
    else:
        status = "unconfigured"
    return{"status": status}

#@app.get("/health", response_model=Health) 
def provide_health_status() -> Any:
    status = "ok"

    return Health(status)

@app.get("/get_discovery_config", response_model=Get_discovery_config)
def get_discovery_config() -> Any: 
    config, validation = load_watson_discovery_env()

    return Get_discovery_config(config,validation)

@app.get("/get_ibmcloud_config", response_model=Get_ibmcloud_config)
def get_ibmcloud_config() -> Any:
    config, validation = load_ibmcloud_env()
    return {"ibmcloud_config":config, "validation":validation }


@app.post("/run_discovery_query/", response_model=Run_discovery_query)
async def run_a_discovery_query(discovery_question:Discovery_question) -> Any:
    data, validation = discovery_query(discovery_question.question)
    return {"context_documents":data, "validation":validation }

#@app.post("/get_simple_answer/", response_model=Get_simple_answer)
async def get_a_watsonx_answer(watsonx_simple_question:Watsonx_simple_question) -> Any:
    answer, validation = watsonx_simple_prompt(watsonx_simple_question.context,
                                               watsonx_simple_question.question)
    return {"answer":answer, "validation":validation}

#@app.get("/get_access_token", response_model=Get_access_token)
def get_an_ibm_cloud_access_token() -> Any:
    data, validation = get_token()
    return {"token":data, "validation":validation }

#@app.post("/get_pipeline_answer/", response_model=Get_pipeline_answer)
async def get_a_pipeline_discovery_watsonx_anwser(pipeline_question: Pipeline_question) -> Any:

    # 1. Search for context documents based on question
    context_documents, validation = discovery_query(pipeline_question.question)
    print(f"***LOG: Contect documents {context_documents}")
    print(f"***LOG: Validation {validation}")
    
    check = validation["status"]
    if ( check == False ):        
        return {"answer": "ERROR IN PIPELINE", "context_documents":context_documents}

    # 2. Create answer based on context documents
    answer, validation = watsonx_prompt(context_documents, pipeline_question.question)

    return {"answer": answer, "context_documents":context_documents}

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=8081)