# -*- coding: utf-8 -*-

from .base import *

DEBUG = True
# INSTALLED_APPS = list(INSTALLED_APPS) + ['devserver']

# Django-SES
#EMAIL_BACKEND = 'django_ses.SESBackend'
# These are optional -- if they're set as environment variables they won't
# need to be set here as well
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


try:
    from .local import *
except ImportError:
    pass
