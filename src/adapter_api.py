import httpx
from .domain import (
    Film,
    Planet,
    PlanetList,
    PlanetList,
    APINotFoundData
)
alderaan_dict = dict(
    name='Alderaan',
    climate='temperate',
    diameter='12500',
    population='2000000000',
    films=[
        Film(title='A New Hope', release_date='1977-05-25'),
        Film(title='Revenge of the Sith', release_date='2005-05-19'),
    ],
)
api_url = 'https://swapi.dev/api'

def search_api(search: str):
    try:
        film_list = []
        planet = httpx.get(
            f'{api_url}/planets/?search={search}'
        ).json().get('results')
        if not planet:
            return None
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
                    films=film_list
                )
            ]
        )
    except KeyError:
        raise APINotFoundData
    except Exception as e:
        raise e
