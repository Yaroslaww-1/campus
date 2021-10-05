import uuid

from learn.domain.groups.entities.student_group import StudentGroup
from learn.domain.groups.value_objects.group_id import GroupId
from learn.domain.groups.value_objects.student_group_id import StudentGroupId
from learn.domain.groups.value_objects.year import Year
from learn.domain.users.value_objects.user_id import UserId


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

    def add_student(self, student_user_id: UserId) -> "StudentGroup":
        id = StudentGroupId(value=uuid.uuid4())
        student_group = StudentGroup(id, student_user_id, self.id)
        return student_group