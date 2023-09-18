import os
import aiohttp
from typing import Awaitable
from dotenv import load_dotenv

from src.dao.base_dao import BaseDAO

load_dotenv()


async def get_access_token_from_twitch(client_id: str, client_secret: str, grant_type: str) -> Awaitable[str]:
    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': grant_type,
    }

    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        async with session.post(os.getenv('TWITCH_TOKEN_URL'), data=data) as response:
            response_data = await response.json()
            return response_data['access_token']


async def fetch_data(url: str, params: dict, dao_instance: BaseDAO):
    api_key = await get_access_token_from_twitch(
        os.getenv('TWITCH_CLIENT_ID'),
        os.getenv('TWITCH_CLIENT_SECRET'),
        os.getenv('TWITCH_GRANT_TYPE')
    )
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Client-Id': os.getenv('TWITCH_CLIENT_ID'),
    }

    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        async with session.get(url, headers=headers, params=params) as response:
            response_data = await response.json()
            dao_instance.create_or_update(response_data['data'])
