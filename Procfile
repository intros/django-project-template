
web: gunicorn  --bind=0.0.0.0:$PORT  {{ project_name }}.wsgi:application  --log-file -
worker: python manage.py celeryd -E -B --loglevel=INFO
