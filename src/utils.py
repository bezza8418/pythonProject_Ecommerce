"""
Модуль для вспомогательных функций.
"""

import json
from typing import List

from src.category import Category
from src.product import Product


def load_categories_from_json(file_path: str) -> List[Category]:
    """
    Загружает категории и товары из JSON-файла.

    Args:
        file_path: Путь к JSON-файлу

    Returns:
        Список созданных категорий
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    categories = []
    for cat_data in data:
        products = []
        for prod_data in cat_data['products']:
            product = Product(
                name=prod_data['name'],
                description=prod_data['description'],
                price=prod_data['price'],
                quantity=prod_data['quantity']
            )
            products.append(product)

        category = Category(
            name=cat_data['name'],
            description=cat_data['description'],
            products=products
        )
        categories.append(category)

    return categories


def save_categories_to_json(categories: List[Category], file_path: str) -> None:
    """
    Сохраняет категории и товары в JSON-файл.

    Args:
        categories: Список категорий для сохранения
        file_path: Путь к JSON-файлу
    """
    data = []
    for category in categories:
        cat_data = {
            "name": category.name,
            "description": category.description,
            "products": [
                {
                    "name": product.name,
                    "description": product.description,
                    "price": product.price,
                    "quantity": product.quantity
                }
                for product in category.products
            ]
        }
        data.append(cat_data)

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
