from typing import Type, TypeVar, List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import insert, update, select, delete
from src.db.models import Order, OrderDetails
from src.schemas import OrderResponse, OrderDetailsResponse
from src.db.query_processing import execute_all


ModelType = TypeVar("ModelType")

class CRUD:
    def __init__(self, model: Type[ModelType]):
        self.model = model
    
    def get_records(self, db: Session, filter: List = []) -> List[ModelType]:
        query = db.query(self.model)
        for condition in filter:
            query = query.filter(condition)
        return query.all()
    
    def get_record(self, db: Session, filters: List = []) -> Optional[ModelType]:
        query = db.query(self.model)
        for condition in filters:
            query = query.filter(condition)
        return query.first()

    def add_record(self, new_order: OrderResponse):
        insert_order = insert(self.model).values(name=new_order.name, mail=new_order.mail, total_amount=new_order.total_amount, date=new_order.date)
        execute_all(insert_order)

    def add_records(self, new_detail: OrderDetailsResponse, id: int):
        stmt = insert(self.model).values(name=new_detail.name, amount=new_detail.amount, order_id=id)
        execute_all(stmt)
        self.update_record_total(id, new_detail.amount, "plus")

    @staticmethod
    def update_record_total(id: int, amount: int, plus_or_minus: str):
        select_total_amount = select(Order.total_amount).where(Order.order_id == id)

        if plus_or_minus == "plus":
            total_amount = execute_all(select_total_amount).fetchone()[0] + amount
        elif plus_or_minus == "minus":
            total_amount = execute_all(select_total_amount).fetchone()[0] - amount

        stmt = (update(Order).where(Order.order_id == id).values(total_amount=total_amount))
        execute_all(stmt)

    def delete_record(self, id: int):
        stmt2 = delete(OrderDetails).where(OrderDetails.order_id == id)
        execute_all(stmt2)
        stmt1 = delete(Order).where(Order.order_id == id)
        execute_all(stmt1)

    def delete_record_detail(self, id: int, db: Session, filter: List = []) -> Optional[ModelType]:
        old_detail = db.query(self.model).filter(filter[0]).first()
        self.update_record_total(id, old_detail.amount, "minus")

        kill_detail = delete(self.model).where(filter[0])
        execute_all(kill_detail)

        return old_detail


order_crud = CRUD(Order)
order_details_crud = CRUD(OrderDetails)

def get_orders(db: Session):
    return order_crud.get_records(db)

def get_order(db: Session, order_id: int):
    return order_crud.get_record(db, [Order.order_id == order_id])

def get_order_details(db: Session, order_id: int):
    return order_details_crud.get_records(db, [OrderDetails.order_id == order_id])

def add_order(new_order: OrderResponse):
    order_crud.add_record(new_order)

def add_order_details(new_detail: OrderDetailsResponse, id:int):
    order_details_crud.add_records(new_detail, id)

def delete_order(id: int):
    order_crud.delete_record(id)

def delete_detail(id: int, serial_number: str, db: Session):
    return order_details_crud.delete_record_detail(id, db, [serial_number == OrderDetails.serial_number])
