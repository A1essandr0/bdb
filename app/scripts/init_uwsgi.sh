#!/usr/bin/env bash

# +Проверка на то, собрана ли уже статика
python3 /apps/bdb/manage.py collectstatic
python3 /apps/bdb/manage.py migrate
python3 /apps/bdb/manage.py loaddata /apps/bdb/bdb_small.json 

chown www-data /tmp 
chown www-data /apps/bdb/instance/bdb.sqlite
chown www-data /apps/bdb/instance

uwsgi --emperor /apps-conf --uid www-data --gid www-data --master
