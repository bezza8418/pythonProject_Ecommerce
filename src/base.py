"""
Модуль с общим абстрактным базовым классом для сущностей магазина.
"""

from abc import ABC, abstractmethod
from typing import Any


class BaseEntity(ABC):
    """Абстрактный базовый класс для всех сущностей магазина."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        Конструктор базового класса.
        Не абстрактный, чтобы можно было вызывать через super().
        """
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Абстрактный метод строкового представления."""
        pass
