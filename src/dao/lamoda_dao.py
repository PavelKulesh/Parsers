from src.schemas.lamoda_schemas import LamodaItem
from src.dao.base_dao import BaseDAO
from src.config.database import Database


class LamodaItemDAO(BaseDAO):
    def __init__(self, database: Database):
        super().__init__(database, 'lamoda_items', LamodaItem)
