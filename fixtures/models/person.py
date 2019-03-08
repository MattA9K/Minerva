from django.db import models


class PersonManager(models.Manager):
    def all_with_prefetch_movies(self):
        qs = self.get_queryset()
        return qs.prefetch_related(
            'directed',
            'writing_credits',
            'role_set__movie'
        )


class Person(models.Model):
    first_name = models.CharField(max_length=140)
    last_name = models.CharField(max_length=140)
    born = models.DateField()
    died = models.DateField(null=True, blank=True)

    objects = PersonManager()

    class Meta:
        ordering = ('last_name', 'first_name')

    def __str__(self):
        if self.died:
            return '{}, {} ({}-{})'.format(
                self.last_name,
                self.first_name,
                self.born,
                self.died
            )
        return '{}, {} ({})'.format(
            self.last_name,
            self.first_name,
            self.born
        )
