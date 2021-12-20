from django.urls import path
from . import views
app_name = 'film'
urlpatterns = [
    path('films/', views.FilmView.as_view(), name='film'),
    path('filmparser/', views.ParserFilmView.as_view(), name='parser')
]