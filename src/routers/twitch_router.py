import os
from fastapi import APIRouter, Depends
from fastapi_cache.decorator import cache

from src.config.database import Database
from src.config.dependencies import get_database
from src.dao.twitch_dao import TwitchGameDAO, TwitchStreamDAO
from src.exceptions.custom_exception import CustomExceptionHandler
from src.producer.producer import send_message

router = APIRouter()


@router.post('/games/', status_code=201)
async def create_twitch_games(database: Database = Depends(get_database)):
    await send_message('twitch_parser', os.getenv('TWITCH_GAMES_URL'), 'games')
    return {"message": "Games Parsing request sent to Kafka"}


@router.post('/streams/', status_code=201)
async def create_twitch_streams(database: Database = Depends(get_database)):
    await send_message('twitch_parser', os.getenv('TWITCH_STREAMS_URL'), 'streams')
    return {"message": "Streams Parsing request sent to Kafka"}


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
