from typing import List

import inject

from learn.application.groups.dtos.group_dto import GroupDto
from learn.application.groups.group_mapper import GroupMapper
from learn.infrastructure.repositories.group_repository import GroupRepository


class GetGroupsQuery:
    @inject.autoparams()
    def __init__(self, group_repository: GroupRepository):
        self.group_repository = group_repository

    def execute(self) -> List[GroupDto]:
        groups = self.group_repository.get_groups()
        return GroupMapper.to_dtos(groups)
