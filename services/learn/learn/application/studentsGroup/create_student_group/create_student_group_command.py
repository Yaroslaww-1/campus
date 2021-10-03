import inject
from pydantic import BaseModel, UUID4

from learn.application.studentsGroup.dtos.student_group_dto import StudentGroupDto
from learn.application.studentsGroup.student_group_mapper import StudentGroupMapper
from learn.domain.students_group.entities.student_group import StudentGroup
from learn.infrastructure.repositories.student_group_repository import StudentGroupRepository


class CreateStudentGroupCommandDto(BaseModel):
    user_id: UUID4
    group_id: UUID4


class CreateStudentGroupCommand:
    @inject.autoparams()
    def __init__(self, student_group_repository: StudentGroupRepository):
        self.student_group_repository = student_group_repository

    def execute(self, dto: CreateStudentGroupCommandDto) -> StudentGroupDto:
        studentGroup = StudentGroup.create_new_student_group(user_id=dto.user_id, group_id=dto.group_id)
        self.student_group_repository.save_student_group(studentGroup)
        return StudentGroupMapper.to_dto(studentGroup)
