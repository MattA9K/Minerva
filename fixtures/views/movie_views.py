# Author - Matt Andrzejczuk
from django.urls import reverse
from django.views.generic import (ListView, DetailView, )

from fixtures.forms import (VoteForm, )
from fixtures.models import (Movie, Vote, )


class MovieList(ListView):
    model = Movie


class MovieDetail(DetailView):
    queryset = (
        Movie.objects.all_with_related_persons_and_score()
    )

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            vote = Vote.objects.get_vote_or_unsaved_blank_vote(
                movie=self.object,
                user=self.request.user
            )
            if vote.id:
                vote_form_url = reverse(
                    'fixtures:UpdateVote',
                    kwargs={'movie_id': vote.movie.id,
                            'pk': vote.id}
                )
            else:
                vote_form_url = (
                    reverse(
                        'fixtures:CreateVote',
                        kwargs={'movie_id': self.object.id}
                    )
                )
            vote_form = VoteForm(instance=vote)
            ctx['vote_form'] = vote_form
            ctx['vote_form_url'] = vote_form_url
        return ctx
