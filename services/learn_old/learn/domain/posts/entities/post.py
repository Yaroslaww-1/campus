from datetime import datetime
import uuid

from learn.domain.common.domain_events import WithDomainEventsMixin
from learn.domain.posts.events.post_created_domain_event import PostCreatedDomainEvent
from learn.domain.posts.value_objects.post_id import PostId
from learn.domain.users.entities.user import User


class Post(WithDomainEventsMixin):
    def __init__(self, id: PostId, name: str, content: str, created_at: datetime.timestamp, created_by: User):
        super().__init__()
        self.id = id
        self.name = name
        self.content = content
        self.created_by = created_by
        self.created_at = created_at

    # Just an example. TODO: remove
    def get_public_url(self, base_posts_url: str) -> str:
        return f'{base_posts_url}/{self.id}'

    @classmethod
    def create_new_post(cls, name: str, content: str, created_by: User) -> "Post":
        id = PostId(value=uuid.uuid4())
        post = Post(id, name, content, datetime.now(), created_by)
        post.add_domain_event(PostCreatedDomainEvent(
            id
        ))
        return post
