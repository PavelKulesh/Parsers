from fastapi import APIRouter, Depends, HTTPException

from src.parsers.lamoda_parsers import parse_lamoda_items
from src.config.database import Database
from src.config.dependencies import get_database
from src.dao.lamoda_dao import LamodaItemDAO

router = APIRouter()


@router.post('/items/', status_code=201)
async def create_lamoda_items(url: str = 'https://www.lamoda.ru/c/1386/shoes-premium-men-obuv/', pages: int = 1,
                              database: Database = Depends(get_database)):
    try:
        for page in range(1, pages + 1):
            await parse_lamoda_items(database, url, page)
        return {"message": "Lamoda Items created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get('/items/')
async def read_lamoda_items(database: Database = Depends(get_database), count: int = 10):
    lamoda_item_dao = LamodaItemDAO(database)
    return lamoda_item_dao.read(count)
