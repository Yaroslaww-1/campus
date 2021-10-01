import uuid

from learn.domain.groups.value_objects.group_id import GroupId
from learn.domain.groups.value_objects.year import Year


class Group:
    def __init__(self, id: GroupId, name: str, formed_at_year: Year):
        self.id = id
        self.name = name
        self.formed_at_year = formed_at_year

    @classmethod
    def create_new_group(cls, name: str, formed_at_year: int) -> "Group":
        id = GroupId(value=uuid.uuid4())
        formed_at_year = Year(value=formed_at_year)
        group = Group(id, name, formed_at_year)
        return group
