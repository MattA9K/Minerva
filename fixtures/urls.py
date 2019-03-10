from django.urls import path

from fixtures.views import (
    MovieList, MovieDetail, UpdateVote, CreateVote,
)

app_name = 'fixtures'
urlpatterns = [
    # Movie Views:
    path('',
         MovieList.as_view(),
         name='MovieList'),
    path('<int:pk>',
         MovieDetail.as_view(),
         name='MovieDetail'),

    # Vote Views
    path('movie/<int:movie_id>/vote',
         UpdateVote.as_view(),
         name='UpdateVote'),
    path('movie/<int:movie_id>/vote/<int:pk>',
         CreateVote.as_view(),
         name='UpdateVote'),
]
