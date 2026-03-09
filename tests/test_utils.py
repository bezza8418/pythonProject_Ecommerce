"""
Тесты для модуля utils.
"""

import json
import os

import pytest

from src.category import Category
from src.product import Product
from src.utils import load_categories_from_json, save_categories_to_json


@pytest.fixture
def sample_categories():
    """Фикстура с тестовыми категориями для сохранения."""
    products1 = [
        Product("Test Product 1", "Description 1", 100.0, 5),
        Product("Test Product 2", "Description 2", 200.0, 3),
    ]
    products2 = [
        Product("Test Product 3", "Description 3", 300.0, 7),
    ]

    category1 = Category("Категория 1", "Описание категории 1", products1)
    category2 = Category("Категория 2", "Описание категории 2", products2)

    return [category1, category2]


class TestUtils:
    """Тесты для утилит."""

    def test_save_categories_to_json(self, sample_categories, tmp_path):
        """Тест сохранения категорий в JSON-файл."""
        json_path = tmp_path / "saved_categories.json"

        # Сохраняем категории
        save_categories_to_json(sample_categories, str(json_path))

        # Проверяем, что файл создан
        assert os.path.exists(json_path)

        # Загружаем и проверяем содержимое
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        assert len(data) == 2
        assert data[0]["name"] == "Категория 1"
        assert data[0]["description"] == "Описание категории 1"
        assert len(data[0]["products"]) == 2
        assert data[0]["products"][0]["name"] == "Test Product 1"
        assert data[0]["products"][0]["price"] == 100.0
        assert data[0]["products"][1]["name"] == "Test Product 2"

        assert data[1]["name"] == "Категория 2"
        assert len(data[1]["products"]) == 1
        assert data[1]["products"][0]["name"] == "Test Product 3"

    def test_save_and_load_consistency(self, sample_categories, tmp_path):
        """Тест согласованности сохранения и загрузки."""
        json_path = tmp_path / "test_consistency.json"

        # Сохраняем
        save_categories_to_json(sample_categories, str(json_path))

        # Загружаем
        loaded_categories = load_categories_from_json(str(json_path))

        # Проверяем соответствие
        assert len(loaded_categories) == len(sample_categories)
        assert loaded_categories[0].name == sample_categories[0].name
        assert loaded_categories[0].description == sample_categories[0].description
        assert len(loaded_categories[0].products) == len(sample_categories[0].products)
        assert loaded_categories[0].products[0].name == sample_categories[0].products[0].name
        assert loaded_categories[0].products[0].price == sample_categories[0].products[0].price
        assert loaded_categories[0].products[0].quantity == sample_categories[0].products[0].quantity

    def test_save_categories_to_json_empty_list(self, tmp_path):
        """Тест сохранения пустого списка категорий."""
        json_path = tmp_path / "empty.json"

        save_categories_to_json([], str(json_path))

        assert os.path.exists(json_path)
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        assert data == []

    def test_save_categories_to_json_invalid_path(self, sample_categories):
        """Тест сохранения по некорректному пути."""
        with pytest.raises(Exception):
            save_categories_to_json(sample_categories, "/invalid/path/that/doesnt/exist/file.json")

    def test_load_categories_from_json_file_not_found(self):
        """Тест загрузки из несуществующего файла."""
        with pytest.raises(FileNotFoundError):
            load_categories_from_json("nonexistent.json")

    def test_load_categories_from_json_invalid_json(self, tmp_path):
        """Тест загрузки из некорректного JSON-файла."""
        json_path = tmp_path / "invalid.json"
        with open(json_path, 'w', encoding='utf-8') as f:
            f.write("{invalid json}")

        with pytest.raises(json.JSONDecodeError):
            load_categories_from_json(str(json_path))
