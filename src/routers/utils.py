import datetime

from fastapi import APIRouter
from src.schemas import Time


time_view = APIRouter(prefix='/time')


@time_view.get("/time/now", response_model=Time)
async def read_time_now():
    """Fetch current time"""
    return {
        "time": datetime.datetime.now()
    }