from typing import Any
from django.contrib import admin
from django.http import HttpRequest
from .models import Client


# admin.site.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['mail']
    fields = ['mail']

    def get_readonls_superusey_fields(self, request: HttpRequest, obj=None):
        return ['password'] if not request.user.ir else []


admin.site.register(Client, ClientAdmin)
