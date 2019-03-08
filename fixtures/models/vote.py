from django.conf import settings
from django.db import models

from .movie import Movie


class Vote(models.Model):
    UP = 1
    DOWN = -1
    VALUE_CHOICES = ((UP, '👍🏻',),
                     (DOWN, '👎🏻',),)

    value = models.SmallIntegerField(
        choices=VALUE_CHOICES,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    movie = models.ForeignKey(
        Movie
    )
    voted_on = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        unique_together = ('user', 'movie')
