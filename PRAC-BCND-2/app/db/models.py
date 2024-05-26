from pydantic import BaseModel
from typing import List
from Constants import *
import psycopg2


class Answer(BaseModel):
    question_id: int
    alternative_id: int


class UserAnswer(BaseModel):
    user_id: int
    answers: List[Answer]


def connection(url):
    try:
        conn = psycopg2.connect(url)
        return conn
    except Exception as error:
        print(f"Не удалось выполнить соединение к базе:{error}")
        return None


conn = connection(URL)
