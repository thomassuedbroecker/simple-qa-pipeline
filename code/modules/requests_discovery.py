import requests 
from .load_env import load_watson_discovery_env

def discovery_query(query_text):
    data, verification = load_watson_discovery_env()
    max_count=4

    if (verification):
        
        # 1. Load environment variables
        base_url = data["DISCOVERY_URL"]
        instance = data["DISCOVERY_INSTANCE"]
        apikey = data["DISCOVERY_API_KEY"]
        collection_id = data["DISCOVERY_COLLECTION_ID"]
        project_id = data["DISCOVERY_PROJECT"]

        # 2. Build endpoint
        endpoint = "v2/projects/" + project_id + "/query" 

        # 3. Build url
        url= base_url + instance + "/" + endpoint

        # 4. Save query
        query = "text:" + query_text
        
        # 5. Create payload
        json_data = {
            "collection_ids": [collection_id],
            "query": query
        }
        
        # 6. Define header
        headers = {
            "Content-Type": "application/json"
        }

        # 7. Define parameter
        params = {
            "version": "2023-03-31"
        }

        # 8. Invoke request       
        response = requests.post(
            url,
            params=params, 
            headers=headers, 
            json=json_data,
            auth=('apikey', apikey)
        )

        # 9. Extract reponse data
        return_data=[]
        i=1
        
        if (response.status_code == 200):
            data_all=response.json()
            #print(f"***LOG: Discovery data: {data_all}")
            data = data_all["results"]
            for item in data_all["results"]:
                text=item["text"]
                title=item["title"]
                document_url=item["url"]
                new_item={"text":text,"title":title,"url":document_url}
                return_data.append(new_item)
                i = i + 1
                if (i == max_count):
                    break
            data = return_data
            verification = True
        else:
            verification = False
            data=response.json
    else:
        verification = False
        data = [{"data":"discovery is not configured"}]

    return {"result": data} , {"status":verification} 