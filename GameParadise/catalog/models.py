from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=40, default='i_need_name')
    genre = models.CharField(max_length=40, default='NoGenre')
    price = models.IntegerField(default=100)
    sold = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    description = models.TextField(
        max_length=400, default='This is a good game, I think...')

    def __str__(self) -> str:
        return self.name
