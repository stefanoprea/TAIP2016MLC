#!/bin/sh
python manage.py makemigrations polls
python manage.py migrate
sh addWordpairsToDatabase.sh
python manage.py runserver
