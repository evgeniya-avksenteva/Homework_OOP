def test_category_init(category) -> None:
    assert category.name == "Смартфоны"
    assert category.description == (
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(category.products) == 2

    assert category.product_count == 2
    assert category.category_count == 1
