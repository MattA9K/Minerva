from django.urls import path

from fixtures.views import (
    MovieList, MovieDetail, TopMovies, UpdateVote, CreateVote, MovieImageUpload,
)

app_name = 'fixtures'
urlpatterns = [
    # Movie Views:
    path('movie',
         MovieList.as_view(),
         name='MovieList'),
    path('<int:pk>',
         MovieDetail.as_view(),
         name='MovieDetail'),
    path('top10/',
         TopMovies.as_view(),
         name='Top10'),


    # Vote Views
    path('<int:movie_id>/vote',
         CreateVote.as_view(),
         name='CreateVote'),
    path('movie/<int:movie_id>/vote/<int:pk>',
         UpdateVote.as_view(),
         name='UpdateVote'),

    # Upload Views
    path('movie/<int:movie_id>/image/upload',
         MovieImageUpload.as_view(),
         name='MovieImageUpload'),

]
