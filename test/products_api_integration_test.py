import unittest

from routes import application


class ProductsApiTest(unittest.TestCase):

    def setUp(self):
        application.config['TESTING'] = True
        application.config['WTF_CSRF_ENABLED'] = False
        application.config['DEBUG'] = False
        self.application = application.test_client()

    def test_get_products_without_products(self):
        response = self.application.get('/api/v1.0/products', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
