from schemas.twitch_schemas import TwitchGame, TwitchStream
from dao.base_dao import BaseDAO


class TwitchGameDAO(BaseDAO):
    def __init__(self, db_uri: str, db_name: str):
        super().__init__(db_uri, db_name, 'twitch_games', TwitchGame)


class TwitchStreamDAO(BaseDAO):
    def __init__(self, db_uri: str, db_name: str):
        super().__init__(db_uri, db_name, 'twitch_streams', TwitchStream)
