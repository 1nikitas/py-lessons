from abc import ABC, abstractmethod
from typing import Any
from sqlalchemy.orm import Session
from src.db.repositories import order_repository, order_details_repository
from uvicorn.config import logger

class Adapter(ABC):

    @abstractmethod
    def get_all(self, db: Session) -> Any:
        """Get all records"""
        pass

    @abstractmethod
    def create(self, db: Session, data: Any) -> Any:
        """Create a new record"""
        pass

    @abstractmethod
    def delete(self, db: Session, id: int) -> Any:
        """Delete a record by ID"""
        pass
