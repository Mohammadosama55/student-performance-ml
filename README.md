# 🎓 Student Performance Predictor

> An end-to-end Machine Learning web application that predicts a student's final score using study habits and academic performance data.

## 🌐 Live Demo

**Try the application:**  
https://student-performance-ml-2d8v.onrender.com

---

## 📌 About the Project

Student Performance Predictor is a beginner-friendly end-to-end Machine Learning project.

The ML model is trained using Python and Scikit-learn, saved as a `.pkl` file, served through a FastAPI backend, and connected to a simple HTML/CSS/JavaScript frontend.

The project demonstrates the complete journey from:

**Data → Model Training → Model Saving → API → Frontend → Deployment**

---

## ✨ Features

- Predict a student's final score
- Uses four student-performance features:
  - Study Hours
  - Attendance
  - Previous Marks
  - Assignments Completed
- Linear Regression Machine Learning model
- FastAPI REST API
- Input validation with Pydantic
- Simple HTML/CSS/JavaScript frontend
- CORS support for frontend-backend communication
- Deployed online using Render

---

## 🧠 Machine Learning

### Input Features

| Feature | Description |
|---|---|
| `study_hours` | Number of hours spent studying |
| `attendance` | Attendance percentage |
| `previous_marks` | Previous academic marks |
| `assignments_completed` | Number of completed assignments |

### Target

```text
final_score
```

The model uses **Linear Regression** from Scikit-learn.

### Model Evaluation

For the learning dataset used in this project:

- **MAE:** ~0.48
- **R²:** ~0.9992

> ⚠️ These results should not be interpreted as real-world model accuracy. The dataset is small and artificially created for learning the end-to-end ML workflow.

---

## 🏗️ Project Architecture

```text
                    Student Input
                         │
                         ▼
              HTML / CSS / JavaScript
                         │
                         │ POST /predict
                         ▼
                    FastAPI API
                         │
                         ▼
                Pydantic Validation
                         │
                         ▼
              Trained ML Model (.pkl)
                         │
                         ▼
                 Predicted Score
                         │
                         ▼
                  Frontend Result
```

---

## 📁 Project Structure

```text
student-performance-ml/
│
├── backend/
│   ├── main.py
│   └── student_score_model.pkl
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🛠️ Tech Stack

### Machine Learning
- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib

### Backend
- FastAPI
- Pydantic
- Uvicorn

### Frontend
- HTML5
- CSS3
- JavaScript
- Fetch API

### Deployment
- Render
- GitHub

---

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd student-performance-ml
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the FastAPI server

```bash
uvicorn backend.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

FastAPI documentation:

```text
http://127.0.0.1:8000/docs
```

### 5. Open the frontend

Open:

```text
frontend/index.html
```

in your browser.

---

## 🔌 API

### Health Check

```http
GET /
```

Response:

```json
{
  "message": "Student Performance API is running"
}
```

### Prediction

```http
POST /predict
```

Example request:

```json
{
  "study_hours": 7,
  "attendance": 85,
  "previous_marks": 75,
  "assignments_completed": 9
}
```

Example response:

```json
{
  "predicted_score": 78.85
}
```

---

## 🔄 Machine Learning Workflow

```text
1. Create student dataset
        ↓
2. Explore data using Pandas
        ↓
3. Separate features (X) and target (y)
        ↓
4. Split data into training and testing sets
        ↓
5. Train Linear Regression model
        ↓
6. Evaluate using MAE and R²
        ↓
7. Save model using Joblib
        ↓
8. Load model in FastAPI
        ↓
9. Create /predict API
        ↓
10. Connect frontend using Fetch API
        ↓
11. Deploy backend and frontend
```

---

## 🎯 What I Learned

This project helped me understand how to take an ML model beyond a notebook and turn it into a working web application.

Key concepts learned:

- Preparing a dataset for ML
- Feature and target separation
- Train/test splitting
- Linear Regression
- Model evaluation
- Saving and loading ML models
- Building APIs with FastAPI
- Pydantic request validation
- Connecting JavaScript to a Python API
- CORS
- Deploying an ML application
- Using Git and GitHub for project management

---

## ⚠️ Project Limitations

This project is primarily an educational demonstration.

- The dataset is small and artificially created.
- The model has not been validated on a large real-world dataset.
- The prediction should not be used for real academic decisions.
- Model performance may change significantly with real-world data.

---

## 🚀 Future Improvements

- Use a larger real-world student dataset
- Compare Linear Regression with Random Forest and other models
- Add data visualization
- Add prediction history
- Improve frontend UI/UX
- Add authentication
- Add a database
- Add automated model retraining
- Improve model evaluation with cross-validation

---

## 👨‍💻 Author

**Mohammad Osama**

Built as an end-to-end Machine Learning learning project.

---

## 📄 License

This project is available for educational and learning purposes.
