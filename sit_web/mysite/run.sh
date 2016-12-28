#!/bin/sh

python2 manage.py makemigrations polls
python2 manage.py migrate
python2 manage.py runserver 0.0.0.0:80
