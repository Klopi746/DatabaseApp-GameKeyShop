from django.shortcuts import render
from catalog.models import Game


def inventory(request):
    games = Game.objects.raw('Select "id", "name", "price", "sold" FROM "catalog_game"')
    template = 'inventory/inventory.html'
    return render(request, template, {'games': games})
