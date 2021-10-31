from typing import List

from learn.application.posts.dtos.post_dto import PostDto
from learn.domain.posts.entities.post import Post


class PostMapper:
    @staticmethod
    def to_dto(entity: Post) -> PostDto:
        return PostDto(
            id=entity.id.value,
            name=entity.name
        )

    @staticmethod
    def to_dtos(entities: List[Post]) -> List[PostDto]:
        return list(map(PostMapper.to_dto, entities))
