import pytest
from fastapi.testclient import TestClient
from .api_test_data import list_planets, yavin_dict


def test_status_code_planet_endpoint(client):
    response = client.get('/planets')
    assert response.status_code == 200


def test_list_planets(client):
    response = client.get('/planets')
    assert response.json() == list_planets


def test_return_planet_yavin_iv(client):
    response = client.get('/planets/?search=yavin')
    assert response.json() == yavin_dict
