from django.http import JsonResponse
from django.urls import path
from rest_framework.decorators import api_view, permission_classes

from learn.api.constants import COMMON_ROUTE_URL
from learn.api.serializers.dto_serializer import DtoSerializer
from learn.application.students_group.create_student_group.create_student_group_command import \
    CreateStudentGroupCommandDto, CreateStudentGroupCommand
from learn.application.students_group.get_student_group.get_students_group_by_group_id import \
    GetStudentsGroupByGroupIdQuery


@api_view(["GET"])
def get_students_group_by_group_id(request, id):
    students_group = GetStudentsGroupByGroupIdQuery().execute(id)
    return JsonResponse(DtoSerializer.to_dict(students_group, many=True), safe=False)


@api_view(["POST"])
def process_student_group(request):
    dto = DtoSerializer.from_json(request.data, CreateStudentGroupCommandDto)
    student_group = CreateStudentGroupCommand().execute(dto)
    return JsonResponse(DtoSerializer.to_dict(student_group), safe=False)


students_group_urlpatterns = [
    path(f'{COMMON_ROUTE_URL}/studentGroup', process_student_group),
    path(f'{COMMON_ROUTE_URL}/groupd/<str:id>/students', get_students_group_by_group_id),
]
