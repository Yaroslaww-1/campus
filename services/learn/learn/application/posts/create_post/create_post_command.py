import inject
from pydantic import BaseModel, StrictStr

from learn.application.posts.dtos.post_dto import PostDto
from learn.application.posts.post_mapper import PostMapper
from learn.domain.posts.entities.post import Post
from learn.infrastructure.repositories.post_repository import PostRepository
from learn.infrastructure.repositories.user_repository import UserRepository


class CreatePostCommandDto(BaseModel):
    name: StrictStr
    content: StrictStr


class CreatePostCommand:
    @inject.autoparams()
    def __init__(self, post_repository: PostRepository, user_repository: UserRepository):
        self.post_repository = post_repository
        self.user_repository = user_repository

    def execute(self, dto: CreatePostCommandDto) -> PostDto:
        # TODO: replace by authenticated user
        created_by = self.user_repository.get_users()[0]
        post = Post.create_new_post(
            name=dto.name,
            content=dto.content,
            created_by=created_by
        )
        self.post_repository.save_post(post)
        return PostMapper.to_dto(post)
