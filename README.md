# Simple `question-answering pipeline` using inside search and prompt with a Large Langauge Model.

This project contains a simple example implementation for a simple `question-answering pipeline` using `inside-search` (`IBM Cloud Watson Discovery`) and `prompt` (`IBM Watsonx` with `prompt-lab`).

## 1. Objective

The objective is to implement that elementary `question-answering pipeline` example by showing how to consume existing REST APIs and create a REST API with [`fastAPI`](https://github.com/tiangolo/fastapi) and `Python` because [`Python`](https://www.python.org) is well known in the AI world.

>Note: An excellent and detailed example implementation for a `question-answering pipeline` implementation in the [`question-answering project`](https://github.com/nheidloff/question-answering). That project contains many more details and integrations; the `question-answering pipeline` is implemented in Java.
The project also provides an example implementation for an experiment execution for the question-answering pipeline called `experiment-runner` implemented in Python. [Niklas Heidloff](https://heidloff.net) has written many awesome blog posts about AI and this [`question-answering project`](https://github.com/nheidloff/question-answering). I recommend briefly looking at the related blog post to this project.

## 2. Simplified Architecture

The `simple-qa-pipeline` creates an answer to a question using a [Large Language Model]() inside [Watsonx with the Prompt lab](https://dataplatform.cloud.ibm.com/docs/content/wsj/getting-started/welcome-main.html?context=wx&audience=wdp) and it searches for documents with Watson Discovery.

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
python3.11 -m venv simple-pipeline-env-3.11
source ./simple-pipeline-env-3.11/bin/activate
```

* Install needed Python libs and create a `requirements.txt` file

```sh
python3 -m pip install --upgrade pip
python3 -m pip install "fastapi[all]"
python3 -m pip install requests
python3 -m pip install pydantic
python3 -m pip freeze > requirements.txt 
```

```sh
python3 -m pip install --upgrade pip
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
# WatsonX
export WATSONX_URL="https://us-south.ml.cloud.ibm.com/ml/v1-beta/generation/text"
export WATSONX_LLM_NAME=google/flan-ul2
export WATSONX_MIN_NEW_TOKENS=1
export WATSONX_MAX_NEW_TOKENS=300
export WATSONX_PROMPT="Document:\n\n<<CONTEXT>>\n\nQuestion:\n\n<<QUESTION>>\n\nAnswer:\n\n"
export WATSONX_PROJECT_ID=
export WATSONX_VERSION="2023-05-29"
# IBM Cloud
export IBMCLOUD_APIKEY=
# APP
export APP_USER=admin
export APP_APIKEY=admin
```

### 3.3 Run `simple-qa-pipeline` server

```sh
source .env
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
* Open the `Watsonx Prompt lab` and insert the following prompt.

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

### 3.5.2 Watsonx instance

1. Visit the [Watsonx link](https://www.ibm.com/watsonx) and get a free trial.
2. A `Sandbox project` will be created for you called `Sandbox`
3. The Watsonx documentation is available on [IBM Cloud](https://dataplatform.cloud.ibm.com/docs/content/wsj/getting-started/welcome-main.html?context=wx&audience=wdp)
4. [Open Prompt lab](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/fm-prompt-lab.html?context=wx&audience=wdp)
5. Open view code
![](/images/watsonx-01.gif)
6. [Create an IBM Cloud API key](https://www.ibm.com/docs/en/app-connect/container?topic=servers-creating-cloud-api-key)
![]()

* With Watsonx sandbox project creation following services will be instantiated in your IBM Cloud Account:

  * [Watson Studio](https://www.ibm.com/products/watson-studio)
  * [Watson Machine Learning](https://cloud.ibm.com/catalog/services/watson-machine-learning)
  * [Cloud Object Storage](https://cloud.ibm.com/docs/cloud-object-storage?topic=cloud-object-storage-getting-started-cloud-object-storage)
  The gif below shows how you can access Watsonx from your Watson Studion in your IBM Cloud Account.
  ![](/images/watsonx-03.gif)

* Simplified dependencies of the created Watonx environment

![](/images/simple-pipeline-watsonx-dependencies.drawio.png)

## 4. Useful tools

  * [`curl-converter`](https://curlconverter.com/)

## 5. Summary

With [`fastAPI`](https://github.com/tiangolo/fastapi) and `Python` was easy and fasted to implement the `simple-qa-pipeline`.
With the automated created Swagger documentation, manually testing the `REST API` for the `simple-qa-pipeline` was easy.
We can download the OpenAPI spec directly and use its `REST API` in other integration scenarios like BYOS with Watson Assistant.

The good REST API documentation from IBM Cloud and Watsonx made it easy to use them even without the SDK.