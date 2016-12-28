#!/bin/sh
python2 manage.py makemigrations polls
python2 manage.py migrate
sh addWordpairsToDatabase.sh
python2 manage.py runserver
