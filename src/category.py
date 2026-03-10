"""
Модуль для работы с категориями товаров интернет-магазина.
"""

from typing import List, Optional

from src.product import Product


class Category:
    """Класс для представления категории товаров."""

    # Атрибуты класса (общие для всех объектов)
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None) -> None:
        """
        Инициализация категории.

        Args:
            name: Название категории
            description: Описание категории
            products: Список товаров в категории (по умолчанию пустой список)
        """
        self.name = name
        self.description = description
        self.__products = products if products is not None else []

        # Увеличиваем счетчик категорий
        Category.category_count += 1

        # Увеличиваем счетчик товаров
        Category.product_count += len(self.__products)

    @property
    def products(self) -> str:
        """
        Геттер для приватного атрибута products.
        Возвращает строку со всеми товарами в формате:
        "Название продукта, X руб. Остаток: X шт.\n"
        """
        if not self.__products:
            return ""

        result = []
        for product in self.__products:
            result.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return "\n".join(result) + ("\n" if result else "")

    def add_product(self, product: Product) -> None:
        """
        Добавляет товар в категорию.

        Args:
            product: Объект класса Product для добавления
        """
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products_list(self) -> List[Product]:
        """
        Дополнительный геттер для получения списка объектов Product.
        Нужен для тестирования и внутренних операций.
        """
        return self.__products.copy()
