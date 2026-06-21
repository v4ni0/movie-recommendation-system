from fastapi.params import Query
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


from src.service.recommender import MovieRecommender
from src.config import TOP_K

class RecommendationRequest(BaseModel):
    description: str
    top_k: int = TOP_K

class RecommendationResponse(BaseModel):
    id: int
    title: str
    score: float

app = FastAPI(
    title="Movie Recommendation System API",
    description="An API for recommending movies based on user description.",
)

recommender = MovieRecommender()

@app.get("/recommend")
def get_recommendations(description: str = Query(...), top_k: int = TOP_K):
    try:
        recommendations = recommender.recommend(description, top_k)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"recommendations": recommendations}

def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
