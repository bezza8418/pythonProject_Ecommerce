"""
Тесты для модуля product.
"""

import pytest

from src.product import Product


class TestProduct:
    """Тесты для класса Product."""

    def test_product_initialization(self):
        """Тест инициализации товара."""
        product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

        assert product.name == "Samsung Galaxy S23 Ultra"
        assert product.description == "256GB, Серый цвет, 200MP камера"
        assert product.price == 180000.0
        assert product.quantity == 5

    def test_product_with_int_price(self):
        """Тест инициализации товара с целочисленной ценой."""
        product = Product("Test Product", "Test Description", 1000, 10)

        assert product.price == 1000.0
        assert isinstance(product.price, float)

    def test_product_with_float_price(self):
        """Тест инициализации товара с дробной ценой."""
        product = Product("Test Product", "Test Description", 99.99, 10)

        assert product.price == 99.99
        assert isinstance(product.price, float)

    def test_product_zero_quantity(self):
        """Тест товара с нулевым количеством."""
        product = Product("Test Product", "Test Description", 100.0, 0)

        assert product.quantity == 0

    def test_product_negative_quantity(self):
        """Тест товара с отрицательным количеством."""
        product = Product("Test Product", "Test Description", 100.0, -5)

        assert product.quantity == -5  # В реальном проекте нужна валидация
