"""
Модуль для работы с товарами интернет-магазина.
"""

from typing import Union


class Product:
    """Класс для представления товара."""

    def __init__(self, name: str, description: str, price: Union[float, int], quantity: int) -> None:
        """
        Инициализация товара.

        Args:
            name: Название товара
            description: Описание товара
            price: Цена товара (может быть с копейками)
            quantity: Количество товара в наличии
        """
        self.name = name
        self.description = description
        self.price = float(price)  # Приводим к float для единообразия
        self.quantity = quantity
