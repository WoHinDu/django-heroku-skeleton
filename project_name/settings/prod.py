"""
Django production settings for {{ project_name }} project.
"""

from os import environ
from django.utils.crypto import get_random_string
import dj_database_url
from .base import *

##########
# Secret key setting
# SECURITY WARNING: keep the secret key used in production secret!
# See: https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#secret-key

SECRET_KEY = environ.get('SECRET_KEY', get_random_string(50, 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'))

##########


##########
# Debug setting
# SECURITY WARNING: don't run with debug turned on in production!
# See: https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#debug

DEBUG = False

##########


##########
# Allowed hosts setting
# See: https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#allowed-hosts
# e.g. ALLOWED_HOSTS = ['.myproject.herokuapp.com']

ALLOWED_HOSTS = [] # Replace

##########


##########
# WSGI application setting
# See: https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#wsgi-application

WSGI_APPLICATION = '{{ project_name }}.wsgi.prod.application'

##########


##########
# Database setting
# See: https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#databases
# See: https://devcenter.heroku.com/articles/django-app-configuration#database-configuration

DATABASES = {
	'default': dj_database_url.config(conn_max_age=500),
}

##########


##########
# WhiteNoise settings
# See: http://whitenoise.evans.io/en/stable/

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

WHITENOISE_MIDDLEWARE = [
	'whitenoise.middleware.WhiteNoiseMiddleware',
]

##########


##########
# Sentry settings
# See: https://docs.sentry.io/clients/python/integrations/django/

RAVEN_CONFIG = {
	'dsn': environ.get('SENTRY_DSN', None),
}

INSTALLED_APPS += (
	'raven.contrib.django.raven_compat',
)

SENTRY_MIDDLEWARE = [
	'raven.contrib.django.raven_compat.middleware.SentryResponseErrorIdMiddleware',
	'raven.contrib.django.raven_compat.middleware.Sentry404CatchMiddleware',
]

##########


##########
# SSL settings
# See: https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#secure-proxy-ssl-header

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SECURE_SSL_REDIRECT = True

##########


##########
# Email settings
# See: https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#email

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.sendgrid.net'

EMAIL_HOST_USER = os.environ.get('SENDGRID_USERNAME')

EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_PASSWORD')

EMAIL_PORT = 25

EMAIL_USE_TLS = False # Sendgrid uses automatically TLS if recipient supports it

SERVER_EMAIL = 'info@myproject.tld' # Replace

DEFAULT_FROM_EMAIL = SERVER_EMAIL

EMAIL_SUBJECT_PREFIX = '[myproject] ' # Replace

ADMINS = MANAGER = []

##########


##########
# Middleware setting
# See: https://docs.djangoproject.com/en/{{ docs_version }}/topics/http/middleware/

MIDDLEWARE = SENTRY_MIDDLEWARE + [
	'django.middleware.security.SecurityMiddleware',
	] + WHITENOISE_MIDDLEWARE + [
	'whitenoise.middleware.WhiteNoiseMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

##########


##########
# Logging settings
# See: https://docs.djangoproject.com/en/{{ docs_version }}/topics/logging/

LOGGING = {
	'version': 1,
	'disable_existing_loggers': True,
	'root': {
		'level': 'WARNING',
		'handlers': ['sentry'],
	},
	'formatters': {
		'verbose': {
			'format': '%(levelname)s %(asctime)s %(module)s '
					  '%(process)d %(thread)d %(message)s'
		},
	},
	'handlers': {
		'sentry': {
			'level': 'ERROR', # To capture more than ERROR, change to WARNING, INFO, etc.
			'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
			'tags': {'custom-tag': 'x'},
		},
		'console': {
			'level': 'DEBUG',
			'class': 'logging.StreamHandler',
			'formatter': 'verbose'
		}
	},
	'loggers': {
		'myapp': { # Replace
			'level': 'INFO',
			'handlers': ['console'],
			'propagate': True,
		},
		'django.db.backends': {
			'level': 'ERROR',
			'handlers': ['console'],
			'propagate': False,
		},
		'raven': {
			'level': 'DEBUG',
			'handlers': ['console'],
			'propagate': False,
		},
		'sentry.errors': {
			'level': 'DEBUG',
			'handlers': ['console'],
			'propagate': False,
		},
	},
}

##########
