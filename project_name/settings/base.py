# -*- coding: utf-8 -*-
# Django settings for {{ project_name }} project.

import os
import sys
import dj_database_url

import  django.conf.global_settings as DEFAULT_SETTINGS
CURRENT_DIR     = os.path.dirname(__file__)
ENV_PATH        = os.path.abspath("%s/../../" % CURRENT_DIR)
PROJECT_ROOT    = os.path.abspath("%s/../../" % CURRENT_DIR)

#PROJECT_ROOT = os.path.join(os.path.dirname(__file__))
#PROJECT_ROOT = os.path.abspath(os.path.dirname(__name__)) #$os.path.join(os.path.dirname(__file__), '..', '..')

# Modify sys.path to include the lib directory
sys.path.append(os.path.join(PROJECT_ROOT, "lib"))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

# Use environment variables for cool stuff, or hardcode them if that's more your style

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID", False)
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", False)
AWS_SES_REGION_NAME = os.environ.get("AWS_SES_REGION_NAME", "us-east-1")
AWS_SES_REGION_ENDPOINT = os.environ.get("AWS_SES_REGION_ENDPOINT", "email.%s.amazonaws.com" % AWS_SES_REGION_NAME)
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME", "")
AWS_CALLING_FORMAT = os.environ.get("AWS_CALLING_FORMAT", "")

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': '{{ project_name }}',
#        'USER': '{{ project_name }}',
#        'PASSWORD': '{{ project_name }}',
#        'HOST': '',  # Set to empty string for localhost.
#        'PORT': '',  # Set to empty string for default.
#    }
#}

DATABASES = {'default': dj_database_url.config(default='sqlite:///%s' % os.path.join(PROJECT_ROOT, '{{ project_name }}.sqlite'))}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'GMT'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-US'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'data', 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'data','static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'public'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
#    'compressor.finders.CompressorFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', None)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

#    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = '{{ project_name }}.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'classy_mail',
    'compressor',
#    'debug_toolbar',
    'django_mailbox',
    'django_ses',
    'djcelery',
    'djfrontend',
    'djfrontend.skeleton',
    'foundation',
    'social.apps.django_app.default',
    'south',
    'storages',
    'taggit',

    'introductions',

    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'invitation'
)

AUTHENTICATION_BACKENDS = (
    'social.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

EMAIL_SUBJECT_PREFIX = '[{{ project_name }}] '

INTERNAL_IPS = ('127.0.0.1', '10.0.2.2')

# django-debug-toolbar settings
#DEBUG_TOOLBAR_CONFIG = {
#    'INTERCEPT_REDIRECTS': False,
#}

THUMBS_GENERATE_ANY_SIZE = True

# Django-SES
EMAIL_BACKEND = 'django_ses.SESBackend'

#Django-Storages
DEFAULT_FILE_STORAGE = 'libs.storages.S3Storage.S3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

PATH_DATA = os.path.join(PROJECT_ROOT, 'data')
PATH_LOG = os.path.join(PATH_DATA, 'logs')


if not os.path.exists(PATH_LOG):
    os.makedirs(PATH_LOG)

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_false'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        # I always add this handler to facilitate separating loggings
        'file': {
            'level': 'DEBUG',
            'filters': ['require_debug_false'],
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(PATH_LOG, 'app.log'),
            'maxBytes': '16777216', # 16megabytes
            'formatter': 'verbose'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        }
    },
    'loggers': {
        'django': {
            'handlers': ['null'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'core': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True
        }
    },
    # you can also shortcut 'loggers' and just configure logging for EVERYTHING at once
    'root': {
        'handlers': ['file', 'console', 'mail_admins'],
        'level': 'DEBUG',
        'propagate': True
    },
}

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'introductions.pipeline.save_mailbox',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details'
)
FIXTURE_DIRS = 'fixtures/'
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/account/login'
LOGOUT_URL = '/account/logout'

#don't change it, its our default to use allauth django application.
INVITATION_USE_ALLAUTH=True

#Invitation expired days
ACCOUNT_INVITATION_DAYS=10

#Total invitation per user
INVITATIONS_PER_USER=5

# Change to false if application accept a new registration
INVITE_MODE=True

ACCOUNT_ADAPTER = "{{ project_name }}.accountadapter.AccountAdapter"
