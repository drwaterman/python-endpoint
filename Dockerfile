FROM python:3.7

COPY . /app
WORKDIR /app
RUN pip install --upgrade pip && pip install -r requirements.txt
EXPOSE 8000

ENTRYPOINT gunicorn --workers=2 -k gevent --bind 0.0.0.0:8000 --timeout 360 --log-level=info --preload 'api:__hug_wsgi__'
