"""
Тесты для пользовательских исключений.
"""

import pytest

from src.exceptions import ZeroQuantityError
from src.order import Order
from src.product import Product


class TestZeroQuantityError:
    """Тесты для пользовательского исключения ZeroQuantityError."""

    def test_zero_quantity_error_raised_in_product(self):
        """Тест, что ZeroQuantityError выбрасывается при создании товара с quantity=0."""
        with pytest.raises(
            ZeroQuantityError,
            match="Товар с нулевым количеством не может быть добавлен",
        ):
            Product("Test", "Desc", 100.0, 0)

    def test_zero_quantity_error_raised_in_order(self):
        """Тест, что ZeroQuantityError выбрасывается при создании заказа с quantity=0."""
        product = Product("Test", "Desc", 100.0, 5)

        with pytest.raises(
            ZeroQuantityError, match="Количество товара должно быть положительным"
        ):
            Order(product, 0)
