from sqlalchemy.orm import Session
from src.schemas import OrderResponse, OrderDetailsResponse
from src.adapters.order import OrderAdapter
from uvicorn.config import logger


class OrderService:
    def __init__(self):
        self.order_adapter = OrderAdapter()

    def get_all_orders(self, db: Session):
        return self.order_adapter.get_all(db)

    def get_order_by_id(self, db: Session, order_id: int):
        order = self.order_adapter.get_by_id(db, order_id)
        if not order:
            raise ValueError(f"Order with ID {order_id} does not exist.")
        return order

    def create_order(self, db: Session, order_data: OrderResponse):
        existing_order = self.order_adapter.get_by_id(db, order_data.order_id)
        if existing_order:
            raise ValueError(f"Order with ID {order_data.order_id} already exists.")
        logger.info(f"Creating order: {order_data}")
        return self.order_adapter.create(db, order_data)

    def add_order_detail(self, db: Session, order_id: int, detail_data: OrderDetailsResponse):

        # TODO: исправить нейминги и адаптеры

        order = self.get_order_by_id(db, order_id)
        return self.order_adapter.create_order_detail(db, order_id, detail_data)

    def delete_order(self, db: Session, order_id: int):
        order = self.get_order_by_id(db, order_id)
        return self.order_adapter.delete(db, order_id)

    def delete_order_detail(self, db: Session, order_id: int, serial_number: str):
        # TODO: исправить нейминги и адаптеры

        return self.order_adapter.delete_order_detail(db, order_id, serial_number)