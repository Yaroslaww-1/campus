from django.http import JsonResponse
from django.urls import path
from rest_framework.decorators import api_view, permission_classes

from learn.api.constants import COMMON_ROUTE_URL
from learn.api.serializers.dto_serializer import DtoSerializer
from learn.application.groups.create_group.create_group_command import CreateGroupCommandDto, CreateGroupCommand
from learn.application.groups.get_groups.get_groups_query import GetGroupsQuery


@api_view(["GET", "POST"])
def process_groups(request):
    if request.method == "GET":
        groups = GetGroupsQuery().execute()
        return JsonResponse(DtoSerializer.to_dict(groups, many=True), safe=False)
    elif request.method == "POST":
        dto = DtoSerializer.from_json(request.data, CreateGroupCommandDto)
        group = CreateGroupCommand().execute(dto)
        return JsonResponse(DtoSerializer.to_dict(group), safe=False)


groups_urlpatterns = [
    path(f'{COMMON_ROUTE_URL}/groups', process_groups),
]
