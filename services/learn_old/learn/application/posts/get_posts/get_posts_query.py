from typing import List

import inject

from learn.application.posts.dtos.post_dto import PostDto
from learn.application.posts.post_mapper import PostMapper
from learn.infrastructure.repositories.post_repository import PostRepository


class GetPostsQuery:
    @inject.autoparams()
    def __init__(self, post_repository: PostRepository):
        self.post_repository = post_repository

    def execute(self) -> List[PostDto]:
        posts = self.post_repository.get_posts()
        return PostMapper.to_dtos(posts)
