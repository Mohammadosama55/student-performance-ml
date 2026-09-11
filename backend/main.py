# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# def home():
#     return {"message": "Student Performance API is running"}

# from fastapi import FastAPI
# import joblib

# app = FastAPI()

# # Load the trained ML model
# model = joblib.load("backend/student_score_model.pkl")


# @app.get("/")
# def home():
#     return {"message": "Student Performance API is running"}

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import joblib
import pandas as pd

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load trained model
model = joblib.load("backend/student_score_model.pkl")


# Data we expect from the frontend
class StudentData(BaseModel):
    study_hours: float = Field(ge=0, le=24)
    attendance: float = Field(ge=0, le=100)
    previous_marks: float = Field(ge=0, le=100)
    assignments_completed: float = Field(ge=0, le=10)


@app.get("/")
def home():
    return {"message": "Student Performance API is running"}


@app.post("/predict")
def predict(data: StudentData):

    # Convert API input into DataFrame
    student = pd.DataFrame({
        "study_hours": [data.study_hours],
        "attendance": [data.attendance],
        "previous_marks": [data.previous_marks],
        "assignments_completed": [data.assignments_completed]
    })

    # Make prediction
    prediction = model.predict(student)

    return {
        "predicted_score": prediction[0]
    }