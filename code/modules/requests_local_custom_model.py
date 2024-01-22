from transformers import AutoModelForCausalLM, AutoTokenizer
from .load_env import load_custom_model_env

def custom_model_load( modelname_or_modelpath):
    model = AutoModelForCausalLM.from_pretrained(modelname_or_modelpath,
                                                 device_map="cuda", #auto, balanced
                                                 trust_remote_code=False,
                                                 revision="main")
    tokenizer = AutoTokenizer.from_pretrained(modelname_or_modelpath, use_fast=True)
    return tokenizer, model

def custom_model_simple_prompt( text, question, modelname_or_modelpath):
    
    model, tokenizer = custom_model_load( modelname_or_modelpath)
    custom_model_env, verification = load_custom_model_env()

    prompt_context_replace_template="<<CONTEXT>>"
    prompt_question_replace_template="<<QUESTION>>"
    input_txt=""
    documents_txt=text

    # Build the prompt with context text and question
    prompt = custom_model_env["CUSTOM_MODEL_PROMPT"]
    input_txt = prompt.replace(prompt_context_replace_template,documents_txt)
    data_input = input_txt.replace(prompt_question_replace_template,question)

    input_ids = tokenizer(data_input, return_tensors='pt').input_ids.cuda()
    output = model.generate(inputs=input_ids, temperature=0.7, 
                            do_sample=True, 
                            top_p=0.95, 
                            top_k=40, 
                            max_new_tokens=512)
    answer = tokenizer.decode(output[0])
    print(f"*** LOG: {answer}")
    return answer, verification

