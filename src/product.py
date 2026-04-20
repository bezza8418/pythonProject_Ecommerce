"""
Модуль для работы с товарами интернет-магазина.
"""

from typing import Dict, List, Optional, Union

from src.base_product import BaseProduct
from src.mixins import CreationMixin

from src.exceptions import ZeroQuantityError

class Product(CreationMixin, BaseProduct):
    """Базовый класс для представления товара."""

    def __init__(self, name: str, description: str, price: Union[float, int], quantity: int) -> None:
        """
        Инициализация товара.

        Args:
            name: Название товара
            description: Описание товара
            price: Цена товара (может быть с копейками)
            quantity: Количество товара в наличии

        Raises:
            ZeroQuantityError: Если количество товара равно 0
        """
        if quantity == 0:
            raise ZeroQuantityError("Товар с нулевым количеством не может быть добавлен")

        self.name = name
        self.description = description
        self.__price = float(price)
        self.quantity = quantity
        super().__init__(name, description, price, quantity)

    def _get_params(self) -> str:
        """Возвращает параметры для логирования создания."""
        return f"('{self.name}', '{self.description}', {self.__price}, {self.quantity})"

    @property
    def price(self) -> float:
        """Геттер для цены."""
        return self.__price

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
            print(f"Вы действительно хотите понизить цену с {self.__price} до {value}?")
            answer = input("Подтвердите действие (y/n): ").strip().lower()

            if answer == "y":
                self.__price = float(value)
                print("Цена успешно изменена")
            else:
                print("Изменение цены отменено")
        else:
            self.__price = float(value)

    def __str__(self) -> str:
        """
        Возвращает строковое представление товара.
        Формат: "Название продукта, X руб. Остаток: X шт."
        """
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "BaseProduct") -> float:
        """
        Складывает стоимость всех товаров на складе двух продуктов.
        Результат: цена1 * количество1 + цена2 * количество2
        """
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только с объектами класса Product")

        # Проверка на одинаковые классы
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных классов")

        return self.price * self.quantity + other.price * other.quantity

    @classmethod
    def new_product(
        cls,
        product_data: Dict[str, Union[str, float, int]],
        existing_products: Optional[List["Product"]] = None,
    ) -> "Product":
        """
        Класс-метод для создания нового продукта из словаря.

        Args:
            product_data: Словарь с данными о продукте
            existing_products: Список существующих продуктов для проверки дубликатов

        Returns:
            Новый экземпляр класса Product
        """
        name = str(product_data.get("name", ""))
        description = str(product_data.get("description", ""))
        price_value = product_data.get("price", 0)
        quantity_value = product_data.get("quantity", 0)

        price = float(price_value) if price_value else 0.0
        quantity = int(quantity_value) if quantity_value else 0

        if existing_products:
            for existing in existing_products:
                if existing.name == name:
                    quantity += existing.quantity
                    price = max(price, existing.price)
                    existing_products.remove(existing)
                    break

        return cls(name, description, price, quantity)

    @classmethod
    def new_product_simple(
        cls, product_data: Dict[str, Union[str, float, int]]
    ) -> "Product":
        """
        Упрощенная версия класс-метода без проверки дубликатов.
        """
        name = str(product_data.get("name", ""))
        description = str(product_data.get("description", ""))

        price_value = product_data.get("price", 0)
        if isinstance(price_value, str):
            try:
                price = float(price_value)
            except ValueError:
                price = 0.0
        else:
            price = float(price_value)

        quantity_value = product_data.get("quantity", 0)
        if isinstance(quantity_value, str):
            try:
                quantity = int(quantity_value)
            except ValueError:
                quantity = 0
        else:
            quantity = int(quantity_value)

        return cls(name, description, price, quantity)


class Smartphone(Product):
    """Класс для представления смартфона."""

    def __init__(
        self,
        name: str,
        description: str,
        price: Union[float, int],
        quantity: int,
        efficiency: str,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        """
        Инициализация смартфона.
        """
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, price, quantity)

    def _get_params(self) -> str:
        """Возвращает параметры для логирования создания."""
        return (
            f"('{self.name}', '{self.description}', {self.price}, {self.quantity}, "
            f"'{self.efficiency}', '{self.model}', {self.memory}, '{self.color}')"
        )


class LawnGrass(Product):
    """Класс для представления газонной травы."""

    def __init__(
        self,
        name: str,
        description: str,
        price: Union[float, int],
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        """
        Инициализация газонной травы.
        """
        self.country = country
        self.germination_period = germination_period
        self.color = color
        super().__init__(name, description, price, quantity)

    def _get_params(self) -> str:
        """Возвращает параметры для логирования создания."""
        return (
            f"('{self.name}', '{self.description}', {self.price}, {self.quantity}, "
            f"'{self.country}', '{self.germination_period}', '{self.color}')"
        )
