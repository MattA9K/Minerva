from django.conf import settings
from django.db import models

from .movie import Movie


class VoteManager(models.Manager):
    def get_vote_or_unsaved_blank_vote(self, movie, user):
        try:
            return Vote.objects.get(
                movie=movie,
                user=user
            )
        except Vote.DoesNotExist:
            return Vote(
                movie=movie,
                user=user
            )


class Vote(models.Model):
    UP = 1
    DOWN = -1
    VALUE_CHOICES = ((UP, '👍🏻',),
                     (DOWN, '👎🏻',),)

    objects = VoteManager()

    value = models.SmallIntegerField(
        choices=VALUE_CHOICES,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    movie = models.ForeignKey(
        Movie,
        on_delete=models.SET_NULL,
        null=True
    )
    voted_on = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        unique_together = ('user', 'movie')
