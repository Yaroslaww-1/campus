from typing import List

import inject

from learn.domain.posts.entities.post import Post
from learn.domain.posts.value_objects.post_id import PostId
from learn.infrastructure.event_bus.domain.domain_event_bus import DomainEventBus
from learn.infrastructure.repositories.user_repository import UserRepository
from learn.models import Post as PostModel


class PostRepository:
    @inject.autoparams()
    def __init__(self, event_bus: DomainEventBus):
        self.event_bus = event_bus

    @staticmethod
    def model_to_entity(model: PostModel) -> Post:
        return Post(
            id=PostId(model.id),
            name=model.name,
            content=model.content,
            created_at=model.created_at,
            created_by=UserRepository.model_to_entity(model.created_by)
        )

    @staticmethod
    def entity_to_model(entity: PostModel) -> PostModel:
        return PostModel(
            id=entity.id.value,
            name=entity.name,
            content=entity.content,
            created_at=entity.created_at,
            created_by=UserRepository.entity_to_model(entity.created_by)
        )

    def get_posts(self) -> List[Post]:
        posts = PostModel.objects.all()
        return list(map(self.model_to_entity, posts))

    def save_post(self, post: Post) -> None:
        self.event_bus.process_domain_events(post.domain_events)
        post.clear_domain_events()
        post_to_save = self.entity_to_model(post)
        PostModel.objects.update_or_create(
            id=post_to_save.id,
            name=post_to_save.name,
            content=post_to_save.content,
            created_at=post_to_save.created_at,
            created_by=post_to_save.created_by
        )
