from django.db import models

from .person import Person


class MovieManager(models.Manager):
    def all_with_related(self):
        qs = self.get_queryset()
        qs = qs.select_related('director')
        qs = qs.prefetch_related(
            'writers', 'actors'
        )
        return qs


# Create your models here.
class Movie(models.Model):
    objects = MovieManager()

    class Meta:
        ordering = ('-year', 'title')

    NOT_RATED = 0
    RATED_G = 1
    RATED_PG = 2
    RATED_R = 3
    RATINGS = (
        (NOT_RATED, 'NR - Not Rated'),
        (RATED_G, 'G - General Audience'),
        (RATED_PG, 'PG - Parental Guidance Suggested'),
        (RATED_R, 'R - Restricted'),
    )
    title = models.CharField(max_length=140)
    plot = models.TextField()
    year = models.PositiveIntegerField()
    rating = models.IntegerField(choices=RATINGS, default=NOT_RATED)
    runtime = models.PositiveIntegerField()
    website = models.URLField(blank=True)

    director = models.ForeignKey(
        to='Person',
        on_delete=models.SET_NULL,
        related_name='directed',
        null=True,
        blank=True
    )

    writers = models.ManyToManyField(
        to='Person',
        related_name='writing_credits',
        blank=True
    )

    actors = models.ManyToManyField(
        to='Person',
        through='Role',
        related_name='acting_credits',
        blank=True
    )

    def __str__(self):
        return '{} ({})'.format(self.title, self.year)


class Role(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.DO_NOTHING)
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=140)

    def __str__(self):
        return "{} {} {}".format(self.movie_id, self.person_id, self.name)

    class Meta:
        unique_together = ('movie',
                           'person',
                           'name')
