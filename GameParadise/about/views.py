from django.shortcuts import render


def about(request):
    template = 'about/about.html'
    logged_in = request.session.get('logged_in', False)
    return render(request, template, {'logged': logged_in})
