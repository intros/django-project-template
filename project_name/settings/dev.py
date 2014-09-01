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


try:
    from .local import *
except ImportError:
    pass
