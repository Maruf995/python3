from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'anime'

urlpatterns = [
    path('anime/', views.AnimeView.as_view(), name='naruto'),
    path('parser/', views.ParserAnimeView.as_view(), name='parser')
]