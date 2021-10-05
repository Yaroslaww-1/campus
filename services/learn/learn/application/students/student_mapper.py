from typing import List

from learn.application.groups.group_mapper import GroupMapper
from learn.application.students.dtos.student_dto import StudentDto
from learn.application.users.user_mapper import UserMapper
from learn.domain.students.entities.student import Student


class StudentMapper:
    @staticmethod
    def to_dto(entity: Student) -> StudentDto:
        return StudentDto(
            user=UserMapper.to_dto(entity.user),
            group=GroupMapper.to_dto(entity.group)
        )

    @staticmethod
    def to_dtos(entities: List[Student]) -> List[StudentDto]:
        return list(map(StudentMapper.to_dto, entities))
