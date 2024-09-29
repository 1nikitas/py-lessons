from sqlalchemy.orm import Session
from fastapi import HTTPException
from typing import List
from src.services.order_details import OrderDetailsService
from src.schemas import OrderDetailsResponse

class OrderDetailsController:
    def __init__(self):
        self.order_details_service = OrderDetailsService()

    def get_all_details_by_order_id(self, order_id: int, db: Session) -> List[OrderDetailsResponse]:
        try:
            return self.order_details_service.get_all_details_by_order_id(order_id, db)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def create_order_detail(self, order_id: int, detail_data: OrderDetailsResponse, db: Session) -> OrderDetailsResponse:
        try:
            return self.order_details_service.create_order_detail(order_id, detail_data, db)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def delete_order_detail(self, order_id: int, serial_number: str, db: Session) -> OrderDetailsResponse:
        try:
            return self.order_details_service.delete_order_detail(order_id, serial_number, db)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
