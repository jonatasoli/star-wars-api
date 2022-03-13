from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from src.config import settings

from .resources import planet_router


def create_app():
    app = FastAPI()
    origins = [
        'localhost',
    ]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )
    app.include_router(
        planet_router,
        responses={status.HTTP_404_NOT_FOUND: {'description': 'Not found'}},
    )
    return app
