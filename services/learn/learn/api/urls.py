from django.urls import path

from .views.groups_view import groups_urlpatterns
from .views.posts_view import posts_urlpatterns
from .views.users_view import users_urlpatterns

urlpatterns = [] + posts_urlpatterns + users_urlpatterns + groups_urlpatterns
