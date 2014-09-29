web: gunicorn_django --workers=4 --bind=0.0.0.0:$PORT {{ project_name }}/{{ project_name }}/settings
worker: python {{ project_name }}/manage.py celeryd -E -B --loglevel=INFO
