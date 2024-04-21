import pytest

from src.category import Category


def test_category(categories_test, product_dict_test):
    category1 = categories_test[0]

    # Проверяем категорию
    assert isinstance(category1, Category)
    assert category1.name == 'test1'
    assert repr(category1) == f"\nname: test1, description: description, products: {repr(category1.products)}"

    # Проверяем общее количество категорий и уникальных продуктов
    assert Category.total_categories() == 1
    assert Category.total_unique_products() == 1

    # Добавляем новую категорию и проверяем общее количество категорий
    category2 = Category('test2', 'description')
    categories_test.append(category2)
    assert Category.total_categories() == 2

    # Добавляем продукты в категорию и проверяем общее количество уникальных продуктов и его наличие в списке продуктов
    new_product = product_dict_test['product4']
    category1.add_product(new_product)
    assert Category.total_unique_products() == 2
    assert any(product.name == new_product['name'] for product in category1.products)

    # Добавляем продукт, который уже существует, и проверяем общее количество уникальных продуктов
    duplicate_product = product_dict_test['product4']
    category1.add_product(duplicate_product)
    assert Category.total_unique_products() == 2

    # Добавляем продукт с новым именем и проверяем общее количество уникальных продуктов
    new_unique_product = product_dict_test['product4']
    category2.add_product(new_unique_product)
    assert Category.total_unique_products() == 3

    #     for product in category.products:
    #         assert isinstance(product, Product)
    #         assert product.name == product_dict_test['product1']['name']
    #         assert product.description == product_dict_test['product1']['description']
    #         assert product.price == product_dict_test['product1']['price']
    #         assert product.quantity == product_dict_test['product1']['quantity']
    #         assert repr(product) == (f"{product_dict_test['product1']['name']}, "
    #                                  f"{product_dict_test['product1']['price']} руб. "
    #                                  f"Остаток: {product_dict_test['product1']['quantity']} шт.")


if __name__ == '__main__':
    pytest.main()
