import os
from elasticsearch import Elasticsearch

elastic_search_singleton = None


def get_es_instance():
    global elastic_search_singleton

    if elastic_search_singleton is None:
        host = os.getenv('MU_ES_HOST', 'localhost')
        port = os.getenv('MU_ES_PORT', '9200')
        elastic_search_singleton = Elasticsearch([host], port=int(port))

    return elastic_search_singleton
