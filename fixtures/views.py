from django.views.generic import ListView, DetailView

from fixtures.models import Movie


class MovieList(ListView):
    model = Movie


class MovieDetail(DetailView):
    model = Movie
