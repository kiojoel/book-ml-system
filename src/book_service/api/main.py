from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from book_service.core import make_prediction, get_recommendations

class BookDataInput(BaseModel):
    num_pages: int
    ratings_count: int
    text_reviews_count: int
    publication_year: float
    language_code: str

class RecommendationInput(BaseModel):
    title: str


app = FastAPI(title="Book Service API")

@app.post("/predict")
def predict(input_data: BookDataInput):
    result = make_prediction(input_data=input_data.dict())
    return result


@app.post("/recommend")
@app.post("/recommend")
def recommend(input_data: RecommendationInput):
    return get_recommendations(title=input_data.title)
