import os
from dotenv import load_dotenv

from dao.twitch_dao import TwitchGameDAO, TwitchStreamDAO
from parsers.utils import fetch_data

load_dotenv()


async def parse_twitch_games():
    url = os.getenv('TWITCH_GAMES_URL')
    params = {
        'first': 100,
    }
    twitch_games_dao = TwitchGameDAO(os.getenv('DB_URI'), os.getenv('DB_NAME'))
    await fetch_data(url, params, twitch_games_dao)


async def parse_twitch_streams():
    url = os.getenv('TWITCH_STREAMS_URL')
    params = {
        'first': 100,
    }
    twitch_streams_dao = TwitchStreamDAO(os.getenv('DB_URI'), os.getenv('DB_NAME'))
    await fetch_data(url, params, twitch_streams_dao)
