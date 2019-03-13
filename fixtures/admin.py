from django.contrib import admin

# Register your models here.
from fixtures.models import Movie, Person, Role, MovieImage

admin.site.register(Movie)
admin.site.register(Person)
admin.site.register(Role)
admin.site.register(MovieImage)
