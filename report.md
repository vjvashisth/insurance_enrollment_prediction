# 📊 Insurance Enrollment Prediction Report

## 🔍 Data Observations
- The dataset includes demographic and employment info of employees.
- Categorical fields like gender, marital_status, region were label-encoded.
- `has_dependents` was binary-encoded (Yes = 1, No = 0).

## 🤖 Model Choices & Rationale
- **Random Forest** for strong baseline.
- **Gradient Boosting** for high accuracy and correcting weak learners.
- **Voting Ensemble** combining RF, GB, and Logistic Regression for balance between linear and nonlinear modeling.

## 📈 Evaluation Results
- F1 Score (10-fold CV): ~0.9998
- Voting Ensemble achieved perfect precision and recall on the test set.

## 🧠 Key Takeaways
- Features like salary, tenure, and employment type are important predictors.
- Ensemble methods improved performance with very low variance across folds.

## 🔮 Next Steps (with more time)
- Test on real-world or external datasets.
- Deploy as a cloud microservice with autoscaling.
- Monitor drift and retrain periodically.
