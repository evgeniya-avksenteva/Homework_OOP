import pytest

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
