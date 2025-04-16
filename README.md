### ТЗ

Создать REST API на базе LiteStar (Python 3.12) с CRUD-операциями для таблицы user в PostgreSQL.
API должен поддерживать:
- Свагер
- Создание пользователя.
- Получение списка пользователей.
- Получение данных одного пользователя.
- Обновление данных пользователя.
- Удаление пользователя.

Стек технологий:
- Backend: LiteStar (версия 2.x).
- База данных: PostgreSQL + Advanced-SQLAlchemy.
- Инфраструктура: Docker.
- пакетный менеджер: Poetry 1.8.3.

требования к таблице user
таблица user:
```
   id BIGINT PRIMARY KEY, автоинкремент
   name
   surname
   password
   created_at TIMESTAMP UTC-0
   updated_at TIMESTAMP UTC-0
  ```
Настроенные зависимости:
```
python = "^3.12"
python-dotenv = "^1"
litestar = { extras = ["standard"], version = "^2" }
litestar-granian = "^0"
litestar-asyncpg = "^0"
advanced-alchemy = "^0.20"
msgspec = "^0.18.6"
```


### Запуск

- Скопируйте переменные окружения
```bash
  cp .env.template .env
```

- Запустите докер
```bash
    docker compose up --build -d
```

- Перейдите в браузере на [`http://0.0.0.0:8000`](http://0.0.0.0:8000/schema/swagger)(или номер порта который укажите в .env файле)