"""
Модуль для работы с категориями товаров интернет-магазина.
"""

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
