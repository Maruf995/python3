from django.urls import path
from . import views

urlpatterns = [
    path("hello", views.hello_world_view),
    path("date/", views.date_view),
    path("", views.blog_view),
    path("<int:pk>/", views.post_detail, name='post-detail'),
    path("<int:pk>/change/", views.EditBlogView.as_view()),
    path("<int:pk>/comment/", views.create_comment),
    path("create/", views.CreateBlogView.as_view()),
]






