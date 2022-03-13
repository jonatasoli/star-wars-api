import contextlib

from .adapter_api import search_api
from .adapter_db import save_planet, search_planet_db
from .domain import APINotFoundData, DBNotFoundData, PlanetNotFound


class Search:
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
