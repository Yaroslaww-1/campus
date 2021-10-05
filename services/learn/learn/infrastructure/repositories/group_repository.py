from typing import List

from learn.domain.groups.entities.group import Group
from learn.domain.groups.value_objects.group_id import GroupId
from learn.domain.groups.value_objects.year import Year
from learn.models import Group as GroupModel


class GroupRepository:
    def __init__(self):
        pass

    @staticmethod
    def model_to_entity(group_model: GroupModel) -> Group:
        id = GroupId(group_model.id)
        formed_at_year = Year(group_model.formed_at_year)
        return Group(
            id=id,
            name=group_model.name,
            formed_at_year=formed_at_year
        )

    def get_groups(self) -> List[Group]:
        groups = GroupModel.objects.all()
        return list(map(self.model_to_entity, groups))

    def save_group(self, group: Group) -> None:
        GroupModel.objects.update_or_create(
            id=group.id.value,
            name=group.name,
            formed_at_year=group.formed_at_year.value
        )

    # TODO: implement. Left as an example
    def add_student(self) -> None:
        raise NotImplementedError()
