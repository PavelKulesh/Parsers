from datetime import datetime
from typing import Union

from src.schemas.base_schema import BaseSchema


class TwitchGame(BaseSchema):
    id: str
    name: str
    created_at: datetime = None
    updated_at: datetime = None


class TwitchStream(BaseSchema):
    id: str
    user_id: str
    user_login: str
    user_name: str
    game_id: str
    game_name: str
    type: str
    title: str
    viewer_count: int
    started_at: str
    language: str
    tag_ids: Union[list[str], None]
    tags: Union[list[str], None]
    is_mature: bool
    created_at: datetime = None
    updated_at: datetime = None
