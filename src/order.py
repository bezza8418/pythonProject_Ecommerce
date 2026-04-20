"""
Модуль для работы с заказами.
"""

from src.base import BaseEntity
from src.exceptions import ZeroQuantityError
from src.product import Product


class Order(BaseEntity):
    """
    Класс для представления заказа.
    Заказ содержит один товар, его количество и итоговую стоимость.
    """

    def __init__(self, product: Product, quantity: int) -> None:
        """
        Инициализация заказа.

        Args:
            product: Товар, который заказывают
            quantity: Количество товара

        Raises:
            ValueError: Если количество меньше или равно 0
            ZeroQuantityError: Если количество равно 0
        """
        super().__init__()

        if quantity <= 0:
            raise ZeroQuantityError("Количество товара должно быть положительным")

        self.product = product
        self.quantity = quantity
        self.total_price = product.price * quantity

    def __str__(self) -> str:
        """
        Строковое представление заказа.
        Формат: "Заказ: {название товара} x{количество} = {итоговая цена} руб."
        """
        return f"Заказ: {self.product.name} x{self.quantity} = {self.total_price} руб."

    def __repr__(self) -> str:
        """Техническое представление заказа."""
        return f"Order({self.product}, {self.quantity})"
