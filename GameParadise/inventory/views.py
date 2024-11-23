from django.shortcuts import render


def inventory(request):
    template = 'inventory/inventory.html'
    return render(request, template)
