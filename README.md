# To-Do API

Простий REST API для управління задачами, написаний на Python + FastAPI.

## Технології
- Python 3.11+
- FastAPI
- Pydantic
- Uvicorn

## Запуск
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Відкрий у браузері: http://127.0.0.1:8000/docs

## Ендпоінти
| Метод  | URL            | Дія             |
|--------|----------------|-----------------|
| GET    | /todos         | Всі задачі      |
| POST   | /todos         | Створити задачу |
| GET    | /todos/{id}    | Одна задача     |
| PATCH  | /todos/{id}    | Оновити задачу  |
| DELETE | /todos/{id}    | Видалити задачу |
