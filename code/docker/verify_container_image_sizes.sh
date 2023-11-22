#!/bin/bash

export ENGINE=docker
#export ENGINE=podman
#podman machine rm
#podman machine init
#podman machine start

${ENGINE} build -f ./Dockerfile -t simple-pipeline-full:1.0.0 ./..
${ENGINE} build -f ./Dockerfile.optimized -t simple-pipeline-optimized:1.0.0 ./..

${ENGINE} images | grep simple-pipeline-full
${ENGINE} images | grep simple-pipeline-optimized