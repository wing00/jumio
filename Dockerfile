FROM python:2.7.13
ENV PYTHONUNBUFFERED 1
RUN mkdir /django
WORKDIR /django


ADD requirements.txt /django/
RUN pip install -r requirements.txt

ADD . /django/

ENV DJANGO_SETTINGS_MODULE jumio.settings

EXPOSE 8000

CMD python manage.py collectstatic --noinput
CMD gunicorn jumio.wsgi -b 0.0.0.0:8000