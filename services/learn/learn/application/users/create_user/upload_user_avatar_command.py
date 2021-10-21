import inject

from pydantic import BaseModel

from learn.infrastructure.repositories.user_repository import UserRepository


class CreateUserAvatarCommandDto(BaseModel):
    id: str
    avatar: str


class CreateUserAvatarCommand:
    @inject.autoparams()
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, dto: CreateUserAvatarCommandDto) -> None:
        self.user_repository.save_user_avatar(dto.id, dto.avatar)
