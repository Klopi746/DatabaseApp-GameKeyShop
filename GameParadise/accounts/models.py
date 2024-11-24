from django.db import models


class Client(models.Model):
    mail = models.CharField(max_length=40, default='Vasya@gmail.cat')
    password = models.CharField(max_length=40, default='1234')

    def __str__(self) -> str:
        return self.mail
