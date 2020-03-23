FROM python

ENV DJANGO_SETTINGS_MODULE=bond_db.settings.local
ENV DJANGO_SECRET_KEY=abracadabra

RUN mkdir /apps-conf
RUN mkdir /apps
COPY /app /apps/bdb
COPY config/bdb.ini /apps-conf
COPY requirements.txt /apps-conf
RUN pip3 install -r /apps-conf/requirements.txt

EXPOSE 5000
CMD bash /apps/bdb/scripts/init_uwsgi.sh
