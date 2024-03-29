# Simple `question-answering pipeline` using inside search and prompt with a Large Langauge Model.

This project contains a simple example implementation for a simple `question-answering pipeline` using an `inside-search` (`IBM Cloud Watson Discovery`) and a `prompt` (`IBM watsonx` with `prompt-lab`) to create an answer.

Related blog post: [IBM watsonx and a simple question-answering pipeline using Python and FastAPI](https://wp.me/paelj4-21Y)

## 1. Objective

The objective is to implement an elementary `question-answering pipeline` example by showing how to consume existing REST APIs and create a REST API with [`FastAPI`](https://github.com/tiangolo/FastAPI) and `Python` because `Python` is well-known in the AI world.

>Note: An excellent and detailed example implementation for a `question-answering pipeline` in the [`question-answering project`](https://github.com/nheidloff/question-answering). That project contains many more details and integrations; the `question-answering pipeline` is implemented in Java.
The project also provides an example implementation for an experiment execution for the question-answering pipeline the service for the execution is called `experiment-runner` and is implemented in Python. [Niklas Heidloff](https://heidloff.net) has written many awesome blog posts about AI and this [`question-answering project`](https://github.com/nheidloff/question-answering). I recommend briefly looking at the related blog posts to this project.

## 2. Simplified Architecture

The `simple-qa-pipeline` creates an answer to a question using a [Large Language Model]() inside [watsonx with the Prompt lab](https://dataplatform.cloud.ibm.com/docs/content/wsj/getting-started/welcome-main.html?context=wx&audience=wdp) and it searches for documents with Watson Discovery to provide the context.

![](/images/simple-pipeline-pipeline.drawio.png)

## 3. Run the `simple-qa-pipeline` locally

### 3.1. Get the source code and create a virtual Python environment

* Clone project

```
git clone https://github.com/thomassuedbroecker/simple-pipeline.git
```

* Create a virtual Python environment

```sh
cd simple-pipeline/code
python3 -m venv simple-pipeline-env-3
source ./simple-pipeline-env-3/bin/activate
```

* Install needed Python libs and create a `requirements.txt` file

```sh
python3 -m pip install --upgrade pip
python3 -m pip install "fastapi[all]"
python3 -m pip install requests
python3 -m pip install pydantic
python3 -m pip install torch
python3 -m pip install accelerate
python3 -m pip install typing
python3 -m pip install transformers
#python3 -m pip install git+https://github.com/huggingface/transformers
```

* Save your configuration in requirements.txt

```sh
python3 -m pip install --upgrade pip
python3 -m pip freeze > requirements.txt
deactivate
```

* Install from configuration from requirements.txt

```sh
python3 -m pip install -r requirements.txt
```

### 3.2. Configure the `simple-qa-pipeline` to access the needed REST API by using environment variables

* Create `.env` file

```sh
cat ./.env-template > ./.env
```

* Outline of the environment file

```sh
# Discovery
export DISCOVERY_API_KEY=
export DISCOVERY_URL=https://api.us-east.discovery.watson.cloud.ibm.com/instances/
export DISCOVERY_COLLECTION_ID=
export DISCOVERY_PROJECT=
export DISCOVERY_INSTANCE=
# watsonx
export WATSONX_URL="https://us-south.ml.cloud.ibm.com/ml/v1-beta/generation/text"
export WATSONX_LLM_NAME=google/flan-ul2
export WATSONX_MIN_NEW_TOKENS=1
export WATSONX_MAX_NEW_TOKENS=300
export WATSONX_PROMPT="Document:\n\n<<CONTEXT>>\n\nQuestion:\n\n<<QUESTION>>\n\nAnswer:\n\n"
export WATSONX_PROJECT_ID=
export WATSONX_VERSION="2023-05-29"
# Watsonx deployment (Watson Studio Deployment)
export WATSONX_DEPLOYMENT_ID=
export WATSONX_DEPLOYMENT_URL=https://[XXX]${WATSONX_DEPLOYMENT_ID}[YYY]
export WATSONX_DEPLOYMENT_VERSION=2021-05-01
# Custom Model
export CUSTOM_MODEL_PROMPT="Code:\n\n<<CONTEXT>>\n\nQuestion:\n\n<<QUESTION>>\n\nAnswer:\n\n"
# IBM Cloud
export IBMCLOUD_APIKEY=
# APP
export APP_USER=admin
export APP_APIKEY=admin
export APPLOG=INFO
```

### 3.3 Run `simple-qa-pipeline` server

```sh
cd code
source ./simple-pipeline-env-3/bin/activate
source ./.env
python3 simple-qa-pipeline.py
```

* Open Swagger UI with the API documentation

```sh
open http://localhost:8081/docs
```

![](/images/watsonx-05.png)

### 3.4. Run a small test

* Question: `"What is your name?"`
* Context:  `"My name is Thomas."`

* Invoke the REST API endpoint `get_simple_answer` in the Swagger UI with the given values.
* Open the `watsonx Prompt lab` and insert the following prompt.

```
Document:

My name is Thomas.

Question:

What is your name?

Answer:


```

The following gif shows how the simple test works.

![](/images/watsonx-04.gif)

### 3.5. Setup the related IBM Cloud instance

This example uses [IBM Cloud](https://cloud.ibm.com/).

### 3.5.1 Watson Discovery service instance

There is no [`Lite plan`](https://www.ibm.com/cloud/free) available, but when you create a new IBM Cloud Account, you a [`free trial period`](https://www.ibm.com/products/watson-discovery), you can use.

* [Create a Watson Discovery instance](https://cloud.ibm.com/docs/discovery-data?topic=discovery-data-getting-started)
* Extract the project ID and collection ID
  * If you need additional help, you can visit my blog post [Show the collection IDs of IBM Cloud Watson Discovery projects using cURL](https://suedbroecker.net/2023/05/12/show-the-collection-ids-of-ibm-cloud-watson-discovery-projects-using-curl/)

### 3.5.2 watsonx instance

1. Visit the [watsonx link](https://www.ibm.com/watsonx) and get a free trial.
2. A `Sandbox project` will be created for you called `Sandbox`
3. The watsonx documentation is available on [IBM Cloud](https://dataplatform.cloud.ibm.com/docs/content/wsj/getting-started/welcome-main.html?context=wx&audience=wdp)
4. [Open Prompt lab](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/fm-prompt-lab.html?context=wx&audience=wdp)
5. Open view code
![](/images/watsonx-01.gif)
6. [Create an IBM Cloud API key](https://www.ibm.com/docs/en/app-connect/container?topic=servers-creating-cloud-api-key)

![](/images/watsonx-03.gif))

* With watsonx sandbox project creation following services will be instantiated in your IBM Cloud Account:

  * [Watson Studio](https://www.ibm.com/products/watson-studio)
  * [Watson Machine Learning](https://cloud.ibm.com/catalog/services/watson-machine-learning)
  * [Cloud Object Storage](https://cloud.ibm.com/docs/cloud-object-storage?topic=cloud-object-storage-getting-started-cloud-object-storage)
  The gif below shows how you can access watsonx from your Watson Studion in your IBM Cloud Account.
  ![](/images/watsonx-03.gif)

* Simplified dependencies of the created Watonx environment

![](/images/simple-pipeline-watsonx-dependencies.drawio.png)

## 4. Useful tools

  * [`curl-converter`](https://curlconverter.com/)

## 5. Summary

With [`FastAPI`](https://github.com/tiangolo/fastapi) and `Python` was easy and fasted to implement the `simple-qa-pipeline`.
With the automated created Swagger documentation, manually testing the `REST API` for the `simple-qa-pipeline` was easy.
We can download the OpenAPI spec directly and use its `REST API` in other integration scenarios like BYOS with Watson Assistant.

The good REST API documentation from IBM Cloud and watsonx made it easy to use them even without the SDK.

## 6. Additional resources

* [VS Code Python debugging](https://code.visualstudio.com/docs/python/debugging)
* [OpenAPI Swagger `array of strings`](https://stackoverflow.com/questions/39281532/specify-an-array-of-strings-as-body-parameter-in-swagger-api)
* [OpenAPI Swagger `array of objects`](https://stackoverflow.com/questions/63738715/how-to-define-an-array-of-objects-in-openapi-3-0)
* [OpenAPI Swagger `authentication`](https://swagger.io/docs/specification/authentication/)
* [OpenAPI Swagger `apikey authentication`](https://github.com/watson-developer-cloud/assistant-toolkit/blob/master/integrations/extensions/starter-kits/language-model-watsonx/watsonx-openapi.json#L14)
* [Required properties](https://stackoverflow.com/questions/40113049/how-to-specify-if-a-field-is-optional-or-required-in-openapi-swagger)
