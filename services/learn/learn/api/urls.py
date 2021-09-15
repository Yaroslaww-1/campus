from django.urls import path

from .views.posts_view import posts_urlpatterns

urlpatterns = [] + posts_urlpatterns
