from django.shortcuts import render
from catalog.models import Game


def inventory(request):
    games = Game.objects.all()
    template = 'inventory/inventory.html'
    return render(request, template, {'games': games})
