from django.urls import path
from .views import hello_world_view, date_view, blog_view


urlpatterns = [
    path("hello", hello_world_view),
    path("date/", date_view),
    path("", blog_view),
]