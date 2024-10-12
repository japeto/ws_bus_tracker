#! /bin/sh

python manage.py makemigrations
python manage.py migrate
python manage.py migrate --run-syncdb

## servidor de producccion
# uvicorn bus_tracker.asgi:application --reload --host 0.0.0.0
# gunicorn bus_tracker.asgi:application --bind=0.0.0.0

# servidor de desarrollo
python manage.py runserver 0.0.0.0:8000