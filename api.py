from fuzzywuzzy import fuzz
from flask_restplus import Api, Resource
from flask import Flask, request, abort, jsonify


def create_app():
    app = Flask(__name__)
    api = Api(app, version=1.0, title="RESTful API", description="Boilerplate Flask API")

    # @api.route("/")
    # def home():
    #     return jsonify({'message': 'OK'}), 200

    @api.route('/health/check')
    class HealthCheck(Resource):
        def get(self):
            return jsonify({'message': 'Up and running'}), 200

    def compare(primary_string, secondary_string):
        """
        Helper method with the scoring logic for the /similarity_score endpoint.
        """
        fuzz_score = fuzz.ratio(primary_string, secondary_string) / 100
        return fuzz_score

    @api.route("/similarity_score", methods=["POST"])
    class SimilarityScore(Resource):
        def post():
            """
            Score the comparison_string for similarity to the others. Can be used for
            comparing company names, sentences, etc. Scale is 0 to 1 (1 is perfect match).

            Parameters
            ----------
            comparison_text:
                String to compare to the other
            text:
                String to compare with

            Returns
            -------
            output_score:
                float from 0 to 1

            """
            if not request.json or not 'comparison_text' in request.json or not 'text' in request.json:
                abort(400)
            comparison_text = request.json['comparison_text']
            text = request.json['text']
            output_score = compare(comparison_text, text)
            return jsonify({'score': output_score}), 200

    @api.route("/metrics", methods=["GET"])
    def metrics():
        """
        Endpoint to get model scores in order to track performance over time.

        Currently has dummy values.
        """
        return jsonify({'Model 1': 10,
                        'Model 2': 100,
                        'Model 3': 1000}), 200

    return app


application = create_app()


if __name__ == "__main__":
    application.run(debug=True)
