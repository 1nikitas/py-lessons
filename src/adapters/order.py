from src.adapters.adapter import Adapter
from sqlalchemy.orm import Session
from src.schemas import OrderResponse, OrderDetailsResponse
from src.db.repositories import order_repository, order_details_repository
# from uvicorn.config import logger

class OrderAdapter(Adapter):
    
    def create(self, db: Session, order_data: OrderResponse):
        return order_repository.create(db, order_data)
    
    def create_order_detail(self, db: Session, order_id: int, detail_data: OrderDetailsResponse):
        return order_details_repository.create(db, detail_data, order_id)
    
    def get_all(self, db: Session):
        return order_repository.get_all(db)

    def get_by_id(self, db: Session, order_id: int):
        return order_repository.get_by_id(db, order_id)

    def delete(self, db: Session, order_id: int):
        return order_repository.remove(db, order_id)
    
    def delete_order_detail(self, db: Session, order_id: int, serial_number: str):
        return order_details_repository.delete_record_detail(db, order_id, serial_number)