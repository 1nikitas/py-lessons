
from src.adapters.adapter import Adapter
from src.schemas import OrderDetailsResponse
from sqlalchemy.orm import Session
from src.db.repositories import order_details_repository
from sqlalchemy.ext.asyncio import AsyncConnection

class OrderDetailsAdapter(Adapter):
    

    def get_all(self, connection: AsyncConnection, order_id: int):
        return order_details_repository.get_by_order_id(
            connection=connection, order_id=order_id
        )

    def create(self, connection: AsyncConnection, order_id: int, detail_data: OrderDetailsResponse):

        {
            'order_id': order_id, 
            **detail_data.model_dump()
        }


        return order_details_repository.create(
            connection=connection,
            order_id=order_id,
            detail_data=detail_data
        )
    
    def delete(self, connection: AsyncConnection, order_id: int, serial_number: str):
        return order_details_repository.delete_record_detail(
            connection=connection,
            order_id=order_id,
            serial_number=serial_number
        )