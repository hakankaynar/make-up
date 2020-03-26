import unittest

from product.product_api import ProductApi
from unittest.mock import Mock
from werkzeug.exceptions import BadRequest, NotFound


class ProductApiTest(unittest.TestCase):

    def testGet(self):
        mock_product = Mock()
        mock_product.id = 1
        mock_product.name = 'EXPECTED'

        mock_product_service = Mock()
        mock_product_service.get.return_value = mock_product

        product_api = ProductApi()
        product_api.product_service = mock_product_service

        expected = {'id': 1, 'name': 'EXPECTED'}
        self.assertEqual(product_api.get(1), expected)

    def testBadGet(self):
        product_api = ProductApi()

        self.assertRaises(BadRequest, product_api.get, None)

    def testBadId(self):
        mock_product_service = Mock()
        mock_product_service.get.return_value = None

        product_api = ProductApi()
        product_api.product_service = mock_product_service

        self.assertRaises(NotFound, product_api.get, 1)


if __name__ == '__main__':
    unittest.main()
