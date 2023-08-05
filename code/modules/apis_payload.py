from pydantic import BaseModel

class Pipeline_question(BaseModel):
    question: str

class Watsonx_simple_question(BaseModel):
    question: str
    context: str

class Discovery_question(BaseModel):
    question: str