"""
Основной модуль для демонстрации работы классов Product и Category.
"""

import os
from src.category import Category
from src.product import Product


def main():
    """Демонстрация работы классов."""
    # Способ 1: Создание объектов вручную
    print("=== СОЗДАНИЕ ВРУЧНУЮ ===")
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(f"Создана категория: {category1.name} с {len(category1.products)} товарами")
    print(f"  - {product1.name}: {product1.price} руб., {product1.quantity} шт.")
    print(f"  - {product2.name}: {product2.price} руб., {product2.quantity} шт.")
    print(f"  - {product3.name}: {product3.price} руб., {product3.quantity} шт.")

    # Способ 2: Загрузка из JSON (дополнительное задание)
    print("\n=== ЗАГРУЗКА ИЗ JSON ===")
    json_path = os.path.join(os.path.dirname(__file__), "data", "products.json")

    try:
        categories = Category.load_from_json(json_path)

        print(f"Загружено категорий: {len(categories)}")
        for i, category in enumerate(categories, 1):
            print(f"\n{i}. {category.name}")
            print(f"   Описание: {category.description[:60]}...")
            print(f"   Товаров: {len(category.products)}")

            # Выводим все товары в категории
            for product in category.products:
                print(f"     - {product.name}: {product.price} руб., {product.quantity} шт.")

    except FileNotFoundError:
        print(f"Файл {json_path} не найден. Создайте его для загрузки данных.")
    except Exception as e:
        print(f"Ошибка при загрузке JSON: {e}")

    # Общая статистика
    print("\n=== ОБЩАЯ СТАТИСТИКА ===")
    print(f"Всего категорий: {Category.category_count}")
    print(f"Всего товаров: {Category.product_count}")


if __name__ == "__main__":
    # Сброс счетчиков для чистоты демонстрации
    Category.category_count = 0
    Category.product_count = 0
    main()
