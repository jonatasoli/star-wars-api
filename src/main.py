from typing import Optional

from fastapi import FastAPI, status, HTTPException
from loguru import logger

from .adapter_db import search_planet_db
from .adapter_api import search_api

app = FastAPI()

yavin_dict = dict(
name='Yavin IV',
    climate='temperate, tropical',
    diameter='10200',
    population='1000',
    films=[dict(title='A New Hope', release_date='1977-05-25')],
)
alderaan_dict = dict(
    name='Alderaan',
    climate='temperate',
    diameter='12500',
    population='2000000000',
    films=[
        dict(title='A New Hope', release_date='1977-05-25'),
        dict(title='Revenge of the Sith', release_date='2005-05-19'),
    ],
)

list_planets = [yavin_dict, alderaan_dict]

@app.get('/planets', status_code=status.HTTP_200_OK)
def get_planets(
        search: str = None
    ):
    try:
        return search_planet(search)
    except PlanetNotFound as e:
        logger.error(f"Error return endpoint {e}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Error to proccess this request.\n{e}"
        )
    except Exception as e:
        logger.error(
            f"Error to process function get_planets {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERRROR,
            detail="This request finish unexpectedly."
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
