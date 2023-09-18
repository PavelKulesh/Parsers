from src.schemas.twitch_schemas import TwitchGame, TwitchStream
from src.dao.base_dao import BaseDAO
from src.config.database import Database


class TwitchGameDAO(BaseDAO):
    def __init__(self, database: Database):
        super().__init__(database, 'twitch_games', TwitchGame)


class TwitchStreamDAO(BaseDAO):
    def __init__(self, database: Database):
        super().__init__(database, 'twitch_streams', TwitchStream)
