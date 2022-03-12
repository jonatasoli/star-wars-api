from .domain import Film, Planet, PlanetList

alderaan_dict = dict(
    name='Alderaan',
    climate='temperate',
    diameter=12500,
    population=2000000000,
    films=[
        Film(title='A New Hope', release_date='1977-05-25'),
        Film(title='Revenge of the Sith', release_date='2005-05-19'),
    ],
)


def search_api(search: str):
    if search != 'alderaan':
        return None
    return PlanetList(result=[Planet(**alderaan_dict)])
