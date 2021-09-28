from typing import List

from learn.domain.posts.entities.post import Post
from learn.domain.posts.value_objects.post_id import PostId
from learn.models import Post as PostModel


class PostRepository:
    def __init__(self):
        pass

    @staticmethod
    def model_to_entity(post_model: PostModel) -> Post:
        post_id = PostId(post_model.id)
        post_name = post_model.name
        return Post(post_id, post_name)

    def get_posts(self) -> List[Post]:
        posts = PostModel.objects.all()
        return list(map(self.model_to_entity, posts))

    def save_post(self, post: Post) -> None:
        post = PostModel.objects.update_or_create(
            id=post.id.value,
            name=post.name
        )
