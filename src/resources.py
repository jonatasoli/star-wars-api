from fastapi import APIRouter, Depends, HTTPException, status
from loguru import logger
from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine

from src.config import settings

from .domain import PlanetList, PlanetNotFound
from .services import Search


client = AsyncIOMotorClient(settings.MONGOURL)
engine = AIOEngine(motor_client=client, database=settings.DATABASE)
planet_router = APIRouter()


@planet_router.get('/planets', status_code=status.HTTP_200_OK, response_model=PlanetList)
async def get_planets(service: Search = Depends(), search: str = None):
    try:
        return await service.search_planet(search, engine)
    except PlanetNotFound as e:
        logger.error(f'Error return endpoint {e}')
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Error to proccess this request.\n{e}',
        )
    except Exception as e:
        logger.error(f'Error to process function get_planets {e}')
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='This request finish unexpectedly.',
        )
