# Підключаємо бібліотеки
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import uuid

app = FastAPI(title="To-Do API", description="Простий API для задач")

# "База даних" в пам'яті
todos: dict = {}

# Модель задачі — які поля вона має
class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = ""

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    done: Optional[bool] = None

# GET / — головна сторінка
@app.get("/")
def root():
    return {"message": "Ласкаво просимо до To-Do API!"}

# GET /todos — отримати всі задачі
@app.get("/todos")
def get_todos():
    return list(todos.values())

# POST /todos — створити нову задачу
@app.post("/todos", status_code=201)
def create_todo(todo: TodoCreate):
    todo_id = str(uuid.uuid4())
    new_todo = {
        "id": todo_id,
        "title": todo.title,
        "description": todo.description,
        "done": False
    }
    todos[todo_id] = new_todo
    return new_todo

# GET /todos/{id} — отримати одну задачу
@app.get("/todos/{todo_id}")
def get_todo(todo_id: str):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Задачу не знайдено")
    return todos[todo_id]

# PATCH /todos/{id} — оновити задачу (позначити як виконану)
@app.patch("/todos/{todo_id}")
def update_todo(todo_id: str, update: TodoUpdate):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Задачу не знайдено")
    if update.title is not None:
        todos[todo_id]["title"] = update.title
    if update.done is not None:
        todos[todo_id]["done"] = update.done
    return todos[todo_id]

# DELETE /todos/{id} — видалити задачу
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: str):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Задачу не знайдено")
    deleted = todos.pop(todo_id)
    return {"deleted": deleted["title"]}