from django.shortcuts import render
from django.shortcuts import redirect
from accounts.models import Client


def login(request):
    template = 'accounts/login.html'
    return render(request, template)


def login_handler(request):
    mail = request.POST.get('mail')
    password = request.POST.get('password')
    if Client.objects.filter(mail=mail).exists():
        if Client.objects.filter(mail=mail)[0].password == password:
            logged_in = True
            request.session['logged_in'] = logged_in
            request.session['user_mail'] = mail
        else:
            template = 'accounts/login.html'
            return render(request, template, {'is_fail': True})
    else:
        new_client = Client.objects.create_client(mail=mail, password=password)
        new_client.save()
        logged_in = True
        request.session['logged_in'] = logged_in
        request.session['user_mail'] = mail
    return redirect('/')


def logout(request):
    logged_in = False
    request.session['logged_in'] = logged_in
    return redirect('/')
