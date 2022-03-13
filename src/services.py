import contextlib

from loguru import logger

from src.adapters import adapter_api, adapter_db

from .domain import APINotFoundData, DBNotFoundData, PlanetNotFound


class Search:
    async def search_planet(self, search, engine):
        try:
            planet = None
            with contextlib.suppress(DBNotFoundData):
                planet = await adapter_db.search_planet_db(search, engine)
            if planet:
                return planet
            planet = await adapter_api.search_api(search)
            if not planet:
                raise PlanetNotFound(f'Planet {search} not found')
            await adapter_db.save_planet(planet, engine)
            return planet
        except APINotFoundData as err:
            raise PlanetNotFound('Planet not found') from err
        except Exception as e:
            logger.error(e)
            raise e
