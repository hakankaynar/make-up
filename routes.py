from flask import Flask, jsonify, make_response
from flask_restful import Api

from product.product_api import ProductApi
from product.products_api import ProductsApi

app = Flask(__name__)
api = Api(app)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


api.add_resource(ProductApi, '/api/v1.0/product/<int:product_id>', endpoint='product_ep')
api.add_resource(ProductApi, '/api/v1.0/product', endpoint='product_add_ep')
api.add_resource(ProductsApi, '/api/v1.0/products', endpoint='products_ep')

if __name__ == '__main__':
    app.run(debug=True)
