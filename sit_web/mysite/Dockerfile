FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
ADD requirements.txt /code/
RUN pip install -r /code/requirements.txt
COPY polls/ /code/polls
COPY mysite/ /code/mysite
VOLUME ["/code/data"]
COPY manage.py run.sh /code/
