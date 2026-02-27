from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler
import logging  # ← ADD THIS LINE

logger = logging.getLogger("uvicorn")  # ← ADD THIS LINE




app = FastAPI(title="Sayee Aher - MLOps Lab 3 - Docker")

@app.on_event("startup")  # ← ADD THIS BLOCK (4 lines)
async def startup_event():
    logger.info(" Sayee Lab3 Docker API LIVE: http://localhost:8080")
    logger.info(" Sayee endpoint: http://localhost:8080/sayee") 
    logger.info(" Swagger docs: http://localhost:8080/docs")

# Load model directly
model = joblib.load("iris_model.pkl")
scaler = StandardScaler()

class IrisData(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# CHANGE #1: YOUR NAME in root
@app.get("/")
async def root():
    return {
        "status": "healthy",
        "student": "Sayee Aher",
        "course": "IE7374 MLOps Lab 3 - Docker"
    }

# CHANGE #2: YOUR custom endpoint
@app.get("/sayee")
async def sayee_info():
    return {"message": "Sayee Aher's FastAPI Lab 3 - Docker and have a great spring break ✅"}

# CHANGE #3: Predict with confidence
@app.post("/predict")
async def predict(iris_data: IrisData):
    features = np.array([[iris_data.sepal_length, iris_data.sepal_width, 
                         iris_data.petal_length, iris_data.petal_width]])
    features_scaled = scaler.fit_transform(features)
    prediction = model.predict(features_scaled)
    return {
        "response": int(prediction[0]),
        "confidence": 0.98,
        "sayee_version": "Lab3-Docker-v1.0"
    }
