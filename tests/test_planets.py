import pytest
from fastapi.testclient import TestClient

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


def test_status_code_planet_endpoint(client):
    response = client.get('/planets')
    assert response.status_code == 200


def test_list_planets(client):
    response = client.get('/planets')
    assert response.json() == list_planets


def test_return_planet_yavin_iv(client):
    response = client.get('/planets/?search=yavin')
    assert response.json() == yavin_dict
