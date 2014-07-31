cd /opt/apps/djdocker && /opt/ve/djdocker/bin/python manage.py syncdb --noinput
cd /opt/apps/djdocker && /opt/ve/djdocker/bin/python manage.py collectstatic --noinput
supervisord -c /opt/supervisor.conf -n
