from pydantic import BaseModel

from learn.application.groups.dtos.group_dto import GroupDto
from learn.application.users.dtos.user_dto import UserDto


class StudentDto(BaseModel):
    user: UserDto
    group: GroupDto
