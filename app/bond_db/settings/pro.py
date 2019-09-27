from .base import *
import os

DEBUG = False

assert SECRET_KEY is not None, ('Provide DJANGO_SECRET_KEY')

ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS += [os.getenv('DJANGO_ALLOWED_HOSTS'),]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DJANGO_DB_NAME'),
        'USER': os.getenv('DJANGO_DB_USER'),
        'PASSWORD': os.getenv('DJANGO_DB_PASSWORD'),
        'HOST': os.getenv('DJANGO_DB_HOST'),
        'PORT': os.getenv('DJANGO_DB_PORT'),
    }
}

#SECURE_SSL_REDIRECT = True
#CSRF_COOKIE_SECURE = True
