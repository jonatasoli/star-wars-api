import pytest

from src.adapter_api import search_api
from src.domain import APINotFoundData

from .api_test_data import list_hoth


@pytest.mark.api
@pytest.mark.asyncio
async def test_return_api_error():
    with pytest.raises(APINotFoundData):
        await search_api('invalid')


@pytest.mark.api
@pytest.mark.asyncio
async def test_return_planet_hoth():
    output = await search_api('hoth')
    assert output == list_hoth
