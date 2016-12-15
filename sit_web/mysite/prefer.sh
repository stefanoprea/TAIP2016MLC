#!/bin/sh
python manage.py shell -c "from prefer import prefer;prefer('$1')"
