import pytest
from api import create_app


@pytest.fixture
def app():
    app = create_app()
    return app


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200


def test_metrics(client):
    response = client.get("/metrics")
    assert response.status_code == 200
    assert response.json == {'Model 1': 10, 'Model 2': 100, 'Model 3': 1000}


def test_similarity_score(client):
    comparison_string = 'Hello World.'
    strings = [{'id': 1, 'body': 'Hello Wrrld.'},
               {'id': 2, 'body': 'H3ll0 W0rld#'},
               {'id': 3, 'body': 'Heck no dog.'},
               ]

    for string in strings:
        response = client.post("/similarity_score",
                               json={'comparison_text': comparison_string, 'text': string['body']})
        assert response.status_code == 200
        score = response.json['score']
        assert isinstance(score, float)
        assert 0 <= score <= 1
