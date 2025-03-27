# 🩺 Insurance Enrollment Prediction

This project predicts whether an employee will enroll in an insurance plan using machine learning.

## 🔧 Setup

Install dependencies with:

```bash
pip install -r requirements.txt
```

Or using conda:

```bash
conda env create -f environment.yml
conda activate insurance-enrollment-ml
```

## 🚀 Run the Model

Place `employee_data.csv` in the root folder and run:

```bash
jupyter notebook insurance_enrollment_prediction.ipynb
```

Or to serve as an API:

```bash
uvicorn api:app --reload
```

## 📈 MLflow Logging

After training, model metrics and parameters are logged with MLflow:

```bash
mlflow ui
```

## 📊 Project Includes

- `insurance_enrollment_prediction.ipynb`: Main notebook
- `report.md`: Summary of findings and next steps
- `api.py`: FastAPI server to make predictions
