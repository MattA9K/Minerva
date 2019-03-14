"""
DEVELOPED BY: MATT ANDRZEJCZUK
"""
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '6li%=%9*@1h3f&o5hb@z%-0q9bh_lek*o$%bhj2rmi7n!%9n3-'
DEBUG = True
ALLOWED_HOSTS = []
LOGIN_REDIRECT_URL = 'fixtures:MovieList'


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3RD PARTY DJANGO MUST-HAVES:
    'django_extensions',
    'debug_toolbar',

    # PROJECT APPS:
    'fixtures',
    'security',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]
ROOT_URLCONF = 'conf.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
WSGI_APPLICATION = 'conf.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR + '/static'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'resources'),
)

MEDIA_URL = '/uploads/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]

DEBUG_TOOLBAR_CONFIG = {
    # TOOLBAR OPTIONS
    'DISABLE_PANELS': {'debug_toolbar.panels.redirects.RedirectsPanel'},
    'INSERT_BEFORE': '</body>',
    'RENDER_PANELS': None,
    'RESULTS_CACHE_SIZE': 10,
    'ROOT_TAG_EXTRA_ATTRS': '',
    'SHOW_COLLAPSED': False,
    'SHOW_TOOLBAR_CALLBACK': 'debug_toolbar.middleware.show_toolbar',
    # PANEL OPTIONS
    'EXTRA_SIGNALS': [],
    'ENABLE_STACKTRACES': True,
    'HIDE_IN_STACKTRACES': ('socketserver', 'threading', 'wsgiref', 'debug_toolbar', 'django'),
    'PROFILER_MAX_DEPTH': 10,
    'SHOW_TEMPLATE_CONTEXT': True,
    'SKIP_TEMPLATE_PREFIXES': ('django/forms/widgets/', 'admin/widgets/'),
    'SQL_WARNING_THRESHOLD': 500
}
