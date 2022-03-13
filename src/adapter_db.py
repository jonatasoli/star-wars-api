from typing import List

from odmantic import AIOEngine, Model, ObjectId

from .domain import DBNotFoundData, Film, Planet, PlanetList


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
    planet = await engine.find_one(Planet, Planet.name.match(rf'{search}'))
    if not planet:
        raise DBNotFoundData(f'The planet {search} not found in db')
    return PlanetList(result=[planet])


async def save_planet(planet, engine):
    try:
        await engine.save(planet)
    except Exception as e:
        raise e
