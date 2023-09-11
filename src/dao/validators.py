from pydantic import ValidationError
from typing import Type, List

from schemas.base_schema import BaseSchema


def get_validated_data(schema_class: Type[BaseSchema], response_data: List[dict]) -> List[dict]:
    validated_data = []

    for obj in response_data:
        try:
            valid_obj = schema_class(**obj)
            validated_data.append(valid_obj.model_dump())
        except ValidationError as e:
            print(f'Invalid data: {e}')

    if not validated_data:
        raise Exception('Invalid data: no valid data')

    return validated_data
