from django.shortcuts import render
from django.shortcuts import redirect


def login(request):
    template = 'accounts/login.html'
    return render(request, template)

def login_handler(request):
    return redirect('catalog:index')
