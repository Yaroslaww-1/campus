import inject
from django.core.files.uploadedfile import InMemoryUploadedFile

from pydantic import BaseModel

from learn.infrastructure.aws.aws_s3_service import AwsS3Service
from learn.infrastructure.repositories.user_repository import UserRepository


class CreateUserAvatarCommandDto(BaseModel):
    id: str
    avatar: InMemoryUploadedFile

    class Config:
        arbitrary_types_allowed = True


class CreateUserAvatarCommand:
    @inject.autoparams()
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, dto: CreateUserAvatarCommandDto) -> None:
        user = self.user_repository.get_user_by_id(dto.id)
        url = AwsS3Service.upload_replace_file(dto.id, user.avatar, dto.avatar)
        user.set_avatar(url)
        # TODO: use update_user in future(when roles will be done)
        self.user_repository.update_user_avatar(user)
