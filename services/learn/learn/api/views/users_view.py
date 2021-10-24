from django.http import JsonResponse
from django.urls import path
from rest_framework.decorators import api_view, permission_classes

from learn.api.constants import COMMON_ROUTE_URL
from learn.api.serializers.dto_serializer import DtoSerializer
from learn.application.users.create_user.create_user_command import CreateUserCommand, CreateUserCommandDto
from learn.application.users.get_users.get_user_by_id_query import GetUserByIdQuery
from learn.application.users.get_users.get_users_query import GetUsersQuery


@api_view(["GET", "POST"])
def process_users(request):
    if request.method == "GET":
        users = GetUsersQuery().execute()
        return JsonResponse(DtoSerializer.to_dict(users, many=True), safe=False)
    elif request.method == "POST":
        dto = DtoSerializer.from_json(request.data, CreateUserCommandDto)
        user = CreateUserCommand().execute(dto)
        return JsonResponse(DtoSerializer.to_dict(user), safe=False)


@api_view(["GET"])
def process_user_by_id(request, id):
    user = GetUserByIdQuery().execute(id)
    return JsonResponse(DtoSerializer.to_dict(user), safe=False)


users_urlpatterns = [
    path(f'{COMMON_ROUTE_URL}users', process_users),
    path(f'{COMMON_ROUTE_URL}users/<str:id>/', process_user_by_id),
]
