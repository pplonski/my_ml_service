#!/usr/bin/env bash

echo "Starting backend django server"
until cd /app/backend/server
do
    echo "Waiting for server volume..."
done

echo "Running manage.py migrate"
until ./manage.py migrate
do
    echo "Waiting for database to be ready..."
    sleep 2
done

echo "Running manage.py collectstatic"
./manage.py collectstatic --noinput

echo "Running manage.py gunicorn on port 8000"
gunicorn server.wsgi --bind :8000 --workers 4 --threads 4
