from pydantic import BaseModel
from typing import List

### Sub type specifictions

#class Document(BaseModel):
#     text: str 
#     title: str 
#     document_url: str

class BasicResult(BaseModel):
    result: str

class Result(BaseModel):
    result: List[dict]

class Status (BaseModel):
    status: bool

### Responses

class Get_discovery_config(BaseModel):
    discovery_config: dict
    validation: bool

class Get_ibmcloud_config(BaseModel):
    ibmcloud_config: dict 
    validation: bool

class Run_discovery_query(BaseModel):
     context_documents: Result
     validation: Status

class Get_simple_answer(BaseModel):
    answer: BasicResult
    validation: Status

class Get_access_token(BaseModel):
    token: BasicResult
    validation: Status

class Get_pipeline_answer(BaseModel):
    answer: dict
    context_documents: Result

class Health(BaseModel):
    status: str