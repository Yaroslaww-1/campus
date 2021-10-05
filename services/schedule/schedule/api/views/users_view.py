from django.http import JsonResponse
from django.urls import path
from rest_framework.decorators import api_view, permission_classes

from schedule.api.constants import COMMON_ROUTE_URL
from schedule.api.serializers.dto_serializer import DtoSerializer
from schedule.application.users.get_users.get_users_query import GetUsersQuery


@api_view(["GET"])
def process_users(request):
    if request.method == "GET":
        users = GetUsersQuery().execute()
        return JsonResponse(DtoSerializer.to_dict(users, many=True), safe=False)


users_urlpatterns = [
    path(f'{COMMON_ROUTE_URL}/users', process_users),
]
