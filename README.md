[//]: # (### Создание виртуального окружения)

[//]: # ()
[//]: # (```)

[//]: # ()
[//]: # (python3 -m venv venv)

[//]: # ()
[//]: # (```)

[//]: # ()
[//]: # (### Скачиваем репозиторий )

[//]: # ()
[//]: # (```)

[//]: # ()
[//]: # (git clone https://github.com/Telemazer555/api_restful-booker)

[//]: # ()
[//]: # (```)

[//]: # ()
[//]: # (### Устанавливаем библиотеки)

[//]: # ()
[//]: # (```)

[//]: # ()
[//]: # (pip install -r requirements.txt)

[//]: # ()
[//]: # (```)

[//]: # ()
[//]: # ()












# Backend API Testing Framework +-

Этот проект предназначен для автоматизированного тестирования backend API с использованием  **Requests**, и **Pytest**. Он предоставляет структурированный подход к написанию тестов, валидации схем ответов. ~~и генерации удобных отчетов.~~

## 🛠️ Стек технологий +-

- [Requests](https://pypi.org/project/requests/) – запуск тестов
- [Python](https://www.python.org/) – ~~строгая типизация~~ тут надо будет чёт написать 
- ~~[Allure](https://docs.qameta.io/allure/) – отчеты о прохождении тестов~~
- [Pydantic](https://docs.pydantic.dev/latest/) – валидация схем JSON


## 📁 Структура проекта ++

```
.
├── tests/                # API тесты
│   ├── conftest/         # Конфигурации для pytests (Хелперы для URL-ов)
├── src/
│   ├── core/             # Сессии, клиент, базовая логика +
│   ├── scenarios/        # Сценарии для тестов +
│   ├── data_models/      # Схемы для валидации ответов +
│   └── utils/            # Вспомогательные функции +
├── pyproject.toml        # Конфиг зависимостей для uv +
├── .env                  # Переменные окружения +
```

## 📦  Установка +

Репозиторий 
```bash

git clone <this-repo>
```
Пакетный менеджер
```bash

pip install uv
``` 

Установка всех зависимостей
``` bash

uv sync
```

## 🚀 Запуск тестов +

Запуск всех тестов: 
```bash

pytest -s -v
```

Запуск конкретного теста: 
```bash

pytest tests/test_api.py::TestBookingScenarios::test_get_and_verify

```

## ⚙️ Конфигурация

### Переменные окружения

Создайте `.env` файл в корне проекта:

```

BASE_URL = https://api.example.com
API_KEY = your-api-key
JSON_BODY = your-json_body
```

> Используйте [dotenv](https://pypi.org/project/python-dotenv/) для загрузки переменных.

## 🔗 Зависимости

```toml
[project]
name = "api-restful-booker"
version = "0.1.0"
description = "Add your description here"
requires-python = ">=3.13"
dependencies = [
    "faker>=37.8.0",
    "pytest>=8.4.2",
    "requests>=2.32.5",
    "pydantic>=2.11.9",
]

```

## 💡 Рекомендации +

- Старайтесь выносить `UUID` и данные в fixtures или конфиги.
- Используйте `responseSchema` для валидации каждого запроса.
- ~~Оборачивайте шаги в `allure.step()` для понятного отчета.~~

## ⚠️ CI

~~В CI-среде (например, GitHub Actions) отчет Allure формируется автоматически и передается в TestOps или другой агрегатор.~~