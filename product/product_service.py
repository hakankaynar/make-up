from .product_data import ProductData


class ProductService:
    __productData = ProductData()

    def list(self):
        return self.__productData.list_all()

    def get(self, product_id):
        return self.__productData.get(product_id)

    def add(self, product):
        self.__productData.insert(product)

    def delete(self, product_id):
        return self.__productData.delete(product_id)
