import pytest
from unittest.mock import Mock, patch
from aioresponses import aioresponses

from tests.conftest import database, twitch_stream_dao, valid_stream_data, lamoda_item_dao, response_body
from src.parsers.twitch_parsers import parse_twitch_streams
from src.parsers.lamoda_parsers import parse_lamoda_items


@pytest.mark.asyncio
async def test_parse_twitch_streams(database, twitch_stream_dao):
    async def mock_fetch_data(url, params, dao_instance):
        response_data = {
            'data': valid_stream_data
        }
        mock_response = Mock()
        mock_response.json.return_value = response_data
        dao_instance.create_or_update(response_data['data'])

    with patch('src.parsers.twitch_parsers.fetch_data', side_effect=mock_fetch_data):
        await parse_twitch_streams(database)
        count = twitch_stream_dao.collection.count_documents({})

        assert count == 5


@pytest.mark.asyncio
async def test_parse_lamoda_items(database, lamoda_item_dao):
    with aioresponses() as mocked:
        mocked.get('https://www.lamoda.ru/c/1386/shoes-premium-men-obuv/?page=1', body=response_body)
        await parse_lamoda_items(database, url='https://www.lamoda.ru/c/1386/shoes-premium-men-obuv/', page=1)

    count = lamoda_item_dao.collection.count_documents({})
    assert count == 2
