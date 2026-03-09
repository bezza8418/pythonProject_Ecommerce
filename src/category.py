"""
Модуль для работы с категориями товаров интернет-магазина.
"""

import json
from typing import List

from src.product import Product


class Category:
    """Класс для представления категории товаров."""

    # Атрибуты класса (общие для всех объектов)
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: List[Product]) -> None:
        """
        Инициализация категории.

        Args:
            name: Название категории
            description: Описание категории
            products: Список товаров в категории
        """
        self.name = name
        self.description = description
        self.products = products

        # Увеличиваем счетчик категорий
        Category.category_count += 1

        # Увеличиваем счетчик товаров
        Category.product_count += len(products)

    @classmethod
    def load_from_json(cls, file_path: str) -> List['Category']:
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

            category = cls(
                name=cat_data['name'],
                description=cat_data['description'],
                products=products
            )
            categories.append(category)

        return categories
