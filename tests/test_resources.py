from fastapi import status

from src.domain import PlanetNotFound

from .api_test_data import list_alderaan, list_planets, list_yavin


def test_status_code_planet_endpoint(client, mocker):
    mocker.patch(
        'src.services.Search.search_planet', return_value=list_planets
    )
    response = client.get('/planets')
    assert response.status_code == status.HTTP_200_OK


def test_list_planets(client, mocker):
    mocker.patch(
        'src.services.Search.search_planet', return_value=list_planets
    )
    response = client.get('/planets')
    assert response.json() == list_planets


def test_invalid_planet(client, mocker):
    """Must return 404 error"""
    mocker.patch(
        'src.services.Search.search_planet', side_effect=PlanetNotFound
    )
    response = client.get('/planets/?search=invalid')
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_return_planet_yavin_iv(client, mocker):
    mocker.patch('src.services.Search.search_planet', return_value=list_yavin)
    response = client.get('/planets/?search=yavin')
    assert response.json() == list_yavin


def test_return_planet_alderaan(client, mocker):
    mocker.patch(
        'src.services.Search.search_planet', return_value=list_alderaan
    )
    response = client.get('/planets/?search=alderaan')
    assert response.json() == list_alderaan
