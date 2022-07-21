from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name):
        for product in self.products:
            if product.__name == product_name:
                return product

    def remove(self, product_name):
        for product in self.products:
            if product.__name == product_name:
                self.products.remove(product)

    def __repr__(self):
        result = ""
        for product in self.products:
            result += f"\n{product.__name}: {product.quantity}"

        return result.strip()
