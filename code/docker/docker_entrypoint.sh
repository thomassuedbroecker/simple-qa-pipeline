#!/bin/bash

CURRENT_USER=$(whoami)
#echo "Current user: $CURRENT_USER"

#echo "*********************"
#echo "** Create enviroment file "
#echo "*********************"

"/bin/sh" ./generate_env-config.sh > ./.env
#cat .env

echo "*********************"
echo "** Start Python server"
echo "*********************"
echo "Home: $(pwd)"
ls -a
python simple-qa-pipeline.py