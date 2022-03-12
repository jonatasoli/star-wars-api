from fastapi import FastAPI, HTTPException, status
from loguru import logger

from .adapter_api import search_api
from .adapter_db import search_planet_db
from .domain import APINotFoundData, PlanetList, PlanetNotFound

app = FastAPI()


@app.get('/planets', status_code=status.HTTP_200_OK, response_model=PlanetList)
async def get_planets(search: str = None):
    try:
        return await search_planet(search)
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


async def search_planet(search: str):
    try:
        planet = await search_planet_db(search)
        if planet:
            return planet
        planet = await search_api(search)
        if not planet:
            raise PlanetNotFound(f'Planet {search} not found')
        return planet
    except APINotFoundData:
        raise PlanetNotFound('Planet not found')
    except Exception as e:
        raise e
