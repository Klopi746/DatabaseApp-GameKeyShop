from django.shortcuts import render
from catalog.models import Game


def index(request):
    games = Game.objects.all()
    print(games.query)
    template = 'catalog/index.html'
    logged_in = request.session.get('logged_in', False)
    user_mail = request.session.get('user_mail', 'Error')
    return render(request, template, {'games': games, 'logged': logged_in, 'user_mail': user_mail})

def genre_games(request, genre_slug):
    games = Game.objects.filter(genre=genre_slug)
    print(games.query)
    template = 'catalog/genre.html'
    logged_in = request.session.get('logged_in', False)
    user_mail = request.session.get('user_mail', 'Error')
    return render(request, template, {'games': games, 'genre': genre_slug, 'logged': logged_in, 'user_mail': user_mail})
