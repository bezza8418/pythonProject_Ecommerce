"""Пакет для работы с интернет-магазином."""

from src.category import Category
from src.product import Product
from src.utils import load_categories_from_json, save_categories_to_json

__all__ = [
    "Product",
    "Category",
    "load_categories_from_json",
    "save_categories_to_json",
]
