# -*- coding: utf-8 -*-

from .base import *

DEBUG = False

#MYSQL
#DATABASES = {'default': dj_database_url.config(default='mysql://{{project_name}}:{{project_name}}@localhost:3306/{{ project_name }}')}

#POSTGRES
#DATABASES = {'default': dj_database_url.config(default='postgres://{{project_name}}:{{project_name}}@localhost:5432/{{ project_name }}')}

try:
    from .local import *
except ImportError:
    pass
