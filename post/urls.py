from django.urls import path
from . import views
    #hello_world_view, date_view, blog_view, post_detail, CreateBlogView


urlpatterns = [
    path("hello", views.hello_world_view),
    path("date/", views.date_view),
    path("", views.blog_view),
    path("<int:pk>/", views.post_detail),
    path("create/", views.CreateBlogView.as_view())
]