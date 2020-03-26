class Product:
    def __init__(self, product_id, name):
        self.id = product_id
        self.name = name

    def has_same_id(self, product_id):
        return self.id == product_id

    def to_json(self):
        return {'id': self.id, 'name': self.name}
