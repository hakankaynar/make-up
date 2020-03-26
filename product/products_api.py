from flask_restful import Resource
from flask import abort, jsonify


from .product_service import ProductService


class ProductsApi(Resource):
    __service = ProductService()

    def get(self):

        products = self.__service.list()

        if products is None:
            abort(404)

        return jsonify(products=[e.to_json() for e in products])
