import os
from dotenv import load_dotenv

from src.dao.twitch_dao import TwitchGameDAO, TwitchStreamDAO
from src.parsers.utils import fetch_data
from src.config.database import Database

load_dotenv()


async def parse_twitch_games(database: Database):
    url = os.getenv('TWITCH_GAMES_URL')
    params = {
        'first': 100,
    }
    twitch_games_dao = TwitchGameDAO(database)
    await fetch_data(url, params, twitch_games_dao)


async def parse_twitch_streams(database: Database):
    url = os.getenv('TWITCH_STREAMS_URL')
    params = {
        'first': 100,
    }
    twitch_streams_dao = TwitchStreamDAO(database)
    await fetch_data(url, params, twitch_streams_dao)
