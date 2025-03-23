from src.class_product import Product


class Category:
    """Создание класса Category"""

    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product):
        """Добавляет новый продукт в атрибут products"""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников.")

        self.__products.append(product)
        Category.product_count += 1
        # self.product_count += 1

    @property
    def products(self) -> str:
        product_list = ""
        for product in self.__products:
            product_list += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return product_list


# if __name__ == '__main__':
#     result = Category("Product", "Description", ["product1", "product2", "product3"])
#     print(result)
