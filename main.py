"""
Основной модуль для демонстрации работы классов.
"""

from src.category import Category
from src.product import Product, Smartphone, LawnGrass


def main():
    """Демонстрация работы классов."""
    # Создаем обычные товары
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Выводим информацию о товарах
    print("=== ТОВАРЫ (Product) ===")
    print(product1)
    print(product2)
    print(product3)

    # Создаем категорию с товарами
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print("\n=== КАТЕГОРИЯ ===")
    print(category1)

    # Создаем смартфон
    phone = None
    try:
        phone = Smartphone(
            "Samsung Galaxy S23 Ultra",
            "256GB, Серый цвет, 200MP камера",
            180000.0,
            5,
            "Snapdragon 8 Gen 2",
            "SM-S918B",
            256,
            "Серый"
        )
        print("\n=== СМАРТФОН ===")
        print(phone)
        print(f"Производительность: {phone.efficiency}")
        print(f"Модель: {phone.model}")
        print(f"Память: {phone.memory}GB")
        print(f"Цвет: {phone.color}")
    except Exception as e:
        print(f"Ошибка при создании смартфона: {e}")

    # Создаем газонную траву
    grass = None
    try:
        grass = LawnGrass(
            "Газон 'Изумрудный'",
            "Семена газонной травы",
            500.0,
            10,
            "Россия",
            "7-10 дней",
            "Зеленый"
        )
        print("\n=== ГАЗОННАЯ ТРАВА ===")
        print(grass)
        print(f"Страна: {grass.country}")
        print(f"Срок прорастания: {grass.germination_period}")
        print(f"Цвет: {grass.color}")
    except Exception as e:
        print(f"Ошибка при создании газонной травы: {e}")

    # Добавляем новые товары в категорию
    print("\n=== ДОБАВЛЕНИЕ В КАТЕГОРИЮ ===")
    try:
        if phone is not None:
            category1.add_product(phone)
        if grass is not None:
            category1.add_product(grass)
        print("Товары успешно добавлены в категорию")
        print(category1)
    except TypeError as e:
        print(f"Ошибка при добавлении: {e}")

    # Проверяем сложение товаров
    print("\n=== СЛОЖЕНИЕ ТОВАРОВ ===")
    try:
        total = product1 + product2
        print(f"product1 + product2 = {total}")

        # Попытка сложить товары разных классов
        if phone is not None and grass is not None:
            total = phone + grass
            print(f"phone + grass = {total}")
    except TypeError as e:
        print(f"Ошибка при сложении: {e}")

    # Перебираем товары в категории
    print("\n=== ПЕРЕБОР ТОВАРОВ В КАТЕГОРИИ ===")
    for product in category1:
        print(product)

    # Статистика
    print("\n=== СТАТИСТИКА ===")
    print(f"Всего категорий: {Category.category_count}")
    print(f"Всего товаров: {Category.product_count}")


if __name__ == "__main__":
    # Сброс счетчиков для чистоты демонстрации
    Category.category_count = 0
    Category.product_count = 0
    main()
