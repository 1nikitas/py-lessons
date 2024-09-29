from src.controllers.order import OrderController
from src.controllers.order_details import OrderDetailsController

def get_order_controller():
    return OrderController()

def get_order_details_controller():
    return OrderDetailsController()