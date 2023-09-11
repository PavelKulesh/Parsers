from pydantic import BaseModel
from datetime import datetime


class BaseSchema(BaseModel):
    def __init__(self, **data):
        super().__init__(**data)
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
