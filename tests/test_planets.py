import pytest
from fastapi import status
from fastapi.testclient import TestClient
from src.adapter_api import search_api
from src.domain import APINotFoundData

from .api_test_data import list_alderaan, list_planets, list_yavin, list_hoth

def test_status_code_planet_endpoint(client, mocker):
    mocker.patch(
        "src.adapter_db.search_planet_db",
        return_value = list_planets
    )
    response = client.get('/planets')
    assert response.status_code == status.HTTP_200_OK


def test_invalid_planet(client, mocker):
    """Must return 404 error"""
    mocker.patch(
        "src.adapter_db.search_planet_db",
        return_value = None
    )
    mocker.patch(
        "src.adapter_api.search_api",
        side_effect = APINotFoundData
    )
    response = client.get('/planets/?search=invalid')
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_list_planets(client, mocker):
    mocker.patch(
        "src.adapter_db.search_planet_db",
        return_value = list_planets
    )
    response = client.get('/planets')
    assert response.json() == list_planets


def test_return_planet_yavin_iv(client, mocker):
    mocker.patch(
        "src.adapter_db.search_planet_db",
        return_value = None
    )
    mocker.patch(
        "src.adapter_api.search_api",
        return_value = list_yavin
    )
    response = client.get('/planets/?search=yavin')
    assert response.json() == list_yavin


def test_return_planet_alderaan(client, mocker):
    mocker.patch(
        "src.adapter_db.search_planet_db",
        return_value = None
    )
    mocker.patch(
        "src.adapter_api.search_api",
        return_value = list_alderaan
    )
    response = client.get('/planets/?search=alderaan')
    assert response.json() == list_alderaan
