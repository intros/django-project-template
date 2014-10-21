web: gunicorn {{ project_name }}.wsgi:application
worker: python manage.py celeryd -E -B --loglevel=INFO
