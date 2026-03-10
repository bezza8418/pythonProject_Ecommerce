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

        assert product.quantity == -5


class TestProductPrice:
    """Тесты для работы с ценой (геттеры/сеттеры)."""

    def test_price_getter(self):
        """Тест геттера цены."""
        product = Product("Test", "Desc", 100.0, 5)
        assert product.price == 100.0

    def test_price_setter_positive(self):
        """Тест сеттера с положительным значением."""
        product = Product("Test", "Desc", 100.0, 5)
        product.price = 150.0
        assert product.price == 150.0

    def test_price_setter_zero(self, capsys):
        """Тест сеттера с нулевым значением."""
        product = Product("Test", "Desc", 100.0, 5)
        product.price = 0
        captured = capsys.readouterr()
        assert product.price == 100.0  # Цена не изменилась
        assert "Цена не должна быть нулевая или отрицательная" in captured.out

    def test_price_setter_negative(self, capsys):
        """Тест сеттера с отрицательным значением."""
        product = Product("Test", "Desc", 100.0, 5)
        product.price = -50.0
        captured = capsys.readouterr()
        assert product.price == 100.0  # Цена не изменилась
        assert "Цена не должна быть нулевая или отрицательная" in captured.out


class TestProductNewProduct:
    """Тесты для класс-метода new_product."""

    def test_new_product_simple(self):
        """Тест создания продукта из словаря."""
        data = {
            'name': 'Test Product',
            'description': 'Test Description',
            'price': 99.99,
            'quantity': 10
        }

        product = Product.new_product_simple(data)

        assert product.name == 'Test Product'
        assert product.description == 'Test Description'
        assert product.price == 99.99
        assert product.quantity == 10

    def test_new_product_with_duplicate_check_no_duplicates(self):
        """Тест создания продукта без дубликатов."""
        data = {
            'name': 'New Product',
            'description': 'New Description',
            'price': 50.0,
            'quantity': 5
        }

        existing = [
            Product("Existing 1", "Desc 1", 100.0, 2),
            Product("Existing 2", "Desc 2", 200.0, 3)
        ]

        product = Product.new_product(data, existing)

        assert product.name == 'New Product'
        assert product.quantity == 5
        assert len(existing) == 2  # Список не изменился

    def test_new_product_with_duplicate(self):
        """Тест создания продукта с дубликатом."""
        data = {
            'name': 'Duplicate Product',
            'description': 'New Description',
            'price': 50.0,
            'quantity': 5
        }

        existing = [
            Product("Duplicate Product", "Old Desc", 30.0, 2),
            Product("Other Product", "Desc", 100.0, 3)
        ]

        product = Product.new_product(data, existing)

        assert product.name == 'Duplicate Product'
        assert product.quantity == 7  # 5 + 2
        assert product.price == 50.0  # Взяли максимальную цену
        assert len(existing) == 1  # Дубликат удален, остался только Other Product

    def test_new_product_with_duplicate_max_price(self):
        """Тест выбора максимальной цены при дубликате."""
        data = {
            'name': 'Duplicate Product',
            'description': 'New Description',
            'price': 30.0,  # Меньше чем у существующего
            'quantity': 5
        }

        existing = [
            Product("Duplicate Product", "Old Desc", 50.0, 2),
        ]

        product = Product.new_product(data, existing)

        assert product.price == 50.0  # Взяли максимальную цену
        assert product.quantity == 7
