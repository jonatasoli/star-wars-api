import httpx

from .domain import APINotFoundData, Film, Planet, PlanetList
from src.config import settings


def search_api(search: str):
    try:
        film_list = []
        planet = (
            httpx.get(f'{settings.API_URL}/planets/?search={search}')
            .json()
            .get('results')
        )
        planet = planet[0]
        for film in planet['films']:
            film = httpx.get(film).json()
            film_list.append(Film(**film))

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
