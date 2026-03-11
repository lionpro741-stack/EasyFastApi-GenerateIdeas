from fastapi import FastAPI, HTTPException, Form
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
import random


app = FastAPI(title="Contacts App")


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DEFAULT_IDEAS = [
    "Угадай число",
    "Камень ножницы бумага",
    "Онлайн викторина",
    "Змейка с рекордами",
    "To-Do список",
    "Сайт заметок",
    "Трекер привычек",
    "Трекер времени",
    "Мини блог",
    "Мини соцсеть",
    "Онлайн чат",
    "Гостевая книга",
    "Генератор стартап идей",
    "Генератор названий игр",
    "Генератор паролей",
    "Генератор историй",
    "Онлайн голосование",
    "Случайный фильм или игра",
    "Тест личности",
    "Карточки для изучения"
]

ideas = DEFAULT_IDEAS.copy()




@app.get('/')
async def get_idea():
    if not ideas:
        return {"Ошибка": "Нету идей"}
    ran = random.choice(ideas)
    return {"Идея": ran}

@app.get('/all_ideas')
async def get_all_ideas():
    return {"Все идеи": ideas}

class Add(BaseModel):
    idea: str


@app.post('/add_idea')
async def add_idea(i:Add):
    if i.idea.strip():
        ideas.append(i.idea)
        return {"Ваша идея": i.idea}
    else:
        raise HTTPException(status_code=405,detail="Нету идеи!")

@app.delete('/delete_idea')
async def delete_idea(description: str):
    if description in ideas:
        ideas.remove(description)
        return {"Успешно": "Идея удалена"}
    else:
        raise HTTPException(status_code=404,detail="Не нашлось идеи!")

@app.delete('/delete_ideas')
async def delete_all_ideas():
    ideas.clear()
    return {"Успешно": "Все удалено!"}


