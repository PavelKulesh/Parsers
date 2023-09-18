from fastapi import APIRouter, Depends
from fastapi_cache.decorator import cache

from src.parsers.lamoda_parsers import parse_lamoda_items
from src.config.database import Database
from src.config.dependencies import get_database
from src.dao.lamoda_dao import LamodaItemDAO
from src.exceptions.custom_exception import CustomExceptionHandler

router = APIRouter()


@router.post('/items/', status_code=201)
async def create_lamoda_items(url: str = 'https://www.lamoda.ru/c/1386/shoes-premium-men-obuv/', pages: int = 1,
                              database: Database = Depends(get_database)):
    try:
        for page in range(1, pages + 1):
            await parse_lamoda_items(database, url, page)
        return {"message": "Lamoda Items created successfully"}
    except Exception as e:
        raise CustomExceptionHandler(detail='Lamoda url is incorrect', status_code=400)


@router.get('/items/')
@cache(expire=60)
async def read_lamoda_items(database: Database = Depends(get_database), count: int = 10):
    try:
        lamoda_item_dao = LamodaItemDAO(database)
        return lamoda_item_dao.read(count)
    except Exception as e:
        raise CustomExceptionHandler(detail='Something went wrong', status_code=500)
