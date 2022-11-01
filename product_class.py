from abc import ABC, abstractmethod

class Product():
    name = ''
    type = ''
    cost = 0
    quantities = 0

class ProductAbstract(ABC):
    @abstractmethod
    def create_product(self, product: Product):
        pass

    @abstractmethod
    def edit_product(self):
        pass

    @abstractmethod
    def get_product_id(self, product_id):
        pass

    @abstractmethod
    def get_all_products(self):
        pass

    @abstractmethod
    def upload_product_image(self):
        pass

    @abstractmethod
    def delete_product(self, product: Product):
        pass

class ProductManager(ProductAbstract):
    def create_product(self, product: Product):
        print("A product has been added")

    def edit_product(self):
        print("A product parameter has been changed")

    def get_product_id(self, product_id):
        print(f"The product ID is {product_id}")

    def get_all_products(self):
        print("This is the collection of all products")

    def upload_product_image(self):
        print("Product image has been uploaded")

    def delete_product(self, product: Product):
        print("The product has been deleted")

first_product = Product()
first_product.name = "Coca-Cola"
first_product.cost = 30
first_product.quantities = 20

product_manager = ProductManager()
product_manager.create_product(first_product)
product_manager.edit_product()
product_manager.get_product_id(322)
product_manager.get_all_products()
product_manager.upload_product_image()
product_manager.delete_product(first_product)





