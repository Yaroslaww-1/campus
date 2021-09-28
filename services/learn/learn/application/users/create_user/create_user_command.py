import inject
from pydantic import BaseModel, StrictStr, EmailStr


from learn.application.users.dtos.user_dto import UserDto
from learn.application.users.user_mapper import UserMapper
from learn.domain.users.entities.user import User
from learn.infrastructure.repositories.user_repository import UserRepository


class CreateUserCommandDto(BaseModel):
    name: StrictStr
    email: EmailStr


class CreateUserCommand:
    @inject.autoparams()
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, dto: CreateUserCommandDto) -> UserDto:
        user = User.create_new_user(name=dto.name, email=dto.email)
        self.user_repository.save_user(user)
        return UserMapper.to_dto(user)
