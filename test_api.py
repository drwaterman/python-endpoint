def test_similarity_score():
    comparison_string = 'Hello World.'
    strings = [{'id': 1, 'body': 'Hello Wrrld.'},
               {'id': 2, 'body': 'H3ll0 W0rld#'},
               {'id': 3, 'body': 'Heck no dog.'},
               ]

    for string in strings:
        response = requests.post('http://0.0.0.0:5000/similarity_score',
                                 json={'comparison_text': comparison_string, 'text': string})
        assert response.status_code == 200
        score = response.json()['score']
        assert isinstance(score, float)
        assert 0 <= score <= 1


if __name__ == "__main__":
    test_similarity_score()
