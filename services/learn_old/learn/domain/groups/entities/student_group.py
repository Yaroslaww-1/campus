from learn.domain.groups.value_objects.group_id import GroupId
from learn.domain.groups.value_objects.student_group_id import StudentGroupId
from learn.domain.users.value_objects.user_id import UserId


class StudentGroup:
    def __init__(self, id: StudentGroupId, user_id: UserId, group_id: GroupId):
        self.id = id
        self.user_id = user_id
        self.group_id = group_id
