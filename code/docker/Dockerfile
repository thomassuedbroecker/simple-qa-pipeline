FROM python:3.11.2-slim-buster

# Install needed environment
RUN apt-get -y update; apt-get -y install curl
RUN python -m pip install --upgrade pip
RUN python -m pip install requests
RUN python -m pip install --upgrade pip
RUN python -m pip install "fastapi[all]"
RUN python -m pip install requests
RUN python -m pip install pydantic
RUN python -m pip freeze > requirements.txt 

# Set directory
WORKDIR /app

# Create modeles folder
RUN mkdir modules

WORKDIR /app
COPY /../simple-qa-pipeline.py /
COPY /../modules/apis_payload.py /
COPY /../modules/load_env.py /
COPY /../modules/requests_discovery.py /
COPY /../modules/requests_ibmcloud_token.py /
COPY /../modules/requests_watsonx.py /

WORKDIR /app
EXPOSE 8081
CMD ["/bin/sh","docker_entrypoint.sh"]