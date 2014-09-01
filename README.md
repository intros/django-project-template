django-project-template
=======================

The project template for creating new instances of the intros application

## Prerequisites ##

- python >= 2.7
- django >= 1.5 to support (custom-project-templates)[https://docs.djangoproject.com/en/dev/ref/django-admin/#startproject-projectname-destination]
- virtualenv/wrapper (optional)

## Usage ##

### Use Vagrant.  It's better! ###
[Vagrant](http://vagrantup.com) does virtual machines.  You might need to also install [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
```shell

django-admin.py startproject --template https://github.com/intros/django-project-template/zipball/master --name templates/partials/header.html --name=provision_vagrant.sh intros

vagrant up
vagrant ssh

```

### Create the project locally ###

```shell

django-admin.py startproject --template https://github.com/intros/django-project-template/zipball/master --name templates/partials/header.html --name=provision_vagrant.sh intros
cd intros
pip install -r requirements.txt

```

### Update the configuration ###

In ````intros/settings/base.py```` update settings for secret keys:
```python

# Use environment variables for cool stuff, or hardcode them if that's more your style 

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID", False)
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", False)
AWS_SES_REGION_NAME = os.environ.get("AWS_SES_REGION_NAME", "us-east-1")
AWS_SES_REGION_ENDPOINT = os.environ.get("AWS_SES_REGION_ENDPOINT", "email.%s.amazonaws.com" % AWS_SES_REGION_NAME)
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME", "")
AWS_CALLING_FORMAT = os.environ.get("AWS_CALLING_FORMAT", "")

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

