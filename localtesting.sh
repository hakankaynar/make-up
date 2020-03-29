#!/bin/bash
NO_DOCKER="false"

if [ "$1" = "no-docker" ]; then
  NO_DOCKER="true"
fi

echo "Setting up virtial environment"
python3 -m venv venv && source venv/bin/activate

echo "Installing requirements"
pip3 install -r requirements.txt

if [ "$NO_DOCKER" = "false" ]; then
  echo "Creating docker elastic search network"
  docker network create elastic-search

  echo "Running elastic search"
  docker run --rm -d --name elastic-search --net elastic-search -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" elasticsearch:7.6.1

  echo "Waiting 30 seconds"
  sleep 30
fi

echo "Configuring python path"
export PYTHONPATH=${PYTHONPATH}:.

echo "Running the tests"
python3 -m coverage run -m unittest discover './test' '*_test.py'

echo "Reporting coverage"
python3 -m coverage report --include **/product/*.py  --fail-under 90

if [ "$NO_DOCKER" = "false" ]; then
  echo "Stopping elastic search"
  docker container stop elastic-search
fi
