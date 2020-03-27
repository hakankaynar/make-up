import os
from elasticsearch import Elasticsearch


class ElasticSearchFactory:

    @staticmethod
    def create():
        host = os.getenv('MU_ES_HOST', 'localhost')
        port = os.getenv('MU_ES_PORT', '9200')
        return Elasticsearch([host], port=int(port))

