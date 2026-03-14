"""
Тесты для модуля product.
"""

import pytest

from src.base_product import BaseProduct
from src.product import LawnGrass, Product, Smartphone


class TestProduct:
    """Тесты для класса Product."""

    def test_product_initialization(self):
        """Тест инициализации товара."""
        product = Product(
            "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
        )

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


class TestProductMagicMethods:
    """Тесты для магических методов класса Product."""

    def test_product_str(self):
        """Тест строкового представления товара."""
        product = Product(
            "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
        )
        expected = "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
        assert str(product) == expected

    def test_product_add(self):
        """Тест сложения двух товаров."""
        product1 = Product("Product 1", "Desc 1", 100.0, 10)
        product2 = Product("Product 2", "Desc 2", 200.0, 2)

        result = product1 + product2
        expected = 100 * 10 + 200 * 2  # 1000 + 400 = 1400

        assert result == expected

    def test_product_add_with_non_product(self):
        """Тест сложения товара с не-товаром."""
        product = Product("Product", "Desc", 100.0, 5)

        with pytest.raises(
            TypeError, match="Можно складывать только с объектами класса Product"
        ):
            product + 100  # noqa

    def test_product_add_with_self(self):
        """Тест сложения товара с самим собой."""
        product = Product("Product", "Desc", 100.0, 5)

        result = product + product
        expected = 100 * 5 + 100 * 5  # 500 + 500 = 1000

        assert result == expected


class TestSmartphone:
    """Тесты для класса Smartphone."""

    def test_smartphone_creation(self):
        """Тест создания смартфона."""
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

        assert phone.name == "Samsung Galaxy S23 Ultra"
        assert phone.price == 180000.0
        assert phone.quantity == 5
        assert phone.efficiency == "Snapdragon 8 Gen 2"
        assert phone.model == "SM-S918B"
        assert phone.memory == 256
        assert phone.color == "Серый"

    def test_smartphone_str(self):
        """Тест строкового представления смартфона."""
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
        expected = "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
        assert str(phone) == expected


class TestLawnGrass:
    """Тесты для класса LawnGrass."""

    def test_lawn_grass_creation(self):
        """Тест создания газонной травы."""
        grass = LawnGrass(
            "Газон 'Изумрудный'",
            "Семена газонной травы",
            500.0,
            10,
            "Россия",
            "7-10 дней",
            "Зеленый",
        )

        assert grass.name == "Газон 'Изумрудный'"
        assert grass.price == 500.0
        assert grass.quantity == 10
        assert grass.country == "Россия"
        assert grass.germination_period == "7-10 дней"
        assert grass.color == "Зеленый"

    def test_lawn_grass_str(self):
        """Тест строкового представления газонной травы."""
        grass = LawnGrass(
            "Газон 'Изумрудный'",
            "Семена газонной травы",
            500.0,
            10,
            "Россия",
            "7-10 дней",
            "Зеленый",
        )
        expected = "Газон 'Изумрудный', 500.0 руб. Остаток: 10 шт."
        assert str(grass) == expected


class TestProductAdditionRestrictions:
    """Тесты для ограничений сложения."""

    def test_add_same_classes(self):
        """Тест сложения объектов одного класса."""
        phone1 = Smartphone(
            "Samsung Galaxy S23 Ultra",
            "256GB",
            180000.0,
            5,
            "Snapdragon",
            "SM-S918B",
            256,
            "Серый",
        )
        phone2 = Smartphone(
            "Iphone 15", "512GB", 210000.0, 8, "A16", "A3090", 512, "Black"
        )

        result = phone1 + phone2
        expected = 180000 * 5 + 210000 * 8  # 900000 + 1680000 = 2580000
        assert result == expected

    def test_add_different_classes(self):
        """Тест сложения объектов разных классов."""
        phone = Smartphone(
            "Samsung Galaxy S23 Ultra",
            "256GB",
            180000.0,
            5,
            "Snapdragon",
            "SM-S918B",
            256,
            "Серый",
        )
        grass = LawnGrass(
            "Газон 'Изумрудный'", "Семена", 500.0, 10, "Россия", "7-10 дней", "Зеленый"
        )

        with pytest.raises(TypeError, match="Нельзя складывать товары разных классов"):
            phone + grass  # noqa


class TestProductNewProduct:
    """Тесты для класс-метода new_product."""

    def test_new_product_simple(self):
        """Тест создания продукта из словаря."""
        data = {
            "name": "Test Product",
            "description": "Test Description",
            "price": 99.99,
            "quantity": 10,
        }

        product = Product.new_product_simple(data)

        assert product.name == "Test Product"
        assert product.description == "Test Description"
        assert product.price == 99.99
        assert product.quantity == 10

    def test_new_product_with_duplicate_check_no_duplicates(self):
        """Тест создания продукта без дубликатов."""
        data = {
            "name": "New Product",
            "description": "New Description",
            "price": 50.0,
            "quantity": 5,
        }

        existing = [
            Product("Existing 1", "Desc 1", 100.0, 2),
            Product("Existing 2", "Desc 2", 200.0, 3),
        ]

        product = Product.new_product(data, existing)

        assert product.name == "New Product"
        assert product.quantity == 5
        assert len(existing) == 2  # Список не изменился

    def test_new_product_with_duplicate(self):
        """Тест создания продукта с дубликатом."""
        data = {
            "name": "Duplicate Product",
            "description": "New Description",
            "price": 50.0,
            "quantity": 5,
        }

        existing = [
            Product("Duplicate Product", "Old Desc", 30.0, 2),
            Product("Other Product", "Desc", 100.0, 3),
        ]

        product = Product.new_product(data, existing)

        assert product.name == "Duplicate Product"
        assert product.quantity == 7  # 5 + 2
        assert product.price == 50.0  # Взяли максимальную цену
        assert len(existing) == 1  # Дубликат удален, остался только Other Product

    def test_new_product_with_duplicate_max_price(self):
        """Тест выбора максимальной цены при дубликате."""
        data = {
            "name": "Duplicate Product",
            "description": "New Description",
            "price": 30.0,  # Меньше чем у существующего
            "quantity": 5,
        }

        existing = [
            Product("Duplicate Product", "Old Desc", 50.0, 2),
        ]

        product = Product.new_product(data, existing)

        assert product.price == 50.0  # Взяли максимальную цену
        assert product.quantity == 7


class TestProductPriceConfirmation:
    """Тесты для подтверждения понижения цены."""

    def test_price_decrease_confirmed(self, monkeypatch, capsys):
        """Тест понижения цены с подтверждением."""
        product = Product("Test", "Desc", 100.0, 5)

        # Имитируем ввод 'y'
        monkeypatch.setattr("builtins.input", lambda _: "y")

        product.price = 80.0
        captured = capsys.readouterr()

        assert product.price == 80.0
        assert "понизить цену" in captured.out
        assert "Цена успешно изменена" in captured.out

    def test_price_decrease_cancelled(self, monkeypatch, capsys):
        """Тест понижения цены с отменой."""
        product = Product("Test", "Desc", 100.0, 5)

        # Имитируем ввод 'n'
        monkeypatch.setattr("builtins.input", lambda _: "n")

        product.price = 80.0
        captured = capsys.readouterr()

        assert product.price == 100.0  # Цена не изменилась
        assert "понизить цену" in captured.out
        assert "Изменение цены отменено" in captured.out

    def test_price_increase_no_confirmation(self, capsys):
        """Тест повышения цены (без подтверждения)."""
        product = Product("Test", "Desc", 100.0, 5)

        product.price = 120.0
        captured = capsys.readouterr()

        assert product.price == 120.0
        assert "понизить цену" not in captured.out


class TestProductEdgeCases:
    """Тесты для граничных случаев."""

    def test_new_product_with_string_price(self):
        """Тест создания продукта с ценой в виде строки."""
        data = {
            "name": "Test Product",
            "description": "Test Description",
            "price": "99.99",
            "quantity": "10",
        }

        product = Product.new_product_simple(data)

        assert product.price == 99.99
        assert product.quantity == 10

    def test_new_product_with_invalid_string_price(self):
        """Тест создания продукта с некорректной строкой цены."""
        data = {
            "name": "Test Product",
            "description": "Test Description",
            "price": "invalid",
            "quantity": "invalid",
        }

        product = Product.new_product_simple(data)

        assert product.price == 0.0  # Должно стать 0
        assert product.quantity == 0  # Должно стать 0

    def test_new_product_with_dict_contains_all_types(self):
        """Тест new_product со сложным словарем."""
        product1 = Product("Product 1", "Desc 1", 100.0, 2)
        product2 = Product("Product 2", "Desc 2", 200.0, 3)

        data = {
            "name": "Duplicate Product",
            "description": "New Description",
            "price": 50.0,
            "quantity": 5,
        }

        existing = [product1, product2]

        product = Product.new_product(data, existing)

        assert product.name == "Duplicate Product"
        assert product.price == 50.0
        assert product.quantity == 5


class TestProductCreationMixin:
    """Тесты для миксина создания продуктов."""

    def test_product_creation_logging(self, capsys):
        """Тест логирования при создании продукта."""
        Product("Test Product", "Test Description", 100.0, 5)
        captured = capsys.readouterr()

        assert "Создан объект: Product" in captured.out
        assert "Test Product" in captured.out
        assert "100.0" in captured.out
        assert "5" in captured.out

    def test_smartphone_creation_logging(self, capsys):
        """Тест логирования при создании смартфона."""
        Smartphone(
            "Samsung Galaxy S23 Ultra",
            "256GB, Серый цвет, 200MP камера",
            180000.0,
            5,
            "Snapdragon 8 Gen 2",
            "SM-S918B",
            256,
            "Серый",
        )
        captured = capsys.readouterr()

        assert "Создан объект: Smartphone" in captured.out
        assert "Samsung Galaxy S23 Ultra" in captured.out
        assert "Snapdragon" in captured.out

    def test_lawn_grass_creation_logging(self, capsys):
        """Тест логирования при создании газонной травы."""
        LawnGrass(
            "Газон 'Изумрудный'",
            "Семена газонной травы",
            500.0,
            10,
            "Россия",
            "7-10 дней",
            "Зеленый",
        )
        captured = capsys.readouterr()

        assert "Создан объект: LawnGrass" in captured.out
        assert "Газон 'Изумрудный'" in captured.out
        assert "Россия" in captured.out


class TestBaseProduct:
    """Тесты для абстрактного базового класса."""

    def test_product_inherits_from_base(self):
        """Тест, что Product наследуется от BaseProduct."""
        assert issubclass(Product, BaseProduct)

    def test_smartphone_inherits_from_base(self):
        """Тест, что Smartphone наследуется от BaseProduct через Product."""
        assert issubclass(Smartphone, BaseProduct)

    def test_base_product_cannot_be_instantiated(self):
        """Тест, что нельзя создать экземпляр абстрактного класса."""
        with pytest.raises(TypeError):
            BaseProduct("Test", "Desc", 100.0, 5)
