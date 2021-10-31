from typing import List, Callable

from learn.domain.students.entities.student import Student
from learn.infrastructure.repositories.group_repository import GroupRepository
from learn.infrastructure.repositories.user_repository import UserRepository
from learn.models import User as UserModel, Group as GroupModel, Student as StudentModel


class StudentRepository:
    @staticmethod
    def model_to_entity(user_model: UserModel, group_model: GroupModel) -> Student:
        return Student(
            user=UserRepository.model_to_entity(user_model),
            group=GroupRepository.model_to_entity(group_model)
        )

    def get_students(self) -> List[Student]:
        # TODO: filter by role
        students = StudentModel.objects.all()
        map_lambda: Callable[[StudentModel], Student] = lambda sd: self.model_to_entity(s.user, s.group)
        return list(map(map_lambda, students))
