from fastapi import Depends

from src.config.settings import Settings
from src.config.database import Database


def get_settings() -> Settings:
    return Settings()


def get_database(settings: Settings = Depends(get_settings)) -> Database:
    return Database(settings)
