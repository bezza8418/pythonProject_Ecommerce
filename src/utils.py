"""
Модуль для вспомогательных функций.
"""

import json
from typing import List, Dict, Any

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
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Проверяем, что данные - список
        if not isinstance(data, list):
            return []

        categories = []
        for cat_data in data:
            # Проверяем, что cat_data - словарь
            if not isinstance(cat_data, dict):
                continue

            # Получаем название категории (обязательное поле)
            name = cat_data.get('name', '')
            if not name:
                continue

            # Получаем описание (опционально)
            description = cat_data.get('description', '')

            # Получаем список товаров
            products_data = cat_data.get('products', [])
            if not isinstance(products_data, list):
                products_data = []

            products = []
            for prod_data in products_data:
                # Проверяем, что prod_data - словарь
                if not isinstance(prod_data, dict):
                    continue

                # Получаем данные о товаре с проверками
                prod_name = prod_data.get('name', '')
                if not prod_name:
                    continue

                prod_description = prod_data.get('description', '')

                try:
                    prod_price = float(prod_data.get('price', 0))
                except (TypeError, ValueError):
                    prod_price = 0.0

                try:
                    prod_quantity = int(prod_data.get('quantity', 0))
                except (TypeError, ValueError):
                    prod_quantity = 0

                product = Product(
                    name=prod_name,
                    description=prod_description,
                    price=prod_price,
                    quantity=prod_quantity
                )
                products.append(product)

            category = Category(
                name=name,
                description=description,
                products=products
            )
            categories.append(category)

        return categories

    except (FileNotFoundError, json.JSONDecodeError):
        # Пробрасываем исключения дальше (они обрабатываются в тестах)
        raise


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
                for product in category.products_list  # Используем products_list
            ]
        }
        data.append(cat_data)

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
