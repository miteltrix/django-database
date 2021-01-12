#!/bin/sh

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --no-input

gunicorn database.asgi:application -k uvicorn.workers.UvicornWorker -b 0.0.0.0
