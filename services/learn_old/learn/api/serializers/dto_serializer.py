from typing import Type

from pydantic import BaseModel


class DtoSerializer:
    @staticmethod
    def from_json(data, DtoClass: Type[BaseModel]):
        return DtoClass(**data)

    @staticmethod
    def to_dict(data, many=False):
        if many:
            return list(map(lambda x: x.dict(), data))
        return data.dict()
