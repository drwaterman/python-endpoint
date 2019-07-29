FROM python:3.6

COPY . /app
WORKDIR /app
RUN pip install --upgrade pip && pip install -r requirements.txt
EXPOSE 5000

ENTRYPOINT gunicorn --workers=2 -k gevent --bind 0.0.0.0:5000 --timeout 360 --log-level=info --preload 'api'
