from .product_model import Product
from elasticsearch.exceptions import NotFoundError
from .elastic_search_factory import ElasticSearchFactory
from elasticsearch import Elasticsearch


class ProductData:

    def __init__(self):
        self.__es = ElasticSearchFactory.create()

    def insert(self, product: Product):
        res = self.__es.index(index="test-index", id=product.id, body=product.to_json())
        if res['result'] == 'created':
            return product

    def get(self, product_id):
        try:
            res = self.__es.get(index="test-index", id=product_id)
            return Product(res['_source']['id'], res['_source']['name'])
        except NotFoundError:
            return None

    def delete(self, product_id):
        try:
            res = self.__es.delete(index="test-index", id=product_id)
            if res['result'] == 'deleted':
                return product_id
        except NotFoundError:
            return None

    def list_all(self):
        try:
            res = self.__es.search(index="test-index", body={"query": {"match_all": {}}})
            return ProductData.__to_product_array(res)
        except NotFoundError:
            return None

    @staticmethod
    def __to_product_array(res):
        products = []

        for hit in res['hits']['hits']:
            products.append(Product(hit["_source"]['id'], hit["_source"]['name']))

        return products
