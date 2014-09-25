# -*- coding: utf-8 -*-

from .base import *

DEBUG = False

# based on 12factor, enviroment variable will take the higher priority
#For database settings, the environment value with key "DATABASE_URL" will override all the settings.

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

try:
    from .local import *
except ImportError:
    pass
