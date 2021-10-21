import os
from typing import Type

from django.core.files.storage import default_storage
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

    @staticmethod
    def upload_replace_files(data, files):
        AWS_BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')
        AWS_REGION_NAME = os.getenv('AWS_REGION_NAME')
        for key, file in files.items():
            file_name = default_storage.save("media/" + data["id"] + "/" + file.name, file)
            file_url = "https://s3-{0}.amazonaws.com/{1}/{2}".format(
                AWS_REGION_NAME,
                AWS_BUCKET_NAME,
                file_name
            )
            data[key] = file_url
