import pytest
from src.adapter_api import search_api
from src.domain import APINotFoundData

from .api_test_data import list_hoth

@pytest.mark.api
def test_return_api_error():
    with pytest.raises(APINotFoundData):
        search_api('invalid')

@pytest.mark.api
def test_return_planet_hoth(client):
    response = client.get('/planets/?search=hoth')
    assert response.json() == list_hoth
