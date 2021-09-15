from django.urls import path
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from learn.api.constants import COMMON_ROUTE_URL
from learn.api.serializers.post_serializer import PostSerializer
from learn.domain.posts.post_service import post_service

@api_view(['GET'])
def get_posts(request):
    posts = post_service.get_posts()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_post(request, pk):
    posts = post_service.get_posts()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data[0])

posts_urlpatterns = [
    path(f'{COMMON_ROUTE_URL}/posts/', get_posts),
    path(f'{COMMON_ROUTE_URL}/posts/<str:pk>/', get_post),
]
