from .base import *
from django.conf import settings

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'e1337ist.herokuapp.com',
]

INSTALLED_APPS += [
    'debug_toolbar',
]

if DEBUG:
    MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'lello',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:8000',
    'http://localhost:8000',
    'http://127.0.0.1:3000',
    'http://localhost:3000',
]


INTERNAL_IPS = [
    '127.0.0.1',
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"