#!/bin/bash

NAME="pyfva"
DJANGO_SETTINGS_MODULE=settings             # which settings file should Django use
DJANGO_WSGI_MODULE=wsgi                     # WSGI module name
NUM_WORKERS=3
LOGDIR=/var/log/pyfva
CERTSDIR=`pwd`/../certs
test -d $LOGDIR || $(sudo mkdir -p $LOGDIR &&  sudo chown $USER $LOGDIR)

code=`pwd`/../
export PYTHONPATH=$PYTHONPATH:$code
export REQUESTS_CA_BUNDLE=$CERTSDIR/ca_nacional_de_CR.pem
export REQUESTS_CA_PATH=$CERTSDIR/ca_nacional_de_CR.pem
export REQUESTS_CERT_PATH=$CERTSDIR/bccr_agent.pem
export REQUESTS_KEY_PATH=$CERTSDIR/bccr_agent_key.pem
export STUB_SCHEME='https'
export STUB_HOST="firmadorexterno.bccr.fi.cr"


python manage.py createcachetable
gunicorn -c gunicorn_conf.py ${DJANGO_WSGI_MODULE}:application

#gunicorn ${DJANGO_WSGI_MODULE}:application \
#  --name $NAME  --timeout 180 \
#  --workers $NUM_WORKERS \
#  --bind=0.0.0.0:8443 \
#  --do-handshake-on-connect \
#  --ssl-version=TLSv1_2 \
#  --ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-SHA256:AES256-GCM-SHA384:AES256-SHA256:AES128-SHA256 \
#  --log-level=debug \
#  --access-logfile=$LOGDIR/access_gunicorn.log \
#  --log-file=$LOGDIR/gunicorn.log \
#  --keyfile $REQUESTS_KEY_PATH \
#  --certfile $REQUESTS_CERT_PATH \
#  --ca-certs $REQUESTS_CA_PATH
