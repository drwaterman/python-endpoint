from fuzzywuzzy import fuzz
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class ComparisonQuery(BaseModel):
    comparison_text: str
    text: str


def compare(primary_string, secondary_string):
    """
    Helper method with the scoring logic for the /similarity_score endpoint.
    """
    fuzz_score = fuzz.ratio(primary_string, secondary_string)/100
    return fuzz_score


@app.get("/")
async def root():
    return {"health": "OK"}


@app.post("/similarity_score")
def similarity_score(query: ComparisonQuery):
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
    output_score = compare(query.comparison_text, query.text)
    return {"score": output_score}


@app.get("/metrics")
def metrics():
    """
    Endpoint to get model scores in order to track performance over time.

    Currently has dummy values.
    """
    return {'Model 1': 10,
            'Model 2': 100,
            'Model 3': 1000}
