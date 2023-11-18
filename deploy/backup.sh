#!/bin/bash

export FECHA=`date +%d_%m_%Y_%H_%M_%S`
export NAME=backup_${FECHA}.dump
export DIR=/home/nur/backup/
USER_DB=postgres
NAME_DB=apibomberosuubr
cd $DIR
> ${NAME}
export PGPASSWORD=postgres
chmod 777 ${NAME}
echo "Procesando la Copia de la Base de Datos"
pg_dump -U $USER_DB -h localhost --port 5432 -f ${NAME} $NAME_DB
echo "Backup Terminado"
