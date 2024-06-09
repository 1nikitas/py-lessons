from pydantic import BaseModel, EmailStr
from typing import List
from Constants import *
import psycopg2


class Answer(BaseModel):
    question_id: int
    alternative_id: int


class UserAnswer(BaseModel):
    user_id: int
    answers: List[Answer]

class CreateUser(BaseModel):
    name: str
    mail: EmailStr
    phone: str

class DeleteUser(BaseModel):
    id: int

class UpdateUser(BaseModel):
    name: str
    mail: EmailStr
    phone: str

def connection(url):
    try:
        conn = psycopg2.connect(url)
        return conn
    except Exception as error:
        print(f"Не удалось выполнить соединение к базе:{error}")
        return None


conn = connection(URL)
