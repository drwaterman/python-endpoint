from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"health": "OK"}


def test_read_metrics():
    response = client.get("/metrics")
    assert response.status_code == 200
    assert response.json() == {'Model 1': 10,
                               'Model 2': 100,
                               'Model 3': 1000}


def test_similarity_score():
    response = client.post(
        "/similarity_score",
        json={"comparison_text": "Hello test!", "text": "Help toast."},
    )
    assert response.status_code == 200
    assert list(response.json().keys()) == ['score']
    assert all(isinstance(x, float) for x in response.json().values())

