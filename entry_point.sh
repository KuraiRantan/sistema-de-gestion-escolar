#!/bin/sh

# Instalar requisitos
pip3 install -r ./applications/SGE/requirements.txt

# Ejecutar migraciones de la base de datos
cd ./applications/SGE
python -m alembic upgrade head

# Iniciar la aplicación
cd ../..
./web2py.py -i 0.0.0.0 -a "${PASSWORD_ADMIN_SERVER}" -c ./ssl/server.crt -k ./ssl/server.key
