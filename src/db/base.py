from contextlib import asynccontextmanager

from pydantic_core import MultiHostUrl
from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import (
    AsyncConnection,
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine
)
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()
Base = declarative_base(metadata=metadata)


class DatabaseManager:

    def __init__(self) -> None:
        self._engine: AsyncEngine | None = None
        self._session_maker: async_sessionmaker | None = None

    def init_db(self, db_url: MultiHostUrl, debug: bool) -> None:
        self._engine = create_async_engine(
            str(db_url),
            echo=debug,
            pool_size=10,
            max_overflow=2,
            pool_recycle=300,
            pool_pre_ping=True,
            pool_use_lifo=True,
        )
        self._session_maker = async_sessionmaker(
            bind=self._engine,
            expire_on_commit=False,
        )

    @property
    def engine(self) -> AsyncEngine:
        return self._engine

    @asynccontextmanager
    async def get_session(self) -> AsyncSession:
        session = self._session_maker()
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

    @asynccontextmanager
    async def get_connection(self) -> AsyncConnection:
        async with self._engine.connect() as connection:
            try:
                yield connection
            except Exception:
                await connection.close()
                raise

    async def disconnect_from_db(self) -> None:
        await self._engine.dispose()


db_manager = DatabaseManager()


async def get_connection() -> AsyncConnection:
    async with db_manager.get_connection() as connection:
        yield connection


async def get_db_session() -> AsyncSession:
    async with db_manager.get_session() as session:
        yield session

def execute_all(sql, connect=get_connection()):
    execute = connect.execute(sql)
    connect.commit()
    return execute