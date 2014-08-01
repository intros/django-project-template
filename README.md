django-project-template
=======================

The project template for creating new instances of the intros application

## Prerequisites ##

- python >= 2.7
- django >= 1.5 to support (custom-project-templates)[https://docs.djangoproject.com/en/dev/ref/django-admin/#startproject-projectname-destination]
- virtualenv/wrapper (optional)

## Usage ##

### Create the project locally ###

```shell

django-admin.py startproject --template https://github.com/intros/django-project-template/zipball/master intros
cd intros
pip install -r requirements.txt

```

### Update the configuration ###

In ````intros/settings/dev.py```` update settings for secret keys:
```python

# Django-SES
#EMAIL_BACKEND = 'django_ses.SESBackend'
# These are optional -- if they're set as environment variables they won't
# need to be set here as well
AWS_ACCESS_KEY_ID = 'YOUR-ACCESS-KEY-ID'
AWS_SECRET_ACCESS_KEY = 'YOUR-SECRET-ACCESS-KEY'
# Additionally, you can specify an optional region, like so:
AWS_SES_REGION_NAME = 'us-east-1'
AWS_SES_REGION_ENDPOINT = 'email.us-east-1.amazonaws.com'

# Django Storages S3
AWS_ACCESS_KEY_ID = 'YOUR-ACCESS-KEY-ID'
AWS_SECRET_ACCESS_KEY = 'YOUR-SECRET-ACCESS-KEY'
AWS_STORAGE_BUCKET_NAME = ''
AWS_CALLING_FORMAT = ''

```

### Create the databases ###

```shell

# models without South
python manage.py syncdb

# models with South
python manage.py migrate

```

### Run the server ###

```shell

python manage.py runserver
```

