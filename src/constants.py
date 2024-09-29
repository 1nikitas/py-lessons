from enum import Enum


class ApiTags(str, Enum):
    ORDER_DETAILS='Order Details'
    ORDER='Order'