import contextlib
from fastapi import FastAPI, Depends, HTTPException, status
from loguru import logger

from .adapter_api import search_api
from .adapter_db import search_planet_db, save_planet
from .domain import APINotFoundData, PlanetList, PlanetNotFound, DBNotFoundData
from odmantic import AIOEngine
from motor.motor_asyncio import AsyncIOMotorClient
from src.config import settings

app = FastAPI()

client = AsyncIOMotorClient(settings.MONGOURL)
engine = AIOEngine(motor_client=client, database=settings.DATABASE)

class Search():
    async def search_planet(self, search, engine):
        try:
            planet = None
            with contextlib.suppress(DBNotFoundData):
                planet = await search_planet_db(search, engine)
            if planet:
                return planet
            planet = await search_api(search)
            if not planet:
                raise PlanetNotFound(f'Planet {search} not found')
            # await save_planet(planet, engine)
            return planet
        except APINotFoundData:
            raise PlanetNotFound('Planet not found')
        except Exception as e:
            raise e

@app.get('/planets', status_code=status.HTTP_200_OK, response_model=PlanetList)
async def get_planets(
        service: Search = Depends(),
        search: str = None
    ):
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
