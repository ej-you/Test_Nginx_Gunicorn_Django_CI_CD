#!/bin/sh

cd /app/HelloWorld

python3 manage.py migrate --no-input
python3 manage.py collectstatic --no-input

gunicorn HelloWorld.wsgi --workers=3 --bind 0.0.0.0:8080
