from django.urls import path
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from learn.api.constants import COMMON_ROUTE_URL
from learn.api.serializers.user_serializer import UserSerializer
from learn.api.serializers.user_serializer import UserCreateSerializer
from learn.domain.users.user_service import user_service


@api_view(["GET", "POST", "PUT"])
def process_users(request):
    if request.method == "GET":
        users = user_service.get_users()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = user_service.create_user(serializer.validated_data.get('name'),
                                        serializer.validated_data.get('email'))
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == "PUT":
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = user_service.update_user(serializer.validated_data.get('id'),
                                        serializer.validated_data.get('name'),
                                        serializer.validated_data.get('email'))
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


@api_view(['GET', "DELETE"])
def process_user_by_id(request, id):
    if request.method == "GET":
        user = user_service.get_user_by_id(id)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        user_service.delete_user_by_id(id)
        return Response(status=status.HTTP_204_NO_CONTENT)


users_urlpatterns = [
    path(f'{COMMON_ROUTE_URL}/users/', process_users),
    path(f'{COMMON_ROUTE_URL}/users/<str:id>/', process_user_by_id),
]
