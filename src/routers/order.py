from src.db.base import get_connection
from src.controllers.order import OrderController
from src.controllers.order_details import OrderDetailsController
from src.fabrics import get_order_controller, get_order_details_controller
from fastapi import APIRouter, Depends
import uvicorn
from sqlalchemy.orm import Session
from typing import List
from uvicorn.config import logger
from src.schemas import OrderDetailsResponse

order_view = APIRouter(prefix='/static')

@order_view.post("/order/{id}/detail", response_model=OrderDetailsResponse)
async def create_order_detail(
    id: int,
    detail_data: OrderDetailsResponse, db: Session = Depends(get_connection),
    order_details_controller: OrderDetailsController = Depends(get_order_details_controller)  
):
    """Add new detail to order"""
    return order_details_controller.create_order_detail(id, detail_data, db)

@order_view.get("/order/{id}/details", response_model=List[OrderDetailsResponse])
async def read_order_details(
    id: int,
    db: Session = Depends(get_connection),
    order_details_controller: OrderDetailsController = Depends(get_order_details_controller)
):
    """Fetch all details for a specific order"""
    return order_details_controller.get_all_details_by_order_id(id, db)

@order_view.delete("/order/{id}/detail/{serial_number}", response_model=OrderDetailsResponse)
async def remove_order_detail(
    id: int,
    serial_number: str,
    db: Session = Depends(get_connection),
    order_details_controller: OrderDetailsController = Depends(get_order_details_controller)
):
    """Remove detail from order"""
    return order_details_controller.delete_order_detail(id, serial_number, db)