FROM debian:wheezy
MAINTAINER Alex Lovell-Troy "alex@lovelltroy.org"

RUN apt-get -qq update
# Get the general dependencies
RUN apt-get install -y python-dev python-setuptools supervisor git-core nginx 
# Get the database you need
RUN apt-get install -y mysql-server mysql-client libmysqlclient-dev
RUN apt-get install -y python-psycopg2
RUN apt-get install -y sqlite3

# PIL imaging support
RUN apt-get install -y libtiff4-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.5-dev tk8.5-dev python-tk

RUN easy_install pip
RUN pip install virtualenv
RUN pip install uwsgi

RUN virtualenv --no-site-packages /opt/ve/djdocker

ADD . /opt/apps/djdocker
ADD docker/supervisor.conf /opt/supervisor.conf
ADD docker/run.sh /usr/local/bin/run

#RUN (cd /opt/apps/djdocker && git remote rm origin)
#RUN (cd /opt/apps/djdocker && git remote add origin https://github.com/kencochrane/django-docker.git)
#
# database binaries anyone?
RUN /opt/ve/djdocker/bin/pip install -r /opt/apps/djdocker/requirements.txt
# Moved to run.sh
#RUN (cd /opt/apps/djdocker && /opt/ve/djdocker/bin/python manage.py syncdb --noinput)
#RUN (cd /opt/apps/djdocker && /opt/ve/djdocker/bin/python manage.py collectstatic --noinput)

EXPOSE 8000

CMD ["/bin/sh", "-e", "/usr/local/bin/run"]
