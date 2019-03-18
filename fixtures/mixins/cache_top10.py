# Author - Matt Andrzejczuk
from django.core.cache import caches
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from django.views.generic import ListView

from pyink import ink


class CachePageVaryOnCookieMixin():
    """
    Mixin caching a single page.

    Subclasses can provide these attributes:

    `cache_name` - name of cache to use.
    `timeout` - cache timeout for this
    page. When not provided, the default
    cache timeout is used.
    """
    cache_name = 'default'

    @classmethod
    def get_timeout(cls):
        ink.p("CachePageVaryOnCookieMixin get_timeout", ink.BG_BLUE, ink.ENDC + "\n")
        if hasattr(cls, 'timeout'):
            return cls.timeout
        cache = caches[cls.cache_name]
        return cache.default_timeout

    @classmethod
    def as_view(cls, *args, **kwargs):
        ink.p("CachePageVaryOnCookieMixin as_view", ink.BG_BLUE, ink.ENDC + "\n")
        view = super().as_view(
            *args, **kwargs
        )
        view = vary_on_cookie(view)
        view = cache_page(
            timeout=cls.get_timeout(),
            cache=cls.cache_name,
        )(view)
        return view
