import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.db.base import db_manager

from src.config import settings
from src.routers.order import order_view
from src.routers.order_details import order_details_view
from src.routers.utils import time_view
def init_app() -> FastAPI:
    db_manager.init_db(db_url=settings.postgresql_url, debug=settings.debug)
    print(f'settings.postgresql_url: {settings. postgresql_url}')
    application = FastAPI(
        docs_url=f'{settings.api_prefix}/docs',
        openapi_url=f'{settings.api_prefix}/openapi.json',
        redoc_url=f'{settings.api_prefix}/redoc'
    )
    application.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    application.include_router(order_view, prefix=settings.api_prefix)
    application.include_router(order_details_view, prefix=settings.api_prefix)
    application.include_router(time_view, prefix=settings.api_prefix)
    
    return application

app = init_app()

if __name__ == '__main__':
    uvicorn.run(
        'src.main:app',
        host='0.0.0.0',
        port=8009,
        reload=settings.debug,
        log_level=settings.logger_settings.log_level.lower(),
    )
