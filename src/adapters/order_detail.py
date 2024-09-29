
from src.adapters.adapter import Adapter
from src.schemas import OrderDetailsResponse
from sqlalchemy.orm import Session
from src.db.repositories import order_details_repository

class OrderDetailsAdapter(Adapter):

    def get_all(self, db: Session, order_id: int):
        return order_details_repository.get_by_order_id(db, order_id)

    def create(self, db: Session, order_id: int, detail_data: OrderDetailsResponse):
        return order_details_repository.create(db, order_id, detail_data)
    
    def delete(self, db: Session, order_id: int, serial_number: str):
        return order_details_repository.delete_record_detail(db, order_id, serial_number)