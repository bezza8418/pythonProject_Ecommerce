"""
Тесты для модуля order.
"""

import pytest

from src.base import BaseEntity
from src.exceptions import ZeroQuantityError
from src.order import Order
from src.product import Product


class TestOrder:
    """Тесты для класса Order."""

    def test_order_creation(self):
        """Тест создания заказа."""
        product = Product("Test Product", "Test Description", 100.0, 10)
        order = Order(product, 3)

        assert order.product == product
        assert order.quantity == 3
        assert order.total_price == 300.0

    def test_order_str(self):
        """Тест строкового представления заказа."""
        product = Product("Test Product", "Test Description", 100.0, 10)
        order = Order(product, 3)

        expected = "Заказ: Test Product x3 = 300.0 руб."
        assert str(order) == expected

    def test_order_repr(self):
        """Тест технического представления заказа."""
        product = Product("Test Product", "Test Description", 100.0, 10)
        order = Order(product, 3)

        assert repr(order) == f"Order({product}, 3)"

    def test_order_invalid_quantity(self):
        """Тест создания заказа с некорректным количеством."""
        product = Product("Test Product", "Test Description", 100.0, 10)

        with pytest.raises(
            ZeroQuantityError, match="Количество товара должно быть положительным"
        ):
            Order(product, 0)

        with pytest.raises(
            ZeroQuantityError, match="Количество товара должно быть положительным"
        ):
            Order(product, -5)


class TestOrderWithDifferentProducts:
    """Тесты заказов с разными типами продуктов."""

    def test_order_with_smartphone(self):
        """Тест заказа со смартфоном."""
        from src.product import Smartphone

        phone = Smartphone(
            "Samsung Galaxy S23 Ultra",
            "256GB, Серый цвет, 200MP камера",
            180000.0,
            5,
            "Snapdragon 8 Gen 2",
            "SM-S918B",
            256,
            "Серый",
        )
        order = Order(phone, 2)

        assert order.total_price == 360000.0
        assert "Samsung Galaxy S23 Ultra" in str(order)

    def test_order_with_lawn_grass(self):
        """Тест заказа с газонной травой."""
        from src.product import LawnGrass

        grass = LawnGrass(
            "Газон 'Изумрудный'",
            "Семена газонной травы",
            500.0,
            10,
            "Россия",
            "7-10 дней",
            "Зеленый",
        )
        order = Order(grass, 7)

        assert order.total_price == 3500.0
        assert "Газон 'Изумрудный'" in str(order)


class TestBaseEntityInheritance:
    """Тесты наследования от BaseEntity."""

    def test_category_inherits_from_base(self):
        """Тест, что Category наследуется от BaseEntity."""
        from src.category import Category

        assert issubclass(Category, BaseEntity)

    def test_order_inherits_from_base(self):
        """Тест, что Order наследуется от BaseEntity."""
        assert issubclass(Order, BaseEntity)

    def test_base_entity_cannot_be_instantiated(self):
        """Тест, что нельзя создать экземпляр абстрактного класса."""
        with pytest.raises(TypeError):
            BaseEntity()
