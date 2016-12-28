#!/bin/sh
CODE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd ${CODE_DIR}
python2 manage.py makemigrations polls
python2 manage.py migrate
python2 manage.py runserver 0.0.0.0:80
