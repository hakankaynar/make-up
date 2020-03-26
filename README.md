curl --header "Content-Type: application/json" --request POST \
--data '{"id":3,"name":"asd"}' http://localhost:5000/api/v1.0/products

docker run --rm --name elastic-search --net elastic-search -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" elasticsearch:7.6.1

export PYTHONPATH=${PYTHONPATH}:/Users/hakankaynar/PycharmProjects/make-up-product

python -m unittest discover './test' '*_test.py'
coverage run -m unittest discover './test' '*_test.py'
coverage report --include **/product/*.py  --fail-under 90
printf '%d\n' $?
