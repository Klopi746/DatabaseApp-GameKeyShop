from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.login, name='login'),
    path('login_handler/', views.login_handler, name='login_handler'),
]
