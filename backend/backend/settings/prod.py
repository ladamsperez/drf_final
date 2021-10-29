import django_heroku

from .base import *
from django.conf import settings


DEBUG = False

ALLOWED_HOSTS = [
    'e1337ist',
    'localhost',
]

CORS_ALLOWED_ORIGINS = [
    # add frontend website here
    'https://1337logs.netlify.app',
    'https://1337logs.com',
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

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# heroku settings
DEBUG_PROPAGATE_EXCEPTIONS = True

django_heroku.settings(locals())