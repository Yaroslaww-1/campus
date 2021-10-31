from django.http import JsonResponse, HttpResponse
from django.urls import path
from rest_framework.decorators import api_view, permission_classes

from learn.api.auth.authenticated_user_context import AuthenticatedUserContext
from learn.api.constants import COMMON_ROUTE_URL
from learn.api.decorators.in_roles_decorator import in_roles
from learn.api.enums.roles_enum import Role
from learn.api.serializers.dto_serializer import DtoSerializer
from learn.application.posts.create_post.create_post_command import CreatePostCommand, CreatePostCommandDto
from learn.application.posts.get_posts.get_posts_query import GetPostsQuery


@api_view(['GET', 'POST'])
@in_roles([Role.STUDENT, Role.ADMIN, Role.TEACHER])
def process_posts(request):
    if request.method == "GET":
        print('user_id', AuthenticatedUserContext(request).user_id)
        posts = GetPostsQuery().execute()
        return JsonResponse(DtoSerializer.to_dict(posts, many=True), safe=False)
    elif request.method == "POST":
        dto = DtoSerializer.from_json(request.data, CreatePostCommandDto)
        post = CreatePostCommand().execute(dto)
        return JsonResponse(DtoSerializer.to_dict(post), safe=False)


posts_urlpatterns = [
    path(f'{COMMON_ROUTE_URL}posts', process_posts),
]
