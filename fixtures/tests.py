from django.test import TestCase
from django.test.client import RequestFactory
from django.urls.base import reverse

from fixtures.models import Movie
from fixtures.views import MovieList


class MovieListPagination(TestCase):
    ACTIVE_PAGINATION_HTML = """
    <li class="page-item active">
        <a href="{}?page={}" class="page-link">{}</a>
    </li>
    """

    def setUp(self):
        for n in range(15):
            dummy_movie = Movie(
                title='Title {}'.format(n),
                year=1990 + n,
                runtime=100,
            )
            dummy_movie.save()


    def testFirstPage(self):
        # print("\033]34m testFirstPage \033]0m " + str(0))
        movie_list_path = reverse('fixtures:MovieList')
        request = RequestFactory().get(path=movie_list_path)
        response = MovieList.as_view()(request)
        self.assertEqual(200, response.status_code)
        self.assertTrue(response.context_data['is_paginated'])
        self.assertInHTML(
            self.ACTIVE_PAGINATION_HTML.format(
                movie_list_path, 1, 1
            ),
            response.rendered_content)
