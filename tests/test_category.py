"""
Тесты для модуля category.
"""

import json

import pytest

from src.category import Category
from src.product import Product
from src.utils import load_categories_from_json


@pytest.fixture
def sample_products():
    """Фикстура с тестовыми товарами."""
    return [
        Product(
            "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
        ),
        Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
    ]


@pytest.fixture
def sample_category(sample_products):
    """Фикстура с тестовой категорией."""
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        sample_products,
    )


class TestCategory:
    """Тесты для класса Category."""

    def test_category_initialization(self, sample_category, sample_products):
        """Тест инициализации категории."""
        assert sample_category.name == "Смартфоны"
        assert sample_category.description == (
            "Смартфоны, как средство не только коммуникации, "
            "но и получения дополнительных функций для удобства жизни"
        )
        # Проверяем через products_list, что товары сохранились
        assert len(sample_category.products_list) == 3
        assert sample_category.products_list == sample_products

    def test_category_with_empty_products(self):
        """Тест категории с пустым списком товаров."""
        category = Category("Пустая категория", "Описание")

        assert category.name == "Пустая категория"
        assert category.description == "Описание"
        assert len(category.products_list) == 0
        assert category.products == ""  # Пустая строка для геттера

    def test_category_with_single_product(self, sample_products):
        """Тест категории с одним товаром."""
        single_product = [sample_products[0]]
        category = Category("Один товар", "Описание", single_product)

        assert len(category.products_list) == 1
        assert category.products_list[0].name == "Samsung Galaxy S23 Ultra"


class TestCategoryPrivate:
    """Тесты для приватных атрибутов."""

    def test_products_private(self, sample_category):
        """Тест, что атрибут products действительно приватный."""
        with pytest.raises(AttributeError):
            sample_category.__products

    def test_products_getter_format(self, sample_category):
        """Тест формата геттера products."""
        result = sample_category.products
        expected = (
            "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
            "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
            "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
        )
        assert result == expected

    def test_products_getter_empty(self):
        """Тест геттера для пустой категории."""
        category = Category("Пустая", "Описание")
        assert category.products == ""


class TestCategoryAddProduct:
    """Тесты для метода add_product."""

    def test_add_product_increases_product_count(self, sample_products):
        """Тест, что добавление товара увеличивает счетчик продуктов."""
        # Сохраняем текущее значение счетчика
        initial_count = Category.product_count

        category = Category("Тестовая категория", "Описание")
        category.add_product(sample_products[0])

        assert Category.product_count == initial_count + 1
        assert len(category.products_list) == 1
        assert category.products_list[0].name == "Samsung Galaxy S23 Ultra"

    def test_add_product_to_existing_category(self, sample_category, sample_products):
        """Тест добавления товара в существующую категорию."""
        initial_count = Category.product_count
        initial_category_len = len(sample_category.products_list)

        sample_category.add_product(sample_products[0])

        assert Category.product_count == initial_count + 1
        assert len(sample_category.products_list) == initial_category_len + 1
        assert sample_category.products_list[-1].name == "Samsung Galaxy S23 Ultra"

    def test_add_product_updates_products_string(
        self, sample_category, sample_products
    ):
        """Тест, что геттер обновляется после добавления товара."""
        initial_products_str = sample_category.products
        sample_category.add_product(sample_products[0])
        new_products_str = sample_category.products

        assert len(new_products_str) > len(initial_products_str)
        assert "Samsung Galaxy S23 Ultra" in new_products_str


class TestCategoryCounters:
    """Тесты для счетчиков категорий и товаров."""

    def setup_method(self):
        """Сброс счетчиков перед каждым тестом."""
        Category.category_count = 0
        Category.product_count = 0

    def test_category_count_increases(self):
        """Тест увеличения счетчика категорий."""
        Category("Категория 1", "Описание 1")
        assert Category.category_count == 1

        Category("Категория 2", "Описание 2")
        assert Category.category_count == 2

    def test_product_count_increases_with_initial_products(self, sample_products):
        """Тест увеличения счетчика товаров при создании категории."""
        Category("Категория 1", "Описание 1", sample_products[:2])
        assert Category.product_count == 2

        Category("Категория 2", "Описание 2", sample_products[2:])
        assert Category.product_count == 3

    def test_product_count_increases_with_add_product(self, sample_products):
        """Тест увеличения счетчика товаров при добавлении."""
        category = Category("Категория", "Описание")
        assert Category.product_count == 0

        category.add_product(sample_products[0])
        assert Category.product_count == 1

        category.add_product(sample_products[1])
        assert Category.product_count == 2

    def test_counters_with_multiple_categories(self, sample_products):
        """Тест счетчиков при создании нескольких категорий."""
        Category.category_count = 0
        Category.product_count = 0

        Category("Смартфоны", "Описание", sample_products[:2])
        Category("Планшеты", "Описание", sample_products[2:])
        Category("Ноутбуки", "Описание", [])

        assert Category.category_count == 3
        assert Category.product_count == 3  # 2 + 1 + 0


class TestCategoryUtils:
    """Тесты для утилит работы с категориями."""

    def test_load_from_json(self, tmp_path):
        """Тест загрузки категорий из JSON-файла."""
        # Сброс счетчиков
        Category.category_count = 0
        Category.product_count = 0

        # Создаем временный JSON-файл
        json_data = [
            {
                "name": "Смартфоны",
                "description": "Тестовое описание смартфонов",
                "products": [
                    {
                        "name": "Test Phone 1",
                        "description": "Test Description 1",
                        "price": 10000.0,
                        "quantity": 5,
                    },
                    {
                        "name": "Test Phone 2",
                        "description": "Test Description 2",
                        "price": 20000.0,
                        "quantity": 3,
                    },
                ],
            },
            {
                "name": "Телевизоры",
                "description": "Тестовое описание телевизоров",
                "products": [
                    {
                        "name": "Test TV",
                        "description": "Test TV Description",
                        "price": 50000.0,
                        "quantity": 2,
                    }
                ],
            },
        ]

        json_path = tmp_path / "test_products.json"
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(json_data, f)

        # Загружаем категории
        categories = load_categories_from_json(str(json_path))

        # Проверяем результат
        assert len(categories) == 2
        assert categories[0].name == "Смартфоны"
        assert len(categories[0].products_list) == 2
        assert categories[0].products_list[0].name == "Test Phone 1"

        assert categories[1].name == "Телевизоры"
        assert len(categories[1].products_list) == 1
        assert categories[1].products_list[0].name == "Test TV"

        # Проверяем счетчики
        assert Category.category_count == 2
        assert Category.product_count == 3

    def test_load_from_json_file_not_found(self):
        """Тест загрузки из несуществующего файла."""
        with pytest.raises(FileNotFoundError):
            load_categories_from_json("nonexistent.json")

    def test_load_from_json_invalid_json(self, tmp_path):
        """Тест загрузки из некорректного JSON-файла."""
        json_path = tmp_path / "invalid.json"
        with open(json_path, "w", encoding="utf-8") as f:
            f.write("{invalid json")

        with pytest.raises(json.JSONDecodeError):
            load_categories_from_json(str(json_path))


class TestCategoryMagicMethods:
    """Тесты для магических методов класса Category."""

    def test_category_str(self, sample_category, sample_products):
        """Тест строкового представления категории."""
        # sample_products: [Samsung(5), Iphone(8), Xiaomi(14)]
        expected = "Смартфоны, количество продуктов: 27 шт."  # 5 + 8 + 14 = 27
        assert str(sample_category) == expected

    def test_category_str_empty(self):
        """Тест строкового представления пустой категории."""
        category = Category("Пустая категория", "Описание", [])
        expected = "Пустая категория, количество продуктов: 0 шт."
        assert str(category) == expected

    def test_category_str_after_add_product(self, sample_category, sample_products):
        """Тест строкового представления после добавления товара."""
        initial_str = str(sample_category)
        sample_category.add_product(sample_products[0])
        new_str = str(sample_category)

        assert initial_str != new_str
        assert "27 шт." in initial_str  # Было 27
        assert "32 шт." in new_str      # Стало 27 + 5 = 32


class TestCategoryIterator:
    """Тесты для итератора категории."""

    def test_category_iteration(self, sample_category, sample_products):
        """Тест перебора товаров в категории."""
        products_list = []
        for product in sample_category:
            products_list.append(product)

        assert len(products_list) == 3
        assert products_list[0].name == "Samsung Galaxy S23 Ultra"
        assert products_list[1].name == "Iphone 15"
        assert products_list[2].name == "Xiaomi Redmi Note 11"

    def test_category_iteration_empty(self):
        """Тест перебора в пустой категории."""
        category = Category("Пустая", "Описание", [])
        products_list = [p for p in category]

        assert products_list == []

    def test_category_iteration_after_add(self, sample_category, sample_products):
        """Тест перебора после добавления товара."""
        initial_count = len([p for p in sample_category])

        sample_category.add_product(sample_products[0])
        new_count = len([p for p in sample_category])

        assert new_count == initial_count + 1
