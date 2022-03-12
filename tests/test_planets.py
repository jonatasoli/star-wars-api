import pytest
from fastapi.testclient import TestClient
from fastapi import status
from .api_test_data import (
    list_planets,
    yavin_dict,
    alderaan_dict
)


def test_status_code_planet_endpoint(client):
    response = client.get('/planets')
    assert response.status_code == status.HTTP_200_OK

def test_invalid_planet(client):
    """Must return 404 error"""
    response = client.get('/planets/?search=invalid')
    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_list_planets(client):
    response = client.get('/planets')
    assert response.json() == list_planets


def test_return_planet_yavin_iv(client):
    response = client.get('/planets/?search=yavin')
    assert response.json() == yavin_dict


def test_return_planet_alderaan(client):
    response = client.get('/planets/?search=alderaan')
    assert response.json() == alderaan_dict


