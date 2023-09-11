from datetime import datetime
from .base_schema import BaseSchema


class LamodaItem(BaseSchema):
    id: str
    brand: str
    title: str
    category: str
    price: str
    currency: str
    created_at: datetime = None
    updated_at: datetime = None
