FROM python:2.7.13
ENV PYTHONUNBUFFERED 1
RUN mkdir /django
WORKDIR /django


ADD requirements.txt /django/
RUN pip install -r requirements.txt

ADD . /django/

ENV DJANGO_SETTINGS_MODULE jumio.settings
ENV DOCKER_HOST db