from django.shortcuts import render
from catalog.models import Game


def index(request):
    games = Game.objects.raw('Select "id", "name", "price", "sold" FROM "catalog_game"')
    template = 'catalog/index.html'
    return render(request, template, {'games': games})
