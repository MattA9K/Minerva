# Author - Matt Andrzejczuk
from django import forms
from django.contrib.auth import get_user_model

from fixtures.models import MovieImage, Movie


class MovieImageForm(forms.ModelForm):
    movie = forms.ModelChoiceField(
        widget=forms.HiddenInput,
        queryset=Movie.objects.all(),
        disabled=True
    )

    user = forms.ModelChoiceField(
        widget=forms.HiddenInput,
        queryset=get_user_model().objects.all(),
        disabled=True,
    )

    class Meta:
        model = MovieImage
        fields = ('image', 'user', 'movie')
