from django.contrib import admin
from .models import Client


admin.site.register(Client)
# @admin.register(Client)
# class ClientAdmin(admin.ModelAdmin):
#     list_display = ['mail']
#     readonly_fields = ['mail']  # Делаем поля только для чтения

#     def has_add_permission(self, request):
#         return False  # Запрещаем добавлять

#     def has_change_permission(self, request, obj=None):
#         return False  # Запрещаем изменять

#     def has_delete_permission(self, request, obj=None):
#         return False  # Запрещаем удалять
