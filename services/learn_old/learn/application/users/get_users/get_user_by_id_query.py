import inject

from learn.application.users.dtos.user_dto import UserDto
from learn.application.users.user_mapper import UserMapper
from learn.infrastructure.repositories.user_repository import UserRepository


class GetUserByIdQuery:
    @inject.autoparams()
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, id) -> UserDto:
        user = self.user_repository.get_user_by_id(id)
        return UserMapper.to_dto(user)
