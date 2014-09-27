# -*- coding: utf-8 -*-

import os
from .base import *

DEBUG = True
# INSTALLED_APPS = list(INSTALLED_APPS) + ['devserver']

# Django-SES
#EMAIL_BACKEND = 'django_ses.SESBackend'
# These are optional -- if they're set as environment variables they won't
# need to be set here as well
# Override these here if you need to.  The defaults are loaded in base.py
#AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID", False)
#AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", False)
#AWS_SES_REGION_NAME = os.environ.get("AWS_SES_REGION_NAME", "us-east-1")
#AWS_SES_REGION_ENDPOINT = os.environ.get("AWS_SES_REGION_ENDPOINT", "email.%s.amazonaws.com" % AWS_SES_REGION_NAME)

#AWS_ACCESS_KEY_ID = 'YOUR-ACCESS-KEY-ID'
#AWS_SECRET_ACCESS_KEY = 'YOUR-SECRET-ACCESS-KEY'
# Additionally, you can specify an optional region, like so:
AWS_SES_REGION_NAME = 'us-east-1'
AWS_SES_REGION_ENDPOINT = 'email.us-east-1.amazonaws.com'

# Django Storages S3
#AWS_ACCESS_KEY_ID
#AWS_SECRET_ACCESS_KEY
#AWS_STORAGE_BUCKET_NAME
#AWS_CALLING_FORMAT
AWS_HEADERS = {
    'Cache-Control': 'max-age=86400',
}

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
STATICFILES_STORAGE = 'django.core.files.storage.FileSystemStorage'

# For database settings, the environment value with key "DATABASE_URL" will override all the settings.
#MYSQL
# the format for url: mysql://USERNAME:PASSWORD@HOST:PORT/DB_NAME
# the default:
# HOST: localhost
# PORT: 3306
# USER: {{ project_name }}
# PASSWORD: {{ project_name }}
# DB: {{ project_name }}
# Uncomment this line for override the setings with mysql.
#DATABASES = {'default': dj_database_url.config(default='mysql://{{project_name}}:{{project_name}}@localhost:3306/{{ project_name }}')}

#POSTGRES
# the format for url: postgres://USERNAME:PASSWORD@HOST:PORT/DB_NAME
# the default:
# HOST: localhost
# PORT: 5432
# USER: {{ project_name }}
# PASSWORD: {{ project_name }}
# DB: {{ project_name }}
# Uncomment this line for override the setings with mysql.
#DATABASES = {'default': dj_database_url.config(default='postgres://{{project_name}}:{{project_name}}@localhost:5432/{{ project_name }}')}


#SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '744922538552-od4jnjterqva46ajonad16ifc14ukm1n.apps.googleusercontent.com'
#SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '92rgzii0Mtxoc9O0Aqqdtsgq'
#SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ['https://mail.google.com']

try:
    from .local import *
except ImportError:
    pass
