from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_uri: str
    db_name: str = 'parsers_db'

    class Config:
        env_file = '../../.env'
