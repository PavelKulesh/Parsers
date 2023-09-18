from datetime import datetime
from typing import List, Type

from src.dao.validators import get_validated_data
from src.schemas.base_schema import BaseSchema
from src.config.database import Database


class BaseDAO:
    def __init__(self, database: Database, collection_name: str, schema_class: Type[BaseSchema]):
        self.collection = database.db[collection_name]
        self.schema = schema_class

    def create_or_update(self, data: List[dict]) -> List[dict]:
        try:
            validated_data = get_validated_data(self.schema, data)
            for item in validated_data:
                existing_item = self.collection.find_one({'id': item['id']})
                if existing_item:
                    item['_id'] = existing_item['_id']
                    item['created_at'] = existing_item['created_at']
                    item['updated_at'] = existing_item['updated_at']
                    if existing_item != item:
                        item['updated_at'] = datetime.now()
                        self.collection.update_one({'_id': item['_id']}, {'$set': item})
                else:
                    self.collection.insert_one(item)
            return validated_data
        except Exception as e:
            print(f'Error: {e}')

    def read(self, count: int = 1, sorting_key: int = -1) -> List[dict]:
        cursor = self.collection.find().sort('updated_at', sorting_key).limit(count)
        items = []
        for item in cursor:
            del item['_id']
            items.append(item)
        return items
