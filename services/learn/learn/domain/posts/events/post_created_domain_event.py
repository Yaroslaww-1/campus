from dataclasses import dataclass

from learn.domain.common.domain_events import DomainEvent
from learn.domain.posts.value_objects.post_id import PostId


@dataclass(frozen=True)
class PostCreatedDomainEvent(DomainEvent):
    id: PostId
