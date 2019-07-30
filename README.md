# python-endpoint: A minimal scaffolding for creating REST endpoints using Python, Flask, and Docker

## Basic Use

`api.py` is the Python script that defines the endpoint(s). Logic can be in api.py, or it can be imported from other Python modules if more complexity is required.

To start the REST server in dev mode, run:

```
python api.py
```

This will start a server on port 5000. Navigate your browser to http://localhost:5000/
and the hard-coded response should appear.

To try out the `/similarity_score` POST endpoint, you can use `curl` or the Python `requests` library, e.g.:

```python
r = requests.post('http://0.0.0.0:5000/similarity_score', 
                  json={'comparison_text': 'Hello World', 'text': 'Hrllo Wrrld'})
```


## Testing

Ensure test libraries are installed from `requirements.txt`.

Then, ensure the tests pass by running:

```
pytest
```

## Production

So far, we've only used the dev/test server built in to `flask`. 
To deploy on a production-grade wsgi webserver,
we will use `gunicorn`. `gunicorn` is avaliable to install via `pip` and
is listed in `requirements.txt`.

To run on the command-line:

```
gunicorn -k gevent -b 0.0.0.0:5000 api
```

## Docker for Deployment
This module also contains a Dockerfile that can be used to build an image that automates running the REST server. It installs all the required libraries and starts `gunicorn`, on port 5000. You need to expose port 5000 to access it from the host machine.
