import django_heroku

from .base import *
from django.conf import settings


DEBUG = False

ALLOWED_HOSTS = [
    'https://e1337ist.herokuapp.com',

]

CORS_ALLOWED_ORIGINS = [
    # add frontend website here
    'https://1337link.netlify.app'

]

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

# heroku settings
DEBUG_PROPAGATE_EXCEPTIONS = True

django_heroku.settings(locals())

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"