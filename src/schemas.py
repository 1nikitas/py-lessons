from pydantic import BaseModel
from typing import List, Any
from datetime import datetime


class OrderDetailsResponse(BaseModel):
    string_id: int
    serial_number: str
    name: str
    amount: int
    order_id: int

    class Config:
        orm_mode = True


class OrderResponse(BaseModel):
    order_id: int
    name: str
    mail: str
    total_amount: int
    date: datetime
    details: List[Any] = []

    class Config:
        orm_mode = True

class Time(BaseModel):
    time: datetime

class OrderRequest(BaseModel):
    order_id: int
    name: str
    mail: str
    total_amount: int
    date: datetime
    details: List[Any] = []

    class Config:
        orm_mode = True

class OrderDetailRequest(BaseModel):
    string_id: int
    serial_number: str
    name: str
    amount: int
    order_id: int

    class Config:
        orm_mode = True
