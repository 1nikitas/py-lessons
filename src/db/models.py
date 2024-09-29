from sqlalchemy import Integer, String, Column, DateTime, ForeignKey, UUID
from sqlalchemy.orm import relationship, Mapped, mapped_column
from src.db.base import Base
from datetime import datetime
import uuid

class Order(Base):
    __tablename__ = "user_orders"

    order_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(20))
    mail: Mapped[str] = mapped_column(String(30))
    total_amount: Mapped[int]
    date: Mapped[datetime] = mapped_column(default=datetime.now())

    details = relationship("OrderDetails", back_populates="order")

class OrderDetails(Base):
    __tablename__ = "order_details"

    string_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    serial_number: Mapped[str] = mapped_column(default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(20))
    amount: Mapped[int]
    order_id: Mapped[int] = mapped_column(ForeignKey("user_orders.order_id"))

    order = relationship("Order", back_populates="details")

