from learn.domain.common.base_entity import BaseEntity
from learn.domain.posts.value_objects.post_id import PostId


class Post(BaseEntity):
    def __init__(self, id: PostId, name: str):
        super().__init__(id)
        self.name = name

    # Just an example. TODO: remove
    def get_public_url(self, base_posts_url: str) -> str:
        return f'{base_posts_url}/{self.id}'

    @classmethod
    def create_new_post(cls, id: PostId, name: str) -> "Post":
        post = Post(id, name)
        return post
