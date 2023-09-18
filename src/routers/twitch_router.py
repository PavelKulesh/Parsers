from fastapi import APIRouter, Depends
from fastapi_cache.decorator import cache

from src.parsers.twitch_parsers import parse_twitch_games, parse_twitch_streams
from src.config.database import Database
from src.config.dependencies import get_database
from src.dao.twitch_dao import TwitchGameDAO, TwitchStreamDAO
from src.exceptions.custom_exception import CustomExceptionHandler

router = APIRouter()


@router.post('/games/', status_code=201)
async def create_twitch_games(database: Database = Depends(get_database)):
    try:
        await parse_twitch_games(database)
        return {"message": "Games created successfully"}
    except Exception as e:
        raise CustomExceptionHandler(detail="Game Parsing Error", status_code=500)


@router.post('/streams/', status_code=201)
async def create_twitch_streams(database: Database = Depends(get_database)):
    try:
        await parse_twitch_streams(database)
        return {"message": "Streams created successfully"}
    except Exception as e:
        raise CustomExceptionHandler(detail="Stream Parsing Error", status_code=500)


@router.get('/games/')
@cache(expire=60)
async def read_twitch_games(database: Database = Depends(get_database), count: int = 10):
    try:
        twitch_game_dao = TwitchGameDAO(database)
        return twitch_game_dao.read(count, 1)
    except Exception as e:
        raise CustomExceptionHandler(detail='Something went wrong', status_code=500)


@router.get('/streams/')
@cache(expire=60)
async def read_twitch_streams(database: Database = Depends(get_database), count: int = 10):
    try:
        twitch_stream_dao = TwitchStreamDAO(database)
        return twitch_stream_dao.read(count)
    except Exception as e:
        raise CustomExceptionHandler(detail='Something went wrong', status_code=500)
