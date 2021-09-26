from django.http import JsonResponse, HttpResponse
from django.urls import path
from rest_framework.decorators import api_view, permission_classes

from learn.api.constants import COMMON_ROUTE_URL
from learn.api.serializers.dataclass_serializer import DataclassSerializer
from learn.application.posts.create_post.create_post_command import CreatePostCommand
from learn.application.posts.create_post.create_post_dto import CreatePostDto
from learn.application.posts.get_posts.get_posts_query import GetPostsQuery


@api_view(['GET', 'POST'])
def process_posts(request):
    if request.method == "GET":
        query = GetPostsQuery()
        posts = query.execute()
        return JsonResponse(DataclassSerializer.to_dict(posts, many=True), safe=False)
    elif request.method == "POST":
        command = CreatePostCommand()
        dto = DataclassSerializer.from_json(request.data, CreatePostDto)
        post = command.execute(dto)
        return JsonResponse(DataclassSerializer.to_dict(post), safe=False)


posts_urlpatterns = [
    path(f'{COMMON_ROUTE_URL}/posts', process_posts),
]
