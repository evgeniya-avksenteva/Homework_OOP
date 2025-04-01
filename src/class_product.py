class Product:
    """Создание класса Product"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) is type(other):
            return self.quantity * self.__price + other.quantity * other.price
        else:
            raise TypeError

    @classmethod
    def new_product(cls, new_product: dict):
        """Возвращает экземпляр класса Product на основе данных словаря"""
        name = new_product.get("name")
        description = new_product.get("description")
        price = new_product.get("price")
        quantity = new_product.get("quantity")
        return cls(name, description, price, quantity)

    @property
    def price(self):
        """Выводит в консоль значение приватного атрибута price"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Устанавливает значение приватного атрибута price"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price
