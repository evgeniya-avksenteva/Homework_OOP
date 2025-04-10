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

    def __str__(self):
        total = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total} шт."

    def add_product(self, product):
        """Добавляет новый продукт в атрибут products"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    def middle_price(self):
        """Функция вычисляет среднюю цену товаров в категории"""
        try:
            total_sum = sum([i.price for i in self.__products])
            total_quantity = sum([i.quantity for i in self.__products])
            return round(total_sum / total_quantity, 2)
        except ZeroDivisionError:
            print("В категории отсутствуют товары")
            return 0

    @property
    def products(self) -> str:
        product_list = ""
        for product in self.__products:
            product_list += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return product_list
