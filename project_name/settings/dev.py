"""
Django development settings for {{ project_name }} project.
"""

from .base import *
from django.utils.crypto import get_random_string

##########
# Secret key setting
# SECURITY WARNING: keep the secret key used in production secret!
# See: https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#secret-key

SECRET_KEY = get_random_string(50, 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)')

##########


##########
# Debug setting
# SECURITY WARNING: don't run with debug turned on in production!
# See: https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#debug

DEBUG = True

##########


##########
# WSGI application setting
# See: https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#wsgi-application

WSGI_APPLICATION = '{{ project_name }}.wsgi.dev.application'

##########


##########
# Database setting
# See: https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	}
}

##########


##########
# Django Debug Toolbar settings
# See: http://django-debug-toolbar.readthedocs.io/en/stable/

INSTALLED_APPS += [
	'debug_toolbar',
]

INTERNAL_IPS = ['127.0.0.1']

DEBUGTOOLBAR_MIDDLEWARE = [
	'debug_toolbar.middleware.DebugToolbarMiddleware',
]

##########


##########
# Middleware setting
# See: https://docs.djangoproject.com/en/{{ docs_version }}/topics/http/middleware/

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
] + DEBUGTOOLBAR_MIDDLEWARE

##########

##########
# Email setting 
# See: https://docs.djangoproject.com/en/{{ docs_version }}/topics/email/#email-backends

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

##########


##########
# Logging settings
# See: https://docs.djangoproject.com/en/{{ docs_version }}/topics/logging/

LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'handlers': {
		'console': {
			'level': 'DEBUG',
			'class': 'logging.StreamHandler',
		},
	},
	'loggers': {
		'myapp': { # Replace
			'handlers': ['console'],
			'propagate': True,
		}
	}
}

##########
