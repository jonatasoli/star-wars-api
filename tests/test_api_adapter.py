import pytest

from src.adapter_api import search_api
from src.domain import APINotFoundData

from .api_test_data import list_hoth


@pytest.mark.api
@pytest.mark.asyncio
async def test_return_api_error():
    async with pytest.raises(APINotFoundData):
        await search_api('invalid')


@pytest.mark.api
@pytest.mark.asyncio
async def test_return_planet_hoth(client):
    response = await client.get('/planets/?search=hoth')
    assert response.json() == list_hoth
