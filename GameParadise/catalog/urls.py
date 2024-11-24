from django.urls import path

from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.index, name='index'),
    path(
        'category/<slug:genre_slug>/',
        views.genre_games,
        name='genre_games'
    ),
]
