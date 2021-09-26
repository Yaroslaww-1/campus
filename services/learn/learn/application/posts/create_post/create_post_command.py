from typing import List

import inject

from learn.application.posts.create_post.create_post_dto import CreatePostDto
from learn.application.posts.dtos.post_dto import PostDto
from learn.application.posts.post_mapper import PostMapper
from learn.domain.posts.entities.post import Post
from learn.infrastructure.repositories.post_repository import PostRepository


class CreatePostCommand:
    @inject.autoparams()
    def __init__(self, post_repository: PostRepository):
        self.post_repository = post_repository

    def execute(self, dto: CreatePostDto) -> PostDto:
        post = Post.create_new_post(name=dto.name)
        self.post_repository.save_post(post)
        return PostMapper.to_dto(post)
