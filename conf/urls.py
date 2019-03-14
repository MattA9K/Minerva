"""conf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

MEDIA_FILE_PATHS = static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)

urlpatterns = [
    # ADMIN / DEV
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),

    # PUBLIC
    path('movies/', include('fixtures.urls', namespace='fixtures')),
    path('security/', include('security.urls', namespace='security')),
]
urlpatterns += MEDIA_FILE_PATHS

if settings.DEBUG == False:
    urlpatterns[1] = None
