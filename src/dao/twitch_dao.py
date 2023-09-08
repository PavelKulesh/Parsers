from pymongo import MongoClient
from typing import List

from schemas.twitch_schemas import TwitchGame, TwitchStream
from dao.validators import get_validated_data
from dao.base_dao import BaseDAO


class TwitchGameDAO:
    def __init__(self, db_uri: str, db_name: str):
        self.client = MongoClient(db_uri)
        self.db = self.client[db_name]
        self.collection = self.db['twitch_games']

    def create_games(self, data: List[dict]) -> List[dict]:
        try:
            validated_data = get_validated_data(TwitchGame, data)
            self.collection.insert_many(validated_data)
            return validated_data
        except Exception as e:
            print(f'Error: {e}')

    def read_games(self, count: int = 1) -> List[dict]:
        cursor = self.collection.find().limit(count)
        games = []
        for game in cursor:
            games.append(game)
        return games


class TwitchStreamDAO(BaseDAO):
    def __init__(self, db_uri: str, db_name: str):
        super().__init__(db_uri, db_name, 'twitch_streams', TwitchStream)
