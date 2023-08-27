from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbempleado',
        'USER': 'cas',
        'PASSWORD': '12345',
        'HOST': 'localhost',
        'PORT':'5432',
    }
}


STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR.joinpath('static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.joinpath('media')