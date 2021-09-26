from django.http import JsonResponse
from django.urls import path
from rest_framework.decorators import api_view, permission_classes

from learn.api.constants import COMMON_ROUTE_URL
from learn.api.serializers.dataclass_serializer import DataclassSerializer
from learn.application.users.create_user.create_user_command import CreateUserCommand
from learn.application.users.create_user.create_user_dto import CreateUserDto
from learn.application.users.get_users.get_users_query import GetUsersQuery


@api_view(["GET", "POST"])
def process_users(request):
    if request.method == "GET":
        query = GetUsersQuery()
        users = query.execute()
        return JsonResponse(DataclassSerializer.to_dict(users, many=True), safe=False)
    elif request.method == "POST":
        command = CreateUserCommand()
        dto = DataclassSerializer.from_json(request.data, CreateUserDto)
        user = command.execute(dto)
        return JsonResponse(DataclassSerializer.to_dict(user), safe=False)


users_urlpatterns = [
    path(f'{COMMON_ROUTE_URL}/users', process_users),
]
