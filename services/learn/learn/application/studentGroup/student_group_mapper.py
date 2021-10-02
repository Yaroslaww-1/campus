from typing import List

from learn.application.studentGroup.dtos.student_group_dto import StudentGroupDto
from learn.domain.studentGroup.entities.studentGroup import StudentGroup


class StudentGroupMapper:
    @staticmethod
    def to_dto(entity: StudentGroup) -> StudentGroupDto:
        return StudentGroupDto(
            id=entity.id.value,
            user_id=entity.user_id.value,
            group_id=entity.group_id.value
        )

    @staticmethod
    def to_dtos(entities: List[StudentGroup]) -> List[StudentGroupDto]:
        return list(map(StudentGroupMapper.to_dto, entities))
