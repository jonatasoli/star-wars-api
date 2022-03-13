import pytest

from src.domain import APINotFoundData, DBNotFoundData, PlanetNotFound
from src.services import Search

from .api_test_data import list_alderaan, list_planets, list_yavin


@pytest.mark.asyncio
async def test_list_planets(mocker):
    mocker.patch(
        'src.adapters.adapter_db.search_planet_db', return_value=list_planets
    )
    mocker.patch('src.adapters.adapter_db.save_planet')
    service = Search()
    assert (
        await service.search_planet(search=None, engine=None) == list_planets
    )


@pytest.mark.asyncio
async def test_empty_search(mocker):
    mocker.patch(
        'src.adapters.adapter_db.search_planet_db',
        return_value=dict(result=[]),
    )
    mocker.patch('src.adapters.adapter_db.save_planet')
    service = Search()
    assert await service.search_planet(search='', engine=None) == dict(
        result=[]
    )


@pytest.mark.asyncio
async def test_invalid_planet(mocker):
    mocker.patch(
        'src.adapters.adapter_db.search_planet_db', side_effect=DBNotFoundData
    )
    mocker.patch(
        'src.adapters.adapter_api.search_api', side_effect=APINotFoundData
    )
    mocker.patch('src.adapters.adapter_db.save_planet')
    service = Search()
    with pytest.raises(PlanetNotFound):
        await service.search_planet(search='invalid', engine=None)


@pytest.mark.asyncio
async def test_return_planet_yavin_iv_in_db_function(mocker):
    mocker.patch(
        'src.adapters.adapter_db.search_planet_db', return_value=list_yavin
    )
    mocker.patch('src.adapters.adapter_db.save_planet')
    service = Search()
    assert (
        await service.search_planet(search='yavin', engine=None) == list_yavin
    )


@pytest.mark.asyncio
async def test_return_planet_alderaan_in_api_function(mocker):
    mocker.patch(
        'src.adapters.adapter_db.search_planet_db', side_effect=DBNotFoundData
    )
    mocker.patch(
        'src.adapters.adapter_api.search_api', return_value=list_alderaan
    )
    mocker.patch('src.adapters.adapter_db.save_planet')
    service = Search()
    assert (
        await service.search_planet(search='alderaan', engine=None)
        == list_alderaan
    )
