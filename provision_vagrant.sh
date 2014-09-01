#!/bin/bash
echo "I am provisioning..."
apt-get update
echo "Installing postgres and mysql because you might have a different preference than I do"
debconf-set-selections <<< 'mysql-server-5.5 mysql-server/root_password password password'
debconf-set-selections <<< 'mysql-server-5.5 mysql-server/root_password_again password password'
apt-get install -y libmysqlclient-dev mysql-server postgresql python-dev python-pip screen vim-nox zsh
cd /vagrant
pip install -r requirements.txt
date > /etc/vagrant_provisioned_at
