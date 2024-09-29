from sqlalchemy.orm import Session
from fastapi import HTTPException
from typing import List
from src.services.order_details import OrderDetailsService
from src.schemas import OrderDetailsResponse
from sqlalchemy.ext.asyncio import AsyncConnection

class OrderDetailsController:
    def __init__(self):
        self.order_details_service = OrderDetailsService()

    def get_all_details_by_order_id(self, connection: AsyncConnection, order_id: int) -> List[OrderDetailsResponse]:
        return self.order_details_service.get_all_details_by_order_id(
            connection=connection,
            order_id=order_id
        )


    def create_order_detail(self, connection: AsyncConnection, order_id: int, detail_data: OrderDetailsResponse) -> OrderDetailsResponse:
        return self.order_details_service.create_order_detail(
            connection=connection,
            order_id=order_id,
            detail_data=detail_data
        )
        
    def delete_order_detail(self, connection: AsyncConnection, order_id: int, serial_number: str) -> OrderDetailsResponse:
        return self.order_details_service.delete_order_detail(
            connection=connection,
            order_id=order_id,
            serial_number=serial_number
        )
