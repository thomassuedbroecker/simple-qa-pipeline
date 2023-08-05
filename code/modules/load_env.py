import os

def load_ibmcloud_env():
       if (os.environ.get("IBMCLOUD_APIKEY") == None):
            IBMCLOUD_APIKEY = ''
       else:
            IBMCLOUD_APIKEY = os.environ.get("IBMCLOUD_APIKEY")
        
       if (os.environ.get("IBMCLOUD_URL") == None):
            IBMCLOUD_URL = ''
       else:
            IBMCLOUD_URL = os.environ.get("IBMCLOUD_URL")

       if ((IBMCLOUD_APIKEY=='') or (IBMCLOUD_URL=='')):
            configurationStatus = False
       else:
            configurationStatus = True
    
       configurationJSON = { "IBMCLOUD_APIKEY": IBMCLOUD_APIKEY,
                             "IBMCLOUD_URL": IBMCLOUD_URL}
       
       return configurationJSON, configurationStatus


def load_watson_x_env():
    if (os.environ.get("WATSONX_URL") == None):
            WATSONX_URL = ''
    else:
            WATSONX_URL = os.environ.get("WATSONX_URL")

    if (os.environ.get("WATSONX_VERSION") == None):
            WATSONX_VERSION = ''
    else:
            WATSONX_VERSION = os.environ.get("WATSONX_VERSION")

    if (os.environ.get("WATSONX_PROJECT_ID") == None):
            WATSONX_PROJECT_ID = ''
    else:
            WATSONX_PROJECT_ID = os.environ.get("WATSONX_PROJECT_ID")

    if (os.environ.get("WATSONX_LLM_NAME") == None):
            WATSONX_LLM_NAME = ''
    else:
            WATSONX_LLM_NAME = os.environ.get("WATSONX_LLM_NAME")

    if (os.environ.get("WATSONX_MIN_NEW_TOKENS") == None):
            WATSONX_MIN_NEW_TOKENS = ''
    else:
            WATSONX_MIN_NEW_TOKENS = os.environ.get("WATSONX_MIN_NEW_TOKENS")

    if (os.environ.get("WATSONX_MAX_NEW_TOKENS") == None):
            WATSONX_MAX_NEW_TOKENS = ''
    else:
            WATSONX_MAX_NEW_TOKENS = os.environ.get("WATSONX_MAX_NEW_TOKENS")

    if (os.environ.get("WATSONX_PROMPT") == None):
            WATSONX_PROMPT = ''
    else:
            WATSONX_PROMPT = os.environ.get("WATSONX_PROMPT")
    
    if ((WATSONX_URL=='') or
        (WATSONX_LLM_NAME=='') or 
        (WATSONX_MIN_NEW_TOKENS=='') or 
        (WATSONX_MAX_NEW_TOKENS=='') or 
        (WATSONX_PROMPT=='') or
        (WATSONX_VERSION=='') or
        (WATSONX_PROJECT_ID=='')):
            configurationStatus = False
    else:
            configurationStatus = True
    
    configurationJSON = { "WATSONX_URL": WATSONX_URL,
                          "WATSONX_LLM_NAME":WATSONX_LLM_NAME,
                          "WATSONX_MIN_NEW_TOKENS":WATSONX_MIN_NEW_TOKENS,
                          "WATSONX_MAX_NEW_TOKENS":WATSONX_MAX_NEW_TOKENS,
                          "WATSONX_PROMPT":WATSONX_PROMPT,
                          "WATSONX_PROJECT_ID":WATSONX_PROJECT_ID,
                          "WATSONX_VERSION":WATSONX_VERSION
                        }

    return configurationJSON, configurationStatus

def load_watson_discovery_env():
    if (os.environ.get("DISCOVERY_API_KEY") == None):
            DISCOVERY_API_KEY = ''
    else:
            DISCOVERY_API_KEY = os.environ.get("DISCOVERY_API_KEY")
    
    if (os.environ.get("DISCOVERY_COLLECTION_ID") == None):
            DISCOVERY_COLLECTION_ID = ''
    else:
            DISCOVERY_COLLECTION_ID = os.environ.get("DISCOVERY_COLLECTION_ID")
    
    if (os.environ.get("DISCOVERY_PROJECT") == None):
            DISCOVERY_PROJECT = ''
    else:
            DISCOVERY_PROJECT = os.environ.get("DISCOVERY_PROJECT")
    
    if (os.environ.get("DISCOVERY_INSTANCE") == None):
            DISCOVERY_INSTANCE = ''
    else:
            DISCOVERY_INSTANCE = os.environ.get("DISCOVERY_INSTANCE")
    
    if (os.environ.get("DISCOVERY_URL") == None):
            DISCOVERY_URL = ''
    else:
            DISCOVERY_URL = os.environ.get("DISCOVERY_URL")
    
    if ((DISCOVERY_URL=='') or 
        (DISCOVERY_INSTANCE=='') or 
        (DISCOVERY_PROJECT=='') or 
        (DISCOVERY_COLLECTION_ID=='') or 
        (DISCOVERY_API_KEY=='')):
            configurationStatus = False
    else:
            configurationStatus = True
    
    configurationJSON = { "DISCOVERY_URL": DISCOVERY_URL,
                          "DISCOVERY_INSTANCE":DISCOVERY_INSTANCE,
                          "DISCOVERY_PROJECT":DISCOVERY_PROJECT,
                          "DISCOVERY_COLLECTION_ID":DISCOVERY_COLLECTION_ID,
                          "DISCOVERY_API_KEY":DISCOVERY_API_KEY
                        }

    return configurationJSON, configurationStatus

def load_apikey_env():
    if (os.environ.get("APP_USER") == None):
            USER = "admin"
    else:
            USER = os.environ.get("APP_USER")
    
    if (os.environ.get("APP_APIKEY") == None):
            APIKEY = "apikey"
    else:
            APIKEY = os.environ.get("APP_APIKEY")
    
    if ((USER=="admin") or 
        (APIKEY=="apikey")):
            authenicationStatus = False
    else:
            authenicationStatus = True
    
    authenicationJSON = { "USER": USER,
                          "APIKEY":APIKEY
                        }
    print(authenicationJSON)

    return authenicationJSON, authenicationStatus