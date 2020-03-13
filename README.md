# python-endpoint: A minimal scaffolding for creating REST endpoints using Python, FastAPI, and Docker

## Basic Use

`main.py` is the Python script that defines the endpoint(s). Logic can be in main.py, or it can be imported from other Python modules if more complexity is required.

To start the REST server in dev mode, run:

```
uvicorn main:app --reload
```

This will start a server on port 8000. Navigate your browser to http://localhost:8000/docs
and documentation of the endpoints appears.

To try out the POST endpoint, you can use `curl` or the Python `requests` library.


## Testing

Testing uses the `pytest` library. Run the tests pass from the project directory by running:

```
pytest
```

## Production

This module contains a Dockerfile that can be used to build an image that automates running the REST server. It installs all the required libraries and starts `gunicorn`, on port 80. You need to expose port 80 to access it from the host machine.
`gunicorn` is a production-grade wsgi webserver.

An example of how to build the Docker image and run it:

```
docker build -t python-endpoint .
docker run -d --name endpoint1 -p 80:80 python-endpoint
```

This will start the container detached (in the background) and set up port forwarding on port 80. Now you can access it directly at http://localhost/ or get the OpenAPI spec at http://localhost/docs/
