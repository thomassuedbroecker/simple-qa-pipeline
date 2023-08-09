from pydantic import BaseModel
from typing import List

class Get_discovery_config(BaseModel):
    discovery_config: dict
    validation: bool

class Get_ibmcloud_config(BaseModel):
    ibmcloud_config: dict 
    validation: bool

class Document:
     text: str | None = None
     title: str | None = None
     document_url: str | None = None

class Run_discovery_query(BaseModel):
    context_documents: List[Document] 
    validation: bool

class Get_simple_answer:
    answer: dict
    validation: dict

class Get_access_token:
    token: str | None = None
    validation: bool

class Get_pipeline_answer:
    answer: dict
    context_documents: list[Document]

class Health:
    status: str | None = None