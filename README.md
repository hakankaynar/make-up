![CI](https://github.com/hakankaynar/make-up/workflows/CI/badge.svg?branch=master)


## Step by step guide for running the application
* python3 -m venv myenv
* source myenv/bin/activate
* pip install -r requirements.txt 
* python routes.py 
* docker run --rm --name elastic-search --net elastic-search -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" elasticsearch:7.6.1

### Testing
* export PYTHONPATH=${PYTHONPATH}:{full_path_of_project}
* python -m unittest discover './test' '*_test.py'
* coverage run -m unittest discover './test' '*_test.py'
* coverage report --include **/product/*.py  --fail-under 90

### Product Api

#### Adding a product
curl --header "Content-Type: application/json" --request POST \
--data '{"id":3,"name":"asd"}' http://localhost:8000/api/v1.0/product

#### Getting a product 
curl http://localhost:8000/api/v1.0/product/3


### Docker image
* Building: docker build -f .docker/Dockerfile --tag proj1:1.1 .
* Running terminal: docker container run -it --rm --name proj1 -p 8000:8000 -e MU_ES_HOST=elastic-search --net elastic-search proj1:1.1
* Running already running: docker exec -it proj1 bash 



