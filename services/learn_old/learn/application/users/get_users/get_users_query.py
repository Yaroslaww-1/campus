from typing import List

import inject

from learn.application.users.dtos.user_dto import UserDto
from learn.application.users.user_mapper import UserMapper
from learn.infrastructure.repositories.user_repository import UserRepository


class GetUsersQuery:
    @inject.autoparams()
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self) -> List[UserDto]:
        users = self.user_repository.get_users()
        return UserMapper.to_dtos(users)
