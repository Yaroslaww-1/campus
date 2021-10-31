from pydantic import BaseModel


class PostDto(BaseModel):
    id: str
    name: str
