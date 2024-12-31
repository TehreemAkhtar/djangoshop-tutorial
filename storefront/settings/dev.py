from .common import *


DEBUG = True
SECRET_KEY = 'django-insecure-jb^7mq5ox5e6^u!-=ppu#$3+eb&+qw54ps--seotfit7zikatv'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storefront3',
        'USER': 'root',
        'PASSWORD': 'root_123',
    }
}