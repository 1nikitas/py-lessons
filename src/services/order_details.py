
from sqlalchemy.orm import Session
from src.adapters.order_detail import OrderDetailsAdapter
from src.schemas import OrderDetailsResponse

class OrderDetailsService:
    def __init__(self):
        self.order_details_adapter = OrderDetailsAdapter()

    def get_all_details_by_order_id(self, order_id: int, db: Session):
        return self.order_details_adapter.get_all(db, order_id)

    def create_order_detail(self, order_id: int, detail_data: OrderDetailsResponse, db: Session):
        return self.order_details_adapter.create(db, order_id, detail_data)

    def delete_order_detail(self, order_id: int, serial_number: str, db: Session):
        return self.order_details_adapter.delete(db, order_id, serial_number)