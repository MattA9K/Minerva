# Author - Matt Andrzejczuk
from uuid import uuid4

from django.conf import settings
from django.db import models


def movie_directory_path_with_uuid(instance, filename):
    return '{}/{}'.format(instance.movie_id, uuid4())


class MovieImage(models.Model):
    image = models.ImageField(upload_to=movie_directory_path_with_uuid)
    uploaded = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
