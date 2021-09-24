from typing import List

from learn.domain.posts.entities.post import Post
from learn.domain.posts.value_objects.post_id import PostId
from learn.models import Post as PostModel


class PostRepository:
    def __init__(self):
        pass

    def _model_to_entity(self, post_model: PostModel) -> Post:
        post_id = PostId(post_model.id)
        post_name = post_model.name
        return Post(post_id, post_name)

    def get_posts(self) -> List[Post]:
        posts = PostModel.objects.all()
        return list(map(self._model_to_entity, posts))

    # TODO: add typings
    def get_post_by_id(self, id):
        return PostModel.objects.get(id=id)

    def get_post_by_name(self, name):
        return PostModel.objects.get(name=name)

    def create_post(self, id, name):
        PostModel.objects.create(id=id, name=name)

    def delete_post_by_id(self, id):
        PostModel.objects.filter(id=id).delete()

    def delete_post_by_name(self, name):
        PostModel.objects.filter(name=name).delete()

