#!/bin/bash 
NAME="apiBomberosUubr"
DJANGODIR=$(dirname $(cd `dirname $0` && pwd))
SOCKFILE=/tmp/gunicorn-apiBomberosUubr.sock
LOGDIR=${DJANGODIR}/logs/gunicorn.log
USER=nur
GROUP=nur
NUM_WORKERS=5
DJANGO_WSGI_MODULE=backend.wsgi
rm -frv $SOCKFILE
echo $DJANGODIR
cd $DJANGODIR
exec ${DJANGODIR}/env/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
--name $NAME \
--workers $NUM_WORKERS \
--user=$USER --group=$GROUP \
--bind=unix:$SOCKFILE \
--log-level=debug \
--log-file=$LOGDIR
