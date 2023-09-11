from schemas.lamoda_schemas import LamodaItem
from dao.base_dao import BaseDAO


class LamodaItemDAO(BaseDAO):
    def __init__(self, db_uri: str, db_name: str):
        super().__init__(db_uri, db_name, 'lamoda_items', LamodaItem)
