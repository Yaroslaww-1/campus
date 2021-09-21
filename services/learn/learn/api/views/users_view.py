from django.urls import path
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from learn.api.constants import COMMON_ROUTE_URL
from learn.api.serializers.user_serializer import UserSerializer
from learn.domain.users.user_service import user_service


@api_view(['GET'])
def get_users(request):
    users = user_service.get_users()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


users_urlpatterns = [
    path(f'{COMMON_ROUTE_URL}/users/', get_users),
]
