#!/usr/bin/env sh

python manage.py makemigrations sais
python manage.py makemigrations student
python manage.py migrate