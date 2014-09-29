#!/bin/bash
echo "I am provisioning..."
mkdir -p data/logs
pip install -r requirements.txt
python manage.py syncdb --noinput
python manage.py migrate
python manage.py collectstatic --noinput
