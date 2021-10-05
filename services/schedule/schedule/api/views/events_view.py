from django.http import JsonResponse
from django.urls import path
from rest_framework.decorators import api_view, permission_classes

from schedule.api.constants import COMMON_ROUTE_URL
from schedule.api.serializers.dto_serializer import DtoSerializer
from schedule.application.events.get_events.get_events_query import GetEventsQuery


@api_view(["GET"])
def process_events(request):
    if request.method == "GET":
        events = GetEventsQuery().execute()
        return JsonResponse(DtoSerializer.to_dict(events, many=True), safe=False)


events_urlpatterns = [
    path(f'{COMMON_ROUTE_URL}/events', process_events),
]
