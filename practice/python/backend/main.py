

from typing import Tuple, Optional, Annotated

from fastapi import FastAPI, Path
from pydantic import BaseModel
from datetime import datetime


class Delivery(BaseModel):
    timestamp: datetime
    dimensions: Tuple[int, int] # (1,2)


d = Delivery(timestamp='2020-01-02T03:04:05Z', dimensions=['10', '20'])
print(d.dimensions)

#
# def summer(a: int, b: str):
#
#     if isinstance(a, int) and isinstance(b, str):
#         print('OK')
#     else:
#         raise TypeError



# ctrl + ?
app = FastAPI()
#
# dict_ = {
#     "item_1": 1,
#     "item_2": 2,
#     "item_3": 3
# }
#
#
# @app.get("/")
# async def root():
#     """
#     HTTP:
#         - запросы
#         - ответы
#
#     Структура:
#         1.start line
#         2. HTTP заголовки
#         3. пустая строчка
#         4. опциональное тело сообщения
#
#     Методы:
#         1. GET (?param=value)
#         2. POST (?param=value)
#         3. PUT
#         4. DELETE (Denial of Service, DoS)
#         5. OPTIONS
#         6. PATCH
#
#     URL - Uniform Resource Locator
#
#     Поле Scheme используется для указания используемого протокола,
#     всегда сопровождается двоеточием и двумя косыми чертами (://).
#
#     Host указывает местоположение ресурса, в нем может быть как доменное имя, так и IP-адрес.
#
#     Port, как можно догадаться, позволяет указать номер порта, по которому следует обратиться к серверу.
#     Оно начинается с двоеточия (:), за которым следует номер порта.
#     При отсутствии данного элемента номер порта будет выбран по умолчанию в соответствии с указанным значением Scheme
#     (например, для http:// это будет порт 80).
#
#     Далее следует поле Path. Оно указывает на ресурс, к которому производится обращение.
#      Если данное поле не указано, то сервер в большинстве случаев вернет указатель по умолчанию (например index.html).
#
#     Поле Query String начинается со знака вопроса (?), за которым следует пара «параметр-значение»,
#      между которыми расположен символ равно (=). В поле Query String могут быть переданы несколько параметров с помощью символа амперсанд (&) в качестве разделителя.
#
#     https://pro-api.coingecko.com/api/v3/simple/?coin=bitcoin&coin=eth
#     """
#     return {"message": "Hello World"}
#
#
# @app.get("/items/{item_name}")
# async def read_item(item_name: int): # type hinting
#     if item_name is None:
#         return {
#             "error": "Item name is required"
#         }
#
#     id_ = dict_.get(item_name)
#
#     if not id_:
#         return {
#             "error": "Not Found"
#         }
#
#     return {
#         "id": id_
#     }


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None



@app.put("/items/{item_id}")
async def update_item(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: str | None = None,
    item: Item | None = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results
















