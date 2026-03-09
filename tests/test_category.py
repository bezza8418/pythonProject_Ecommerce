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
        Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
        Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
    ]


@pytest.fixture
def sample_category(sample_products):
    """Фикстура с тестовой категорией."""
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        sample_products
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
        assert sample_category.products == sample_products
        assert len(sample_category.products) == 3

    def test_category_with_empty_products(self):
        """Тест категории с пустым списком товаров."""
        category = Category("Пустая категория", "Описание", [])

        assert category.name == "Пустая категория"
        assert category.description == "Описание"
        assert category.products == []
        assert len(category.products) == 0

    def test_category_with_single_product(self, sample_products):
        """Тест категории с одним товаром."""
        single_product = [sample_products[0]]
        category = Category("Один товар", "Описание", single_product)

        assert len(category.products) == 1
        assert category.products[0].name == "Samsung Galaxy S23 Ultra"


class TestCategoryCounters:
    """Тесты для счетчиков категорий и товаров."""

    @staticmethod
    def setup_method():
        """Сброс счетчиков перед каждым тестом."""
        Category.category_count = 0
        Category.product_count = 0

    def test_category_count_increases(self):
        """Тест увеличения счетчика категорий."""
        self.setup_method()
        Category("Категория 1", "Описание 1", [])
        assert Category.category_count == 1

        Category("Категория 2", "Описание 2", [])
        assert Category.category_count == 2

    def test_product_count_increases(self, sample_products):
        """Тест увеличения счетчика товаров."""
        self.setup_method()
        Category("Категория 1", "Описание 1", sample_products[:2])
        assert Category.product_count == 2

        Category("Категория 2", "Описание 2", sample_products[2:])
        assert Category.product_count == 3

    def test_counters_with_multiple_categories(self, sample_products):
        """Тест счетчиков при создании нескольких категорий."""
        self.setup_method()
        Category("Смартфоны", "Описание", sample_products[:2])
        Category("Планшеты", "Описание", sample_products[2:])
        Category("Ноутбуки", "Описание", [])

        assert Category.category_count == 3
        assert Category.product_count == 3  # 2 + 1 + 0

    def test_load_from_json(self, tmp_path):
        """Тест загрузки категорий из JSON-файла."""
        self.setup_method()

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
                        "quantity": 5
                    },
                    {
                        "name": "Test Phone 2",
                        "description": "Test Description 2",
                        "price": 20000.0,
                        "quantity": 3
                    }
                ]
            },
            {
                "name": "Телевизоры",
                "description": "Тестовое описание телевизоров",
                "products": [
                    {
                        "name": "Test TV",
                        "description": "Test TV Description",
                        "price": 50000.0,
                        "quantity": 2
                    }
                ]
            }
        ]

        json_path = tmp_path / "test_products.json"
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(json_data, f)

        # Загружаем категории
        categories = load_categories_from_json(str(json_path))

        # Проверяем результат
        assert len(categories) == 2
        assert categories[0].name == "Смартфоны"
        assert categories[0].description == "Тестовое описание смартфонов"
        assert len(categories[0].products) == 2
        assert categories[0].products[0].name == "Test Phone 1"
        assert categories[0].products[0].price == 10000.0
        assert categories[0].products[1].name == "Test Phone 2"
        assert categories[0].products[1].price == 20000.0

        assert categories[1].name == "Телевизоры"
        assert categories[1].description == "Тестовое описание телевизоров"
        assert len(categories[1].products) == 1
        assert categories[1].products[0].name == "Test TV"
        assert categories[1].products[0].price == 50000.0
        assert categories[1].products[0].quantity == 2

        # Проверяем счетчики
        assert Category.category_count == 2
        assert Category.product_count == 3  # 2 + 1 = 3

    def test_load_from_json_file_not_found(self):
        """Тест загрузки из несуществующего файла."""
        self.setup_method()
        with pytest.raises(FileNotFoundError):
            load_categories_from_json("nonexistent.json")

    def test_load_from_json_invalid_json(self, tmp_path):
        """Тест загрузки из некорректного JSON-файла."""
        self.setup_method()
        json_path = tmp_path / "invalid.json"
        with open(json_path, 'w', encoding='utf-8') as f:
            f.write("{invalid json}")

        with pytest.raises(json.JSONDecodeError):
            load_categories_from_json(str(json_path))
