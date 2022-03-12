from typing import Optional

from fastapi import FastAPI, HTTPException, status
from loguru import logger

from .adapter_api import search_api
from .adapter_db import search_planet_db
from .domain import PlanetList

app = FastAPI()


@app.get('/planets', status_code=status.HTTP_200_OK, response_model=PlanetList)
def get_planets(search: str = None):
    try:
        return search_planet(search)
    except PlanetNotFound as e:
        logger.error(f'Error return endpoint {e}')
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Error to proccess this request.\n{e}',
        )
    except Exception as e:
        logger.error(f'Error to process function get_planets {e}')
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERRROR,
            detail='This request finish unexpectedly.',
        )


def search_planet(search: str):
    planet = search_planet_db(search)
    if planet:
        return planet
    planet = search_api(search)
    if not planet:
        raise PlanetNotFound(f'Planet {search} not found')
    return planet


class PlanetNotFound(Exception):
    pass
