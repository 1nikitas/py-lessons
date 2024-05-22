from fastapi import FastAPI
from pydantic import BaseModel
from psycopg2.pool import Pool


# Параметры подключения к БД
DB_URL = "postgresql://gen_user:Jde%25m%3F9P1%40@147.45.107.88:5432/default_db"


# Создание пула соединений к БД
db_pool = Pool(minsize=1, maxsize=10, host="147.45.107.88", database="default_db", 
                user="gen_user", password="Jde%25m%3F9P1", port=5432)


class Item(BaseModel):
    item_id: int


app = FastAPI()


def get_db_connection():
    """ Функция получения соединения из пула """
    try:
        return db_pool.getconn()
    except Exception as e:
        print(f"Не удалось получить соединение: {e}")
        return None


def close_db_connection(connection):
    """ Функция возврата соединения в пул """
    if connection:
        connection.close()
        db_pool.putconn(connection)


@app.get("/skins/{item_id}")
async def read_item(item_id: Item):
    """ Функция чтения информации о предмете по item_id """
    with get_db_connection() as conn:
        cursor = conn.cursor()
        sql = f"""SELECT * FROM public.skins WHERE id = {item_id.item_id};"""
        cursor.execute(sql)
        item = cursor.fetchone()

        if not item:
            return {"message": "Предмет не найден"}

        return {
            "id": item[0],
            "name": item[1],
            "amount": item[2],
            "game": item[3],
            "price": item[4],
            "day": item[5],
            "time": item[6]
        }


@app.on_event("shutdown")
def shutdown_event():
    """ Функция закрытия соединения при выключении приложения """
    db_pool.closeall()
