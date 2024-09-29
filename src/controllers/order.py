"""
Базовые слои обработки запроса в fastapi:
1. Controllers - точка входа и предобработка для бизнес-логики
2. Services - обработка бизнес-логики
3. Adapters - промежуточного слоя между сервисами и репозиториями
4. Repositories - Репозитории отвечают за доступ к данным и взаимодействие с базой данных.
"""

from sqlalchemy.orm import Session
from fastapi import HTTPException
from typing import List
from uvicorn.config import logger
from src.services.order import OrderService
from src.schemas import OrderResponse, OrderDetailsResponse, OrderDetailRequest

class OrderController:
    def __init__(self):
        self.order_service = OrderService()

    def get_all_orders(self, db: Session) -> List[OrderResponse]:
        try:
            return self.order_service.get_all_orders(db)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_order_by_id(self, order_id: int, db: Session) -> OrderResponse:
        order = self.order_service.get_order_by_id(db, order_id)
        

        if order is None:
            raise HTTPException(
                status_code=404,
                detail=f"Order with ID {order_id} does not exist."
            )
        return order


    def create_order(self, order_data: OrderResponse, db: Session) -> OrderResponse:
        try:
            logger.info(f"order: {order_data}")
            return self.order_service.create_order(db, order_data)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def add_order_detail(self, order_id: int, detail_data: OrderDetailRequest, db: Session) -> OrderResponse:
        try:
            return self.order_service.add_order_detail(db, order_id, detail_data)
        except ValueError as e:
            raise HTTPException(status_code=404, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def delete_order(self, order_id: int, db: Session) -> OrderResponse:
        try:
            return self.order_service.delete_order(db, order_id)
        except ValueError as e:
            raise HTTPException(status_code=404, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def delete_order_detail(self, order_id: int, serial_number: str, db: Session) -> OrderDetailsResponse:
        try:
            return self.order_service.delete_order_detail(db, order_id, serial_number)
        except ValueError as e:
            raise HTTPException(status_code=404, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

