import inject
from pydantic import BaseModel, StrictStr, StrictInt

from learn.application.groups.dtos.group_dto import GroupDto
from learn.application.groups.group_mapper import GroupMapper
from learn.domain.groups.entities.group import Group
from learn.infrastructure.repositories.group_repository import GroupRepository


class CreateGroupCommandDto(BaseModel):
    name: StrictStr
    formed_at_year: StrictInt


class CreateGroupCommand:
    @inject.autoparams()
    def __init__(self, group_repository: GroupRepository):
        self.group_repository = group_repository

    def execute(self, dto: CreateGroupCommandDto) -> GroupDto:
        group = Group.create_new_group(name=dto.name, formed_at_year=dto.formed_at_year)
        self.group_repository.save_group(group)
        return GroupMapper.to_dto(group)
