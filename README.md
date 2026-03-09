# E-commerce проект для изучения ООП

## 📋 Описание

Проект представляет собой ядро интернет-магазина с базовыми классами для работы с товарами и категориями. Реализована загрузка данных из/в JSON-файла.

### Основные возможности:
- ✅ Создание товаров с названием, описанием, ценой и количеством
- ✅ Создание категорий с названием, описанием и списком товаров
- ✅ Автоматический подсчет количества категорий и товаров
- ✅ Загрузка данных из JSON-файла
- ✅ Сохранение данных в JSON-файл

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
Создание товаров и категорий вручную:
```python
from src.product import Product
from src.category import Category


# Создание товаров
product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

# Создание категории
category = Category("Смартфоны", "Описание категории", [product1, product2])
```

Загрузка из JSON:
```python
from src.utils import load_categories_from_json

categories = load_categories_from_json("data/products.json")
for category in categories:
    print(f"{category.name}: {len(category.products)} товаров")
```

Сохранение в JSON:
```python
from src.utils import load_categories_from_json, save_categories_to_json

categories = load_categories_from_json("data/products.json")

save_categories_to_json(categories, "data/new_products.json")
```

Запуск демонстрации:
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
### Статистика покрытия (100%)
| Модуль        | Строк  | Пропущено | Покрытие |
|---------------|--------|-----------|----------|
| `__init__.py` | 4      | 0         | 100%     |
| `category.py` | 11     | 0         | 100%     |
| `product.py`  | 7      | 0         | 100%     |
| `utils.py`    | 23     | 0         | 100%     |
| **ИТОГО**     | **45** | **0**     | **100%** |

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
