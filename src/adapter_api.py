import httpx

from src.config import settings

from .domain import APINotFoundData, Film, Planet, PlanetList


async def search_api(search: str):
    try:
        film_list = []
        planet = None
        async with httpx.AsyncClient() as client:
            planet = await client.get(
                f'{settings.API_URL}/planets/?search={search}'
            )
            planet = planet.json().get('results')[0]
            for film in planet['films']:
                film = await client.get(film)
                film_list.append(Film(**film.json()))

        return PlanetList(
            result=[
                Planet(
                    name=planet['name'],
                    climate=planet['climate'],
                    diameter=planet['diameter'],
                    population=planet['population'],
                    films=film_list,
                )
            ]
        )
    except (KeyError, IndexError):
        raise APINotFoundData
    except Exception as e:
        raise e
