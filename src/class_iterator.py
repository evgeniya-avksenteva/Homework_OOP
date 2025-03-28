# from src.class_category import Category
# from src.class_product import Product


class ProductIterator:
    """Класс для итерации товаров одной категории"""

    def __init__(self, iter_obj):
        self.iter_obj = iter_obj
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.iter_obj.products):
            prod_iter = self.iter_obj.products[self.index]
            self.index += 1
            return str(prod_iter)  # Возвращаем строковое представление продукта
        else:
            raise StopIteration


# if __name__ == "__main__":
#     product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#     product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#
#     category1 = Category(
#         "Смартфоны",
#         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
#         [product2, product3],
#     )
#
#     # Итерация по продуктам и вывод их на экран
#     for product in ProductIterator(category1):
#         print(product)  # Печать каждого продукта
