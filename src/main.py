from typing import Optional

from fastapi import FastAPI

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

@app.get('/planets')
def get_planets(search: str = None):
    if search:
        return search_planet(search)
    return list_all_planets()


def search_planet(search: str):
    return yavin_dict

def list_all_planets():
    return list_planets
