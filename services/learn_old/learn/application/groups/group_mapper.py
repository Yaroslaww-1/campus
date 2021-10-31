from typing import List

from learn.application.groups.dtos.group_dto import GroupDto
from learn.domain.groups.entities.group import Group


class GroupMapper:
    @staticmethod
    def to_dto(entity: Group) -> GroupDto:
        return GroupDto(
            id=entity.id.value,
            name=entity.name,
            formed_at_year=entity.formed_at_year.value
        )

    @staticmethod
    def to_dtos(entities: List[Group]) -> List[GroupDto]:
        return list(map(GroupMapper.to_dto, entities))
