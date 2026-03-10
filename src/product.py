"""
Модуль для работы с товарами интернет-магазина.
"""

from typing import Dict, List, Optional, Union


class Product:
    """Класс для представления товара."""

    def __init__(self, name: str, description: str, price: Union[float, int], quantity: int) -> None:
        """
        Инициализация товара.

        Args:
            name: Название товара
            description: Описание товара
            price: Цена товара (может быть с копейками)
            quantity: Количество товара в наличии
        """
        self.name = name
        self.description = description
        self.__price = float(price)  # Приводим к float для единообразия
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Геттер для цены."""
        return self.__price

    @price.setter
    def price(self, value: Union[float, int]) -> None:
        """
        Сеттер для цены с проверкой на положительное значение.

        Args:
            value: Новое значение цены
        """
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = float(value)

    @classmethod
    def new_product(cls, product_data: Dict[str, Union[str, float, int]],
                   existing_products: Optional[List['Product']] = None) -> 'Product':
        """
        Класс-метод для создания нового продукта из словаря.

        Args:
            product_data: Словарь с данными о продукте
            existing_products: Список существующих продуктов для проверки дубликатов

        Returns:
            Новый экземпляр класса Product
        """
        name = product_data.get('name', '')
        description = product_data.get('description', '')
        price = product_data.get('price', 0.0)
        quantity = product_data.get('quantity', 0)

        # Проверка на дубликаты (дополнительное задание)
        if existing_products:
            for existing in existing_products:
                if existing.name == name:
                    # Если товар уже существует, складываем количество
                    # и берем максимальную цену
                    quantity += existing.quantity
                    price = max(float(price), existing.price)
                    # Удаляем старый товар из списка (будет заменен новым)
                    existing_products.remove(existing)
                    break

        return cls(name, description, price, quantity)

    @classmethod
    def new_product_simple(cls, product_data: Dict[str, Union[str, float, int]]) -> 'Product':
        """
        Упрощенная версия класс-метода без проверки дубликатов.
        """
        return cls(
            name=product_data.get('name', ''),
            description=product_data.get('description', ''),
            price=product_data.get('price', 0.0),
            quantity=product_data.get('quantity', 0)
        )

    @price.setter
    def price(self, value: Union[float, int]) -> None:
        """
        Сеттер для цены с проверкой на положительное значение
        и подтверждением при понижении цены.

        Args:
            value: Новое значение цены
        """
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        # Проверка на понижение цены
        if value < self.__price:
            print(f"Вы确实 собираетесь понизить цену с {self.__price} до {value}?")
            answer = input("Подтвердите действие (y/n): ").strip().lower()

            if answer == 'y':
                self.__price = float(value)
                print("Цена успешно изменена")
            else:
                print("Изменение цены отменено")
        else:
            self.__price = float(value)
