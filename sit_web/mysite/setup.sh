#!/bin/sh
python manage.py makemigrations polls
python manage.py migrate
sh adaugaWordpairs.sh
python manage.py runserver
