from fastapi import APIRouter, Depends
from fastapi_cache.decorator import cache

from src.config.database import Database
from src.config.dependencies import get_database
from src.dao.lamoda_dao import LamodaItemDAO
from src.exceptions.custom_exception import CustomExceptionHandler
from src.producer.producer import send_message

router = APIRouter()


@router.post('/items/', status_code=201)
async def create_lamoda_items(url: str = 'https://www.lamoda.ru/c/1386/shoes-premium-men-obuv/', pages: int = 1,
                              database: Database = Depends(get_database)):
    await send_message('lamoda_parser', {'url': url, 'pages': pages}, 'items')
    return {"message": "Lamoda Items Parsing request sent to Kafka"}


@router.get('/items/')
@cache(expire=60)
async def read_lamoda_items(database: Database = Depends(get_database), count: int = 10):
    try:
        lamoda_item_dao = LamodaItemDAO(database)
        return lamoda_item_dao.read(count)
    except Exception as e:
        raise CustomExceptionHandler(detail='Something went wrong', status_code=500)
