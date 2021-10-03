from typing import List

from learn.domain.groups.value_objects.group_id import GroupId
from learn.domain.students_group.entities.student_group import StudentGroup
from learn.domain.students_group.value_objects.student_group_id import StudentGroupId
from learn.domain.users.value_objects.user_id import UserId
from learn.models import StudentGroup as StudentGroupModel
from learn.models import Group as GroupModel
from learn.models import User as UserModel


class StudentGroupRepository:
    def __init__(self):
        pass

    @staticmethod
    def model_to_entity(student_group_model: StudentGroupModel) -> StudentGroup:
        id = StudentGroupId(student_group_model.id)
        user_id = UserId(student_group_model.user.id)
        group_id = GroupId(student_group_model.group.id)
        return StudentGroup(
            id=id,
            user_id=user_id,
            group_id=group_id
        )

    def save_student_group(self, student_group: StudentGroup) -> None:
        StudentGroupModel.objects.update_or_create(
            id=student_group.id.value,
            user=UserModel.objects.get(id=student_group.user_id.value),
            group=GroupModel.objects.get(id=student_group.group_id.value)
        )

    def get_students_group_by_group_id(self, group_id: str) -> List[StudentGroup]:
        students_group = StudentGroupModel.objects.filter(group=GroupModel.objects.get(id=group_id)).all()
        return list(map(self.model_to_entity, students_group))
