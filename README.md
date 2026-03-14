# E-commerce проект для изучения ООП

## 📋 Описание

Ядро интернет-магазина с классами для товаров, категорий и заказов.

### Основные возможности:
- ✅ Товары, категории, заказы
- ✅ Загрузка/сохранение в JSON
- ✅ Приватные атрибуты, геттеры/сеттеры
- ✅ Классы-наследники (`Smartphone`, `LawnGrass`)
- ✅ Магические методы и итераторы
- ✅ Логирование создания объектов

## 🚀 Установка

```bash
git clone https://github.com/bezza8418/pythonProject_Ecommerce
cd pythonProject_Ecommerce
poetry install
```

## 📚 Примеры использования
### Товары и категории
```python
from src.product import Product
from src.category import Category

product = Product("Смартфон", "Описание", 50000.0, 10)
category = Category("Электроника", "Описание", [product])
```

### Заказы
```python
from src.product import Product
from src.order import Order

# Сначала создаем товар
product = Product("Смартфон", "Описание", 50000.0, 10)

# Потом создаем заказ
order = Order(product, 2)
print(order)  # Заказ: Смартфон x2 = 100000.0 руб.
```

## Логирование создания
```python
# При создании автоматически выводится:
# Создан объект: Product('Смартфон', 'Описание', 50000.0, 10)
```

## 🧪 Тестирование
```bash
# Запуск всех тестов
poetry run pytest

# Запуск с подробным выводом
poetry run pytest -v

# Запуск с отчетом о покрытии
poetry run pytest --cov=src --cov-report=term-missing

# Генерация HTML-отчета
poetry run pytest --cov=src --cov-report=html
```

## 📊 Покрытие тестами
### Статистика покрытия (95%)
| Модуль            | Строк   | Пропущено | Покрытие |
|-------------------|---------|-----------|----------|
| `__init__.py`     | 6       | 0         | 100%     |
| `base.py`         | 5       | 0         | 100%     |
| `base_product.py` | 3       | 0         | 100%     |
| `category.py`     | 46      | 1         | 98%      |
| `mixins.py`       | 6       | 1         | 83%      |
| `order.py`        | 12      | 0         | 100%     |
| `product.py`      | 88      | 0         | 100%     |
| `utils.py`        | 51      | 9         | 82%      |
| **ИТОГО**         | **217** | **11**    | **95%**  |

Просмотр отчета:

После генерации HTML-отчета откройте htmlcov/index.html в браузере для детального просмотра покрытия.

## 🔧 Инструменты качества кода
```bash
# Проверка стиля
poetry run flake8 src/ tests/

# Форматирование
poetry run black src/ tests/
poetry run isort src/ tests/

# Проверка типов
poetry run mypy src/
```

## 📁 Структура проекта

```
pythonProject_Ecommerce/
├── data/                   # Данные в формате JSON
├── htmlcov/                # Отчет о покрытии тестами
├── src/                    # Исходный код
│   ├── __init__.py
│   ├── base.py             # Абстрактный базовый класс BaseEntity
│   ├── base_product.py     # Абстрактный базовый класс для продуктов
│   ├── category.py         # Класс Category
│   ├── mixins.py           # Классы-миксины (CreationMixin)
│   ├── order.py            # Класс Order
│   ├── product.py          # Класс Product
│   └── utils.py            # Утилиты для работы с JSON
├── tests/                  # Тесты
│   ├── __init__.py
│   ├── test_category.py
│   ├── test_order.py
│   ├── test_product.py
│   └── test_utils.py
├── .flake8                 # Конфигурация flake8
├── .gitignore              # Игнорируемые файлы
├── main.py                 # Точка входа
├── poetry.lock             # Зависимости poetry
├── pyproject.toml          # Конфигурация проекта
└── README.md               # Документация
```


## 🚀 Запуск проекта

```powershell
# Установка зависимостей
poetry install

# Запуск тестов
poetry run pytest

# Запуск программы
poetry run python main.py

# Проверка линтерами
poetry run flake8 src/ tests/
poetry run black src/ tests/ --check
poetry run isort src/ tests/ --check-only
poetry run mypy src/
```

## 🌿 Работа с Git
```powershell
# Создание ветки для разработки
git checkout -b develop

# Добавление файлов
git add .
git commit -m "Initial commit: add e-commerce project structure"

# Создание ветки для домашнего задания
git checkout -b feature/ecommerce-oop

# После выполнения задания
git add .
git commit -m "Add Product and Category classes with tests"

# Создание Pull Request на GitHub
git push origin feature/ecommerce-oop
```
## 📄 Лицензия
Проект разработан в учебных целях.

## 📞 Контакты

Автор: [bezza8418](https://github.com/bezza8418)

---
