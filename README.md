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


## 📁 Структура проекта +

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

## 📦  Установка + -

```bash

git clone <this-repo>
cd <project-folder>
...
```

>  Заполняем (.env) Наполение файла находится в (.env-copy)**

## 🚀 Запуск тестов

Обычный запуск всех тестов: +
```bash

pytest -s -v
```

Запуск конкретного файла: -
```bash

npx pytest test tests/negativeGetBuyout.test.ts
```

[//]: # (## 📊 Allure-отчет локально)

[//]: # ()
[//]: # (1. Запуск тестов и генерация отчета:)

[//]: # (   ```bash)

[//]: # (   )
[//]: # (   npx playwright test && allure serve allure-results)

[//]: # (   ```)

[//]: # ()
[//]: # (2. Если установлен глобально:)

[//]: # (   ```bash)

[//]: # (   )
[//]: # (   npm install -g allure-commandline)
[//]: # (   ```)

[//]: # ()
[//]: # (## 📌 Пример теста)

[//]: # ()
[//]: # (```ts)

[//]: # ()
[//]: # (test&#40;'Проверка метода GET /v1/buyout-objects', async &#40;&#41; => {)

[//]: # (    allure.label&#40;'il1', '02_Тестирование BE'&#41;;)

[//]: # (    allure.tag&#40;'SMOKE'&#41;;)

[//]: # (    allure.suite&#40;'GET /v1/buyout-objects'&#41;;)

[//]: # ()
[//]: # (    const session: APIClient = await defaultUserSession&#40;&#41;;)

[//]: # ()
[//]: # (    await allure.step&#40;'✅ Запрос с валидным UUID — 200 OK', async &#40;&#41; => {)

[//]: # (        await session.request&#40;{)

[//]: # (            method: 'GET',)

[//]: # (            endpoint: amInfoEndpoints.getAmInfo&#40;'ffdbc4ab-73f0-4b9d-b89e-bf76efec7a30'&#41;,)

[//]: # (            headers: { 'x-api-key': 'your-api-key' },)

[//]: # (            expectedStatus: 200,)

[//]: # (            responseSchema: buyoutObjectResponseSchema,)

[//]: # (        }&#41;;)

[//]: # (    }&#41;;)

[//]: # (}&#41;;)

[//]: # (```)

## ⚙️ Конфигурация

### Переменные окружения

Создайте `.env` файл в корне проекта (если требуется):

```

BASE_URL=https://api.example.com
API_KEY=your-api-key
```

> Используйте [dotenv](https://www.npmjs.com/package/dotenv) для загрузки переменных.

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

## 💡 Рекомендации

- Старайтесь выносить `UUID` и данные в fixtures или конфиги.
- Используйте `responseSchema` для валидации каждого запроса.
- Оборачивайте шаги в `allure.step()` для понятного отчета.

## ⚠️ CI

В CI-среде (например, GitHub Actions) отчет Allure формируется автоматически и передается в TestOps или другой агрегатор.