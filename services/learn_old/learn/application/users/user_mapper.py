from typing import List

from learn.application.users.dtos.user_dto import UserDto
from learn.domain.users.entities.user import User


class UserMapper:
    @staticmethod
    def to_dto(entity: User) -> UserDto:
        return UserDto(
            id=entity.id.value,
            name=entity.name,
            email=entity.email.value
        )

    @staticmethod
    def to_dtos(entities: List[User]) -> List[UserDto]:
        return list(map(UserMapper.to_dto, entities))
