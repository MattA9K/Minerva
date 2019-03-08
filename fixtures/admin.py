from django.contrib import admin

# Register your models here.
from fixtures.models import Movie

admin.site.register(Movie)
