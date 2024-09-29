
from sqlalchemy.orm import Session
from src.adapters.order_detail import OrderDetailsAdapter
from src.schemas import OrderDetailsResponse
from sqlalchemy.ext.asyncio import AsyncConnection

class OrderDetailsService:
    def __init__(self):
        self.order_details_adapter = OrderDetailsAdapter()

    def get_all_details_by_order_id(self, connection: AsyncConnection, order_id: int):
        return self.order_details_adapter.get_all(
            connection=connection,
            order_id=order_id
        )

    def create_order_detail(self, connection: AsyncConnection, order_id: int, detail_data: OrderDetailsResponse):
        return self.order_details_adapter.create(
            connection=connection,
            order_id=order_id,
            detail_data=detail_data
        )

    def delete_order_detail(self, connection: AsyncConnection, order_id: int, serial_number: str):
        return self.order_details_adapter.delete(
            connection=connection,
            order_id=order_id,
            serial_number=serial_number
        )