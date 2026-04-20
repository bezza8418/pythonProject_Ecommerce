"""
Модуль с пользовательскими исключениями.
"""


class ZeroQuantityError(Exception):
    """Исключение, возникающее при попытке добавить товар с нулевым количеством."""

    def __init__(
        self, message: str = "Товар с нулевым количеством не может быть добавлен"
    ) -> None:
        self.message = message
        super().__init__(self.message)
