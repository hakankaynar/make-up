import unittest
import random

from routes import application


class ProductApiIntegrationTest(unittest.TestCase):

    def setUp(self):
        application.config['TESTING'] = True
        application.config['WTF_CSRF_ENABLED'] = False
        application.config['DEBUG'] = False
        self.app = application.test_client()
        self.product_id = random.randint(1, 100)

    def tearDown(self):
        self.app.delete('/api/v1.0/product/' + str(self.product_id), follow_redirects=True)

    def test_empty_get(self):
        response = self.app.get('/api/v1.0/product/' + str(self.product_id), follow_redirects=True)
        self.assertEqual(response.status_code, 404)

    def test_delete(self):
        response = self.app.post('/api/v1.0/product', data='{ "id":' + str(self.product_id) + ', "name": "asd" }',
                                 follow_redirects=True, content_type='application/json')
        self.assertEqual(response.status_code, 200, "Product add should work")

        response = self.app.delete('/api/v1.0/product/' + str(self.product_id), follow_redirects=True)
        self.assertEqual(response.status_code, 200, "Product delete should work")

    def test_get(self):
        response = self.app.post('/api/v1.0/product', data='{ "id":' + str(self.product_id) + ', "name": "asd" }',
                                 follow_redirects=True, content_type='application/json')

        self.assertEqual(response.status_code, 200, "Product add should work")

        response = self.app.get('/api/v1.0/product/' + str(self.product_id), follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
