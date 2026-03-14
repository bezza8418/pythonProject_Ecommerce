"""
Модуль с абстрактным базовым классом для продуктов.
"""

from abc import ABC, abstractmethod
from typing import Union


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов."""

    @abstractmethod
    def __init__(
        self, name: str, description: str, price: Union[float, int], quantity: int
    ) -> None:
        """Абстрактный метод инициализации продукта."""
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        """Геттер для цены (должен быть реализован в наследниках)."""
        pass

    @price.setter
    @abstractmethod
    def price(self, value: Union[float, int]) -> None:
        """Сеттер для цены (должен быть реализован в наследниках)."""
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Строковое представление продукта."""
        pass

    @abstractmethod
    def __add__(self, other: "BaseProduct") -> float:
        """Сложение продуктов (общая стоимость на складе)."""
        pass
