import re
from typing import List

from loguru import logger
from odmantic import Model

from .domain import DBNotFoundData, Planet, PlanetList


class Planet(Model):
    name: str
    climate: str
    diameter: str
    population: str
    films: List


async def search_planet_db(search: str = None, engine=None):
    if search is None:
        planets = await engine.find(Planet)
        return PlanetList(result=planets)
    planet = await engine.find_one(
        Planet, Planet.name.match(re.compile(search, re.IGNORECASE))
    )
    if not planet:
        raise DBNotFoundData(f'The planet {search} not found in db')
    return PlanetList(result=[planet])


async def save_planet(planet, engine):
    try:
        _planet = Planet(**planet.result[0].dict())
        await engine.save(_planet)
    except Exception as e:
        logger.error(e)
        raise e
