from flask_restful import Resource
from flask import abort, request

from .product_service import ProductService
from .product_model import Product


class ProductApi(Resource):
    product_service = ProductService()

    def get(self, product_id):

        if product_id is None:
            abort(400)

        product = self.product_service.get(product_id)

        if product is None:
            abort(404)

        return to_json(product)

    def delete(self, product_id):

        if product_id is None:
            abort(400)

        product_id = self.product_service.delete(product_id)

        if product_id is None:
            abort(404)

        return {'id' : product_id}

    def post(self):

        if request.json is None:
            abort(400)

        product = Product(int(request.json['id']), request.json['name'])
        self.product_service.add(product)

        return to_json(product)


def to_json(product):
    return {'id': product.id, 'name': product.name}
