from typing import Type, TypeVar, List, Optional
from src.exceptions import ObjectNotFound
from sqlalchemy.orm import Session
from src.db.models import Order, OrderDetails
from uvicorn.config import logger
from src.schemas import OrderResponse, OrderDetailsResponse
from sqlalchemy.ext.asyncio import AsyncConnection


ModelType = TypeVar("ModelType")

class CRUDBase:
    def __init__(self, model: Type[ModelType]):
        self.model = model
    
    def get_all(self, connection: AsyncConnection) -> List[ModelType]:
        return connection.query(self.model).all()
    
    def get_by_id(self, connection: AsyncConnection, id: int) -> Optional[ModelType]:
        return connection.query(self.model).filter(self.model.order_id == id).first()
    
    def create(self, connection: AsyncConnection, obj_in: dict) -> OrderResponse:
        connection.add(obj_in)
        connection.commit()
        connection.refresh(obj_in)
        logger.info(f"obj_in: {obj_in}")
        return obj_in
    
    def remove(self, connection: AsyncConnection, id: int) -> ModelType:
        obj = connection.query(self.model).get(id)
        connection.delete(obj)
        connection.commit()
        return obj


class OrderRepository(CRUDBase):
    def __init__(self):
        super().__init__(Order)
    
    def update_total_amount(self, connection: AsyncConnection, order_id: int, amount: int, operation: str):
        order = connection.query(Order).filter(Order.order_id == order_id).first()
        if not order:
            raise ObjectNotFound("Order not found")

        if operation == "plus":
            order.total_amount += amount
        elif operation == "minus":
            order.total_amount -= amount
        connection.commit()

class OrderDetailsRepository(CRUDBase):
    def __init__(self):
        super().__init__(OrderDetails)

    def delete_record_detail(self, connection: AsyncConnection, order_id: int, serial_number: str):
        detail = connection.query(self.model).filter(self.model.serial_number == serial_number).first()
        if detail:
            order_repository.update_total_amount(connection, order_id, detail.amount, "minus")
            connection.delete(detail)
            connection.commit()
            return detail
        return None


order_repository = OrderRepository()
order_details_repository = OrderDetailsRepository()
