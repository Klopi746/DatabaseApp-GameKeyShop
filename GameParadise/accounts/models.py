from django.db import models


class Client_Manager(models.Manager):
    def create_client(self, mail, password):
        client = self.create(mail=mail, password=password)
        return client


class Client(models.Model):
    mail = models.CharField(max_length=40, default='Vasya@gmail.cat')
    password = models.CharField(max_length=40, default='1234')

    objects = Client_Manager()

    def __str__(self) -> str:
        return self.mail
