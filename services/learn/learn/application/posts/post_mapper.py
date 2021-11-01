from typing import List

from learn.application.posts.dtos.post_dto import PostDto
from learn.application.users.user_mapper import UserMapper
from learn.domain.posts.entities.post import Post


class PostMapper:
    @staticmethod
    def to_dto(entity: Post) -> PostDto:
        return PostDto(
            id=entity.id.value,
            name=entity.name,
            content=entity.content,
            created_at=entity.created_at,
            created_by=UserMapper.to_dto(entity.created_by)
        )

    @staticmethod
    def to_dtos(entities: List[Post]) -> List[PostDto]:
        return list(map(PostMapper.to_dto, entities))
