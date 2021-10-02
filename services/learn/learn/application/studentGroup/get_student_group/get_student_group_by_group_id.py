from typing import List

import inject

from learn.application.studentGroup.dtos.student_group_dto import StudentGroupDto
from learn.application.studentGroup.student_group_mapper import StudentGroupMapper
from learn.infrastructure.repositories.studentGroup_repository import StudentGroupRepository


class GetStudentGroupsByGroupIdQuery:
    @inject.autoparams()
    def __init__(self, student_group_repository: StudentGroupRepository):
        self.student_group_repository = student_group_repository

    def execute(self, group_id: str) -> List[StudentGroupDto]:
        students_group = self.student_group_repository.get_students_group_by_group_id(group_id)
        return StudentGroupMapper.to_dtos(students_group)
