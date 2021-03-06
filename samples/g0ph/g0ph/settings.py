"""
Django settings for g0ph project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$+*4&u7py2s!+_jwmyn8sfle2e%7*$l8$&s$b!753t1gc29nh0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# G0PH-related
WEB_DOMAIN = 'g0ph.com'
DEFAULT_FROM_EMAIL = 'admin@%s' % WEB_DOMAIN


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'nucleo',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'g0ph.urls'

WSGI_APPLICATION = 'g0ph.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

################################################################
# EXTRA SECTIONS
INSTALLED_APPS = list(INSTALLED_APPS)
MIDDLEWARE_CLASSES = list(MIDDLEWARE_CLASSES)

# Django nose tests
# Usage: python manage.py test another.test:TestCase.test_method
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
INSTALLED_APPS.append('django_nose')


# Serve ANGULAR files
STATIC_ROOT = ''
if DEBUG:
    STATIC_URL = '/ng-app/'
else:
    STATIC_URL = '/dist/'

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(__file__), 'ng-app'),
)

#########################################
# BEGIN of `allauth` + `rest-auth`
LOGIN_URL = '/#/login'
LOGOUT_URL = '/#/logout'
LOGIN_REDIRECT_URL = '/'

# 'allauth' + 'rest_auth'
# https://django-allauth.readthedocs.org/en/latest/configuration.html
# http://django-rest-auth.readthedocs.org/en/latest/demo.html
REST_SESSION_LOGIN = False
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# `allauth` requires `django.contrib.sites` framework.
SITE_ID = 3
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
if not DEBUG:
    # Turn off in DEBUG mode.
    ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    )
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                # Already defined Django-related contexts here

                # `allauth` needs this from django
                'django.core.context_processors.request',

                # `allauth` specific context processors
                'allauth.account.context_processors.account',
                'allauth.socialaccount.context_processors.socialaccount',
            ],
        },
    },
]

SOCIALACCOUNT_PROVIDERS = \
    {'facebook':
       {'SCOPE': ['email', 'public_profile', 'user_friends'],
        'AUTH_PARAMS': {},
        'METHOD': 'oauth2',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v2.3'}}

# Modern auth with 3-rd party openauth providers.
INSTALLED_APPS.append('django.contrib.sites')  # required by 'allauth'
INSTALLED_APPS.append('allauth')
INSTALLED_APPS.append('allauth.account')
INSTALLED_APPS.append('allauth.socialaccount')
INSTALLED_APPS.append('allauth.socialaccount.providers.facebook')

# Mobile ready auth
INSTALLED_APPS.append('rest_framework')
INSTALLED_APPS.append('rest_framework.authtoken')
INSTALLED_APPS.append('rest_auth')
INSTALLED_APPS.append('rest_auth.registration')
# END of `allauth` + `rest-auth`
#########################################

#########################################
# BEGIN of CORS (for cordova apps)
# CORS_ORIGIN_WHITELIST = ('127.0.0.1:4400',)
CORS_ORIGIN_WHITELIST = ('localhost:8000', 'g0ph.com')
ALLOWED_HOSTS = ["localhost", "127.0.0.1", 'g0ph.com']
CORS_ALLOW_HEADERS = (
    'x-requested-with',
    'content-type',
    'accept',
    'origin',
    'authorization',
    'x-csrftoken',
    'Api-Authorization',
)
INSTALLED_APPS.append('corsheaders')
MIDDLEWARE_CLASSES.append('corsheaders.middleware.CorsMiddleware')
# END of CORS
#########################################
