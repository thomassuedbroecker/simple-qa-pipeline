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
     length: str
     validation: Status

# Example return value
#  "context_documents": {
#    "result": [
#      {
#        "text": "Text",
#        "title": "Title",
#        "document_url: "URL"
#       }
#     ]
#  },
#  "length": "4",
#  "validation": {
#      "status": true
#  }


class Get_simple_answer(BaseModel):
    answer: BasicResult
    validation: Status
# Example return value
#{
#  "answer": {
#    "result": "answer"
#  },
#  "validation": {
#    "status": true
#  }
#}

class Get_access_token(BaseModel):
    token: BasicResult
    validation: Status

class Get_pipeline_answer(BaseModel):
    answer: dict
    length: str
    context_documents: Result

# Example return value
#  {
#    "answer": {
#      "result": "Answer text"
#    },
#    "length": "4"
#    "context_documents": {
#      "result": [
#        {
#          "text": "Text",
#          "title": "Title",
#          "url": "URL"
#        },
#        {
#            "text": "Text",
#            "title": "Title",
#            "url": "URL"
#        }
#      ]
#    }
#   }
#

class Health(BaseModel):
    status: str