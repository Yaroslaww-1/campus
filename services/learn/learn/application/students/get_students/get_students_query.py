from typing import List

import inject

from learn.application.students.dtos.student_dto import StudentDto
from learn.application.students.student_mapper import StudentMapper
from learn.infrastructure.repositories.student_repository import StudentRepository


class GetStudentsQuery:
    @inject.autoparams()
    def __init__(self, student_repository: StudentRepository):
        self.student_repository = student_repository

    def execute(self) -> List[StudentDto]:
        students = self.student_repository.get_students()
        return StudentMapper.to_dtos(students)
