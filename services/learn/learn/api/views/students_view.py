from django.http import JsonResponse
from django.urls import path
from rest_framework.decorators import api_view

from learn.api.constants import COMMON_ROUTE_URL
from learn.api.serializers.dto_serializer import DtoSerializer
from learn.application.students.get_students.get_students_query import GetStudentsQuery


@api_view(["GET"])
def get_students(request):
    students = GetStudentsQuery().execute()
    return JsonResponse(DtoSerializer.to_dict(students, many=True), safe=False)


students_group_urlpatterns = [
    path(f'{COMMON_ROUTE_URL}/students', get_students),
]
