from .domain import Film, Planet, PlanetList

yavin_dict = dict(
    name='Yavin IV',
    climate='temperate, tropical',
    diameter='10200',
    population='1000',
    films=[Film(title='A New Hope', release_date='1977-05-25')],
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

list_planets = [yavin_dict, alderaan_dict]


async def search_planet_db(search: str = None):
    if search is None:
        return PlanetList(result=list_planets)
    if search != 'yavin':
        return None
    return PlanetList(result=[Planet(**yavin_dict)])
