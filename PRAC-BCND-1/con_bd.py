""" Подключение модулей """
from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2

path = "postgresql://gen_user:Jde%25m%3F9P1%40@147.45.107.88:5432/default_db"


def connection(file):
    """ Функция соединения БД """
    connect = psycopg2.connect(file)
    return connect
conn = connection(path)


def execute(connect, sql):
    """ Функция отправки запроса в БД """
    cursor = connect.cursor()
    cursor.execute(sql)
    query = cursor.fetchone()
    return query

class Item(BaseModel):
    """ Класс для валидации """
    item_id: int



app = FastAPI()  # Создание приложения


@app.get("/skins/{item_id}")
async def read_id(
        item_id: Item):
    """ Функция чтения item_id """
    sql = f""" SELECT * FROM public.skins WHERE id = {item_id};  """
    query = execute(conn, sql)
    return {"id": query[0],
            "name": query[1],
            "amount": query[2],
            "game": query[3],
            "price": query[4],
            "day": query[5],
            "time": query[6]}
    


