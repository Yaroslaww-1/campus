from datetime import datetime

from pydantic import BaseModel

from learn.application.users.dtos.user_dto import UserDto


class PostDto(BaseModel):
    id: str
    name: str
    content: str
    created_at: datetime
    created_by: UserDto
