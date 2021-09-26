import uuid

from learn.domain.posts.value_objects.post_id import PostId


class Post():
    def __init__(self, id: PostId, name: str):
        self.id = id
        self.name = name

    # Just an example. TODO: remove
    def get_public_url(self, base_posts_url: str) -> str:
        return f'{base_posts_url}/{self.id}'

    @classmethod
    def create_new_post(cls, name: str) -> "Post":
        id = PostId(value=uuid.uuid4())
        post = Post(id, name)
        return post
