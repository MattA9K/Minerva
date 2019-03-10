# Author - Matt Andrzejczuk
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import (CreateView, )
from django.views.generic import (UpdateView, )

from fixtures.forms import VoteForm
from fixtures.models import (Vote, )


class CreateVote(LoginRequiredMixin, CreateView):
    form_class = VoteForm

    def get_initial(self):
        initial = super().get_initial()
        initial['user'] = self.request.user.id
        initial['movie'] = self.kwargs[
            'movie_id'
        ]
        return initial

    def get_success_url(self):
        movie_id = self.object.movie.id
        return reverse(
            'fixtures:MovieDetail',
            kwargs={'pk': movie_id}
        )

    def render_to_response(self, context, **response_kwargs):
        movie_id = context['object'].id
        movie_detail_url = reverse(
            'fixtures:MovieDetail',
            kwargs={'pk': movie_id}
        )
        return redirect(
            to=movie_detail_url
        )


class UpdateVote(LoginRequiredMixin, UpdateView):
    form_class = VoteForm
    queryset = Vote.objects.all()

    def get_object(self, queryset=None):
        vote = super().get_object(queryset)
        user = self.request.user
        if vote.user != user:
            raise PermissionDenied(
                'cannot change another '
                'users vote'
            )
        return vote

    def get_success_url(self):
        movie_id = self.object.movie.id
        return reverse(
            'fixtures:MovieDetail',
            kwargs={'pk': movie_id}
        )

    def render_to_response(self, context, **response_kwargs):
        movie_id = context['object'].id
        movie_detail_url = reverse(
            'fixtures:MovieDetail',
            kwargs={'pk': movie_id}
        )
        return redirect(
            to=movie_detail_url
        )
