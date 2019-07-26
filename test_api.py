import hug
import api


def test_similarity_score():
    comparison_string = 'Hello World.'
    strings = [{'id': 1, 'body': 'Hello Wrrld.'},
               {'id': 2, 'body': 'H3ll0 W0rld#'},
               {'id': 3, 'body': 'Heck no dog.'},
               ]

    for string in strings:
        response = hug.test.post(api, 'similarity_score',
                                 {'comparison_text': comparison_string, 'text': string['body']})
        assert response.status == '200 OK'
        score = response.data
        assert isinstance(score, float)
        assert 0 <= score <= 1


if __name__ == "__main__":
    test_similarity_score()
