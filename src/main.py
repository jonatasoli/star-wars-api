from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get('/planets')
def get_planets(search: str = None):
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
    if search:
        return yavin_dict
    return list_planets
