from .views.users_view import users_urlpatterns
from .views.events_view import events_urlpatterns

urlpatterns = [] +users_urlpatterns + events_urlpatterns
