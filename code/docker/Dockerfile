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

COPY ./../simple-qa-pipeline.py /app
COPY ./../modules/apis_payload.py.py /app/modules
COPY ./../modules/load_env.py /app/modules
COPY ./../modules/requests_discovery.py /app/modules
COPY ./../modules/requests_ibmcloud_token.py /app/modules
COPY ./../modules/requests_ibmcloud_token.py /app/modules

EXPOSE 8081
CMD ["/bin/sh","docker_entrypoint.sh"]