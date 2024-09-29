from typing import Type, TypeVar, List, Optional
from src.exceptions import ObjectNotFound
from sqlalchemy.orm import Session
from src.db.models import Order, OrderDetails
from uvicorn.config import logger
from src.schemas import OrderResponse, OrderDetailsResponse


ModelType = TypeVar("ModelType")

class CRUDBase:
    def __init__(self, model: Type[ModelType]):
        self.model = model
    
    def get_all(self, db: Session) -> List[ModelType]:
        return db.query(self.model).all()
    
    def get_by_id(self, db: Session, id: int) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.order_id == id).first()
    
    def create(self, db: Session, obj_in: OrderResponse) -> OrderResponse:
        db.add(obj_in)
        db.commit()
        db.refresh(obj_in)
        logger.info(f"obj_in: {obj_in}")
        return obj_in
    
    def remove(self, db: Session, id: int) -> ModelType:
        obj = db.query(self.model).get(id)
        db.delete(obj)
        db.commit()
        return obj


class OrderRepository(CRUDBase):
    def __init__(self):
        super().__init__(Order)
    
    def update_total_amount(self, db: Session, order_id: int, amount: int, operation: str):
        order = db.query(Order).filter(Order.order_id == order_id).first()
        if not order:
            raise ObjectNotFound("Order not found")

        if operation == "plus":
            order.total_amount += amount
        elif operation == "minus":
            order.total_amount -= amount
        db.commit()

class OrderDetailsRepository(CRUDBase):
    def __init__(self):
        super().__init__(OrderDetails)

    def delete_record_detail(self, db: Session, order_id: int, serial_number: str):
        detail = db.query(self.model).filter(self.model.serial_number == serial_number).first()
        if detail:
            order_repository.update_total_amount(db, order_id, detail.amount, "minus")
            db.delete(detail)
            db.commit()
            return detail
        return None


order_repository = OrderRepository()
order_details_repository = OrderDetailsRepository()
