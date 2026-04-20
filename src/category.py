"""
Модуль для работы с категориями товаров интернет-магазина.
"""

from typing import Iterator, List, Optional

from src.base import BaseEntity
from src.exceptions import ZeroQuantityError
from src.product import Product


class CategoryIterator:
    """Итератор для перебора товаров в категории."""

    def __init__(self, category: "Category") -> None:
        """
        Инициализация итератора.

        Args:
            category: Объект категории, товары которой нужно перебирать
        """
        self._products = category.products_list
        self._index = 0

    def __iter__(self) -> Iterator[Product]:
        """Возвращает итератор."""
        return self

    def __next__(self) -> Product:
        """
        Возвращает следующий товар или бросает StopIteration.
        """
        if self._index >= len(self._products):
            raise StopIteration

        product = self._products[self._index]
        self._index += 1
        return product


class Category(BaseEntity):
    """Класс для представления категории товаров."""

    # Атрибуты класса (общие для всех объектов)
    category_count: int = 0
    product_count: int = 0

    def __init__(
        self, name: str, description: str, products: Optional[List[Product]] = None
    ) -> None:
        """
        Инициализация категории.

        Args:
            name: Название категории
            description: Описание категории
            products: Список товаров в категории (по умолчанию пустой список)
        """
        super().__init__()  # Вызов конструктора BaseEntity
        self.name = name
        self.description = description
        self.__products = products if products is not None else []

        # Увеличиваем счетчик категорий
        Category.category_count += 1

        # Увеличиваем счетчик товаров
        Category.product_count += len(self.__products)

    @property
    def products(self) -> str:
        """
        Геттер для приватного атрибута products.
        Возвращает строку со всеми товарами в формате:
        "Название продукта, X руб. Остаток: X шт.\n"
        """
        if not self.__products:
            return ""

        result = []
        for product in self.__products:
            # Используем __str__ продукта для форматирования
            result.append(str(product))
        return "\n".join(result) + ("\n" if result else "")

    @property
    def products_list(self) -> List[Product]:
        """
        Дополнительный геттер для получения списка объектов Product.
        Нужен для тестирования и внутренних операций.
        """
        return self.__products.copy()

    def add_product(self, product: Product) -> None:
        """
        Добавляет товар в категорию.

        Args:
            product: Объект класса Product или его наследников для добавления

        Raises:
            TypeError: Если передан не объект класса Product или его наследников
            ZeroQuantityError: Если количество товара равно 0
        """
        if not isinstance(product, Product):
            raise TypeError(
                "Можно добавлять только объекты класса Product или его наследников"
            )

        if product.quantity == 0:
            raise ZeroQuantityError(
                "Товар с нулевым количеством не может быть добавлен"
            )

        self.__products.append(product)
        Category.product_count += 1

    def average_price(self) -> float:
        """
        Возвращает средний ценник всех товаров в категории.

        Returns:
            Средняя цена товаров или 0, если товаров нет
        """
        if not self.__products:
            return 0.0

        try:
            total_price = sum(product.price for product in self.__products)
            return total_price / len(self.__products)
        except ZeroDivisionError:
            return 0.0

    def __str__(self) -> str:
        """
        Возвращает строковое представление категории.
        Формат: "Название категории, количество продуктов: X шт."
        Количество продуктов считается как сумма quantity всех товаров в категории.
        """
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def __iter__(self):
        """Возвращает итератор для перебора товаров категории."""
        return CategoryIterator(self)
