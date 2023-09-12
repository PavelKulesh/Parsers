from pymongo import MongoClient
from datetime import datetime
from typing import List, Type

from dao.validators import get_validated_data
from schemas.base_schema import BaseSchema


class BaseDAO:
    def __init__(self, db_uri: str, db_name: str, collection_name: str, schema_class: Type[BaseSchema]):
        self.client = MongoClient(db_uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]
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
            items.append(item)
        return items
