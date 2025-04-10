import pytest

from src.class_category import Category
from src.class_product import Product

# def test_category_init(category) -> None:
#     assert category.name == "Смартфоны"
#     assert category.description == (
#         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
#     )
#     assert len(category.products) == 2
#
#     assert category.product_count == 2
#     assert category.category_count == 1
#
#
# def test_category(first_category, second_category):
#     assert first_category.name == "Category"
#     assert first_category.description == "Description of the category"
#     assert (
#         first_category.get_product_list
#         == "Product, 84.5 руб. Остаток: 10 шт.\nProduct number two, 155.87 руб. Остаток: 34 шт.\n"
#     )
#
#     assert first_category.category_count == 2
#     assert second_category.category_count == 2
#
#     assert first_category.product_count == 5
#     assert second_category.product_count == 5


def test_category(first_category, second_category):
    assert first_category.name == "Category"
    assert first_category.description == "Description of the category"
    assert (
        first_category.products
        == "Product, 84.5 руб. Остаток: 10 шт.\nProduct number two, 155.87 руб. Остаток: 34 шт.\n"
    )

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 5
    assert second_category.product_count == 5


def test_cat_get_product_list_property(first_category, second_category):
    with pytest.raises(AttributeError):
        print(first_category.__products)
    assert (
        first_category.products
        == "Product, 84.5 руб. Остаток: 10 шт.\nProduct number two, 155.87 руб. Остаток: 34 шт.\n"
    )
    assert (
        second_category.products
        == "Product, 84.5 руб. Остаток: 10 шт.\nProduct number two, 155.87 руб. Остаток: 34 шт."
        "\nProduct three, 8467.56 руб. Остаток: 32 шт.\n"
    )


def test_category_str(first_category, second_category):
    assert str(first_category) == "Category, количество продуктов: 44 шт."
    assert str(second_category) == "Category number two, количество продуктов: 76 шт."


def test_middle_price_with_products():
    product1 = Product("Product A", "красный цвет", 100, quantity=1)
    product2 = Product("Product B", "зеленый цвет", 300, quantity=2)

    category = Category("Смартфоны", "Категория смартфонов", [product1, product2])

    category.add_product(product1)
    category.add_product(product2)

    # Проверяем среднюю цену
    assert category.middle_price() == 133.33


def test_middle_price_no_products(capsys):
    category = Category("Пустая категория", "Категория без продуктов", [])
    # Проверяем среднюю цену при отсутствии продуктов
    result = category.middle_price()
    # Проверяем вывод сообщения и результат
    captured = capsys.readouterr()
    assert result == 0
    assert captured.out.strip() == "В категории отсутствуют товары"
