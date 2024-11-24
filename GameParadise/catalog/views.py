from django.shortcuts import render
from catalog.models import Game


def index(request):
    games = Game.objects.all()
    template = 'catalog/index.html'
    return render(request, template, {'games': games})

def genre_games(request, genre_slug):
    games = Game.objects.filter(genre=genre_slug)
    template = 'catalog/genre.html'
    return render(request, template, {'games': games, 'genre': genre_slug})
