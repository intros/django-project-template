#!/bin/bash
echo "I am setting things up within Vagrant..."
apt-get update
echo "Installing postgres and mysql because you might have a different preference than I do"
debconf-set-selections <<< 'mysql-server-5.5 mysql-server/root_password password password'
debconf-set-selections <<< 'mysql-server-5.5 mysql-server/root_password_again password password'
apt-get install -y libmysqlclient-dev mysql-server-5.5 postgresql python-dev python-pip screen vim-nox zsh
mysqladmin -u root --password=password create {{ project_name }}
mysql -u root --password=password -e "GRANT ALL ON {{ project_name }}.* TO '{{ project_name }}'@'localhost' IDENTIFIED BY '{{ project_name }}';"
cd /vagrant
./provision.sh
date > /etc/vagrant_provisioned_at
