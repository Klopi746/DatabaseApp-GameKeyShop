from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    sold = models.IntegerField()
