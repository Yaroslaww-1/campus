import uuid

from learn.domain.groups.value_objects.group_id import GroupId
from learn.domain.students_group.value_objects.student_group_id import StudentGroupId
from learn.domain.users.value_objects.user_id import UserId


class StudentGroup:
    def __init__(self, id: StudentGroupId, user_id: UserId, group_id: GroupId):
        self.id = id
        self.user_id = user_id
        self.group_id = group_id

    @classmethod
    def create_new_student_group(cls, user_id: uuid, group_id: uuid) -> "StudentGroup":
        id = StudentGroupId(value=uuid.uuid4())
        user_id = UserId(value=user_id)
        group_id = GroupId(value=group_id)
        student_group = StudentGroup(id, user_id, group_id)
        return student_group
