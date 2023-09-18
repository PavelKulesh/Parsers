from pymongo import MongoClient

from src.config.settings import Settings


class Database:
    _instance = None

    def __new__(cls, settings: Settings):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance.client = MongoClient(settings.db_uri)
            cls._instance.db = cls._instance.client[settings.db_name]
        return cls._instance
