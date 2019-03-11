# Author - Matt Andrzejczukd
from django.contrib.auth.mixins import (
    LoginRequiredMixin
)
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView

from fixtures.forms import MovieImageForm


class MovieImageUpload(LoginRequiredMixin, CreateView):
    form_class = MovieImageForm

    def get_initial(self):
        initial = super().get_initial()
        initial['user'] = self.request.user.id
        initial['movie'] = self.kwargs['movie_id']
        return initial

    def render_to_response(self, context, **response_kwargs):
        movie_id = self.kwargs['movie_id']
        movie_detail_url = reverse(
            'fixtures:MovieDetail',
            kwargs={'pk': movie_id}
        )
        return redirect(to=movie_detail_url)

    def get_success_url(self):
        movie_id = self.kwargs['movie_id']
        movie_detail_url = reverse('fixtures:MovieDetail', kwargs={'pk': movie_id})
        return movie_detail_url
