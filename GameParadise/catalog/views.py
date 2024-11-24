from django.shortcuts import render
from catalog.models import Game


def index(request):
    games = Game.objects.all()
    template = 'catalog/index.html'
    logged_in = request.session.get('logged_in', False)
    return render(request, template, {'games': games, 'logged': logged_in})

def genre_games(request, genre_slug):
    games = Game.objects.filter(genre=genre_slug)
    template = 'catalog/genre.html'
    logged_in = request.session.get('logged_in', False)
    return render(request, template, {'games': games, 'genre': genre_slug, 'logged': logged_in})
