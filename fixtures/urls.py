from django.urls import path

from fixtures.views import MovieList, MovieDetail

app_name = 'fixtures'
urlpatterns = [
    path('', MovieList.as_view(), name='MovieList'),
    path('<int:pk>', MovieDetail.as_view(), name='MovieDetail'),
]
