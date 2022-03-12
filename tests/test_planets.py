import pytest
from fastapi import status
from fastapi.testclient import TestClient

from .api_test_data import list_alderaan, list_planets, list_yavin, list_hoth

@pytest.mark.skip
def test_status_code_planet_endpoint(client):
    response = client.get('/planets')
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.skip
def test_invalid_planet(client):
    """Must return 404 error"""
    response = client.get('/planets/?search=invalid')
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.skip
def test_list_planets(client):
    response = client.get('/planets')
    assert response.json() == list_planets


@pytest.mark.skip
def test_return_planet_yavin_iv(client):
    response = client.get('/planets/?search=yavin')
    assert response.json() == list_yavin


@pytest.mark.skip
def test_return_planet_alderaan(client):
    response = client.get('/planets/?search=alderaan')
    assert response.json() == list_alderaan


def test_return_planet_hoth(client):
    response = client.get('/planets/?search=hoth')
    assert response.json() == list_hoth
