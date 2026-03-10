# E-commerce проект для изучения ООП

## 📋 Описание

Проект представляет собой ядро интернет-магазина с базовыми классами для работы с товарами и категориями. Реализована загрузка данных из/в JSON-файла.

### Основные возможности:
- ✅ Создание товаров с названием, описанием, ценой и количеством
- ✅ Создание категорий с названием, описанием и списком товаров
- ✅ Автоматический подсчет количества категорий и товаров
- ✅ Загрузка данных из JSON-файла
- ✅ Сохранение данных в JSON-файл
- ✅ Приватные атрибуты для защиты данных (`__products`, `__price`)
- ✅ Геттеры и сеттеры с валидацией
- ✅ Класс-метод для создания товаров из словаря
- ✅ Подтверждение при понижении цены

## 🚀 Установка

1. **Клонируйте репозиторий:**
```bash
git clone https://github.com/bezza8418/pythonProject_Ecommerce
cd pythonProject_Ecommerce
```

Установите зависимости через Poetry:
```bash
poetry install
```

## 📚 Использование
### Базовые операции:
- Создание товаров и категорий вручную:
```python
from src.product import Product
from src.category import Category

# Создание товаров
product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

# Создание категории
category = Category("Смартфоны", "Описание категории", [product1, product2])
```

- Загрузка из JSON:
```python
from src.utils import load_categories_from_json

# Загружаем категории из файла
categories = load_categories_from_json("data/products.json")

# Выводим информацию о каждой категории
for cat in categories:
    print(f"{cat.name}: {len(cat.products_list)} товаров")
```

- Сохранение в JSON:
```python
from src.utils import load_categories_from_json, save_categories_to_json

# Загружаем категории из файла
categories = load_categories_from_json("data/products.json")

# Сохраняем их в новый файл
save_categories_to_json(categories, "data/new_products.json")
```

### 🆕 Новые возможности (версия 2.0)
Защита данных:
- Атрибут products в классе Category теперь приватный (__products)
- Атрибут price в классе Product теперь приватный (__price)

Добавление товаров в категорию:
```python
from src.product import Product
from src.category import Category

# Создаем товары
product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

# Создаем категорию
category = Category("Смартфоны", "Описание категории", [product1, product2])

# Создаем новый товар
new_product = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

# Добавляем товар через специальный метод
category.add_product(new_product)
```

Просмотр товаров через геттер
```python
# Предположим, у нас есть категория с товарами
from src.product import Product
from src.category import Category

# Создаем товары
product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

# Создаем категорию
category = Category("Смартфоны", "Описание категории", [product1, product2])

# Геттер возвращает красиво отформатированную строку
print(category.products)
# Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.
# Iphone 15, 210000.0 руб. Остаток: 8 шт.
```

Создание товаров из словаря
```python
from src.product import Product

# Создаем товар из словаря
data = {
    "name": "Samsung Galaxy S23 Ultra",
    "description": "256GB, Серый цвет, 200MP камера",
    "price": 180000.0,
    "quantity": 5
}
product = Product.new_product(data)

# При наличии дубликатов происходит объединение
product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
existing_products = [product1, product2]

# Создаем новый товар с проверкой дубликатов
data2 = {
    "name": "Samsung Galaxy S23 Ultra",
    "description": "Новое описание",
    "price": 190000.0,
    "quantity": 3
}
new_product = Product.new_product(data2, existing_products)
# Количество складывается (5+3=8), цена выбирается максимальная (190000.0)
```

Безопасное изменение цены
```python
from src.product import Product

product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

product.price = 200000.0  # Повышение цены без подтверждения
product.price = 150000.0  # Понижение цены требует подтверждения
# Вы действительно хотите понизить цену? (y/n)
```

### Запуск демонстрации:
```bash
poetry run python main.py
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
### Статистика покрытия (89%)
| Модуль        | Строк   | Пропущено | Покрытие |
|---------------|---------|-----------|----------|
| `__init__.py` | 4       | 0         | 100%     |
| `category.py` | 25      | 0         | 100%     |
| `product.py`  | 68      | 8         | 88%      |
| `utils.py`    | 51      | 9         | 82%      |
| **ИТОГО**     | **148** | **17**    | **89%**  |

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
│   ├── category.py         # Класс Category
│   ├── product.py          # Класс Product
│   └── utils.py            # Утилиты для работы с JSON
├── tests/                  # Тесты
│   ├── __init__.py
│   ├── test_category.py
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
