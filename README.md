# 🤖 Customer Churn Prediction & Retention Analytics Platform

[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen?style=for-the-badge)](https://customer-churn-prediction-retention-analytics-hd5cea3mxqbnp7sh.streamlit.app)

🌐 **Live Application:**  
https://customer-churn-prediction-retention-analytics-hd5cea3mxqbnp7sh.streamlit.app# 🤖 Customer Churn Prediction & Retention Analytics Platform

An end-to-end **Machine Learning + Explainable AI application** that predicts customer churn risk, identifies customers likely to leave, explains the reasons behind churn predictions, and provides actionable retention strategies.

Built using **Python, Scikit-Learn, SHAP, and Streamlit**.

---

# 📌 Project Overview

Customer retention is one of the most important challenges for subscription-based businesses.

Acquiring new customers is usually more expensive than retaining existing ones. Therefore, identifying customers who are likely to churn allows businesses to take preventive actions before losing revenue.

This project builds an AI-powered customer churn analytics platform that helps organizations:

- Predict customers likely to churn
- Calculate churn probability
- Classify customers into risk categories
- Understand the key drivers behind churn
- Provide retention recommendations

The solution combines:

- Machine Learning Classification
- Explainable AI (SHAP)
- Interactive Streamlit Dashboard
- Customer Risk Segmentation
- Business KPI Monitoring
- Automated Batch Prediction
- Data Validation & Error Handling
- Downloadable Prediction Reports
- Business Retention Recommendations

---

# 🎯 Business Problem

Businesses often have large amounts of customer data but struggle to answer:

### Which customers are likely to leave?

Machine learning can identify hidden patterns in customer behaviour.

### Why are customers leaving?

Explainable AI techniques can reveal the factors influencing churn.

### What actions should the business take?

Analytics can convert predictions into retention strategies.

---

# 🏆 Project Objective

Develop an end-to-end customer churn prediction system that:

1. Cleans and prepares customer data
2. Performs feature engineering
3. Trains multiple machine learning models
4. Selects the best-performing model
5. Deploys the model using Streamlit
6. Provides explainable predictions using SHAP
7. Generates actionable retention insights

---

# 📊 Dataset

## Telco Customer Churn Dataset

Dataset contains customer information from a telecommunications company.

It includes:

- Customer demographics
- Account information
- Service subscriptions
- Billing details
- Contract information
- Customer churn status


## Dataset Information

```
Customers: 7,043

Target Variable:
Churn Label

Problem Type:
Binary Classification
```

---

# 🛠 Technology Stack

## Programming Language

- Python


## Data Processing

- Pandas
- NumPy


## Machine Learning

- Scikit-Learn

Algorithms tested:

- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting
- XGBoost


## Explainable AI

- SHAP


## Visualization

- Matplotlib
- Streamlit


## Model Serialization

- Joblib

## Version Control

- Git
- GitHub

## Deployment

- Streamlit Community Cloud

---

# 🏗 Project Structure

```
Customer-Churn-Prediction/

│
├── app.py
├── README.md
├── requirements.txt
├── LICENSE
├── runtime.txt
│
├── assets/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│   ├── best_model.pkl
│   ├── scaler.pkl
│   ├── feature_names.pkl
│   ├── label_encoders.pkl
│   ├── categorical_columns.pkl
│   └── numeric_columns.pkl
│
├── reports/
│   ├── figures/
│   └── model_results/
│       ├── feature_importance.csv
│       └── model_comparison.csv
│
├── screenshots/
│
└── src/
    ├── data_cleaning.py
    ├── feature_engineering.py
    ├── train.py
    └── evaluate.py

```

---

# 🔄 Machine Learning Workflow

```
Raw Dataset

      ↓

Data Cleaning

      ↓

Exploratory Data Analysis

      ↓

Feature Engineering

      ↓

Encoding & Scaling

      ↓

Train-Test Split

      ↓

Model Training

      ↓

Model Evaluation

      ↓

Best Model Selection

      ↓

Streamlit Deployment

      ↓

SHAP Explainability

      ↓

Retention Recommendations
```

---

# 🧹 Data Cleaning & Feature Engineering

## Removed Identifier Columns

Removed:

```
Customer ID
City
Zip Code
Latitude
Longitude
Country
```

Reason:

These columns do not provide meaningful predictive value.

---

## Removed Data Leakage Columns

Removed:

```
Customer Status
Churn Score
Churn Category
Churn Reason
Satisfaction Score
```

Reason:

These variables directly reveal churn outcomes and would create unrealistic model performance.

---

# 🔧 Feature Engineering Steps

Performed:

- Binary encoding
- One-hot encoding
- Numerical scaling
- Feature selection
- Train-test splitting


Generated processed files:

```
X_train.csv

X_test.csv

y_train.csv

y_test.csv
```

---

# 🤖 Machine Learning Model Development

Multiple classification algorithms were trained and evaluated.


## Models Tested


| Model | Description |
|---|---|
| Logistic Regression | Baseline classification model |
| Decision Tree | Rule-based model |
| Random Forest | Ensemble learning |
| Gradient Boosting | Advanced boosting algorithm |
| XGBoost | Gradient boosting framework |


---

# 🏆 Final Model Selection

The best-performing model was:

```
Gradient Boosting Classifier
```


Selection criteria:

- ROC-AUC score
- Cross-validation performance
- Classification metrics


---

# 📈 Model Evaluation


Performance metrics used:


| Metric | Purpose |
|-|-|
| Accuracy | Overall prediction correctness |
| Precision | Correct churn predictions |
| Recall | Ability to identify churners |
| F1 Score | Balance between precision and recall |
| ROC-AUC | Model discrimination ability |


Example performance:

```
Accuracy:
84.46%


ROC-AUC:
0.84
```

---

# 🚀 Interactive Streamlit Dashboard

The trained Gradient Boosting model has been deployed as an interactive analytics dashboard that enables business users to predict customer churn and understand the reasons behind each prediction.

---

## Dashboard Features

### 📊 Executive Overview

Displays key business metrics:

- 👥 Total Customers
- ⚠ Churn Customers
- ✅ Retained Customers
- 📉 Churn Rate

---

### 🔮 Prediction Engine

Supports two prediction methods:

- Manual Customer Prediction
- Batch Prediction using CSV Upload

The application automatically preprocesses uploaded datasets before generating predictions.

---

### 📂 Smart Dataset Validation

To ensure prediction reliability, the dashboard:

- Detects unsupported datasets
- Validates uploaded CSV structure
- Handles missing columns automatically
- Prevents predictions on incompatible datasets
- Displays user-friendly validation messages

---

### ⚠ Customer Risk Analysis

Customers are automatically segmented into:

| Risk Level | Probability |
|------------|------------:|
| Low Risk | 0–30% |
| Medium Risk | 30–70% |
| High Risk | 70–100% |

Business users can quickly identify customers requiring immediate attention.

---

### 📈 Prediction Distribution

Visualizes:

- Churn vs Retained Customers
- Customer Risk Distribution

---

### 🧠 Model Insights

Displays:

- Feature Importance
- Top Churn Drivers
- Model Performance Metrics

---

### 🔍 Explainable AI (SHAP)

Every prediction can be explained using SHAP values.

The dashboard shows:

- Features increasing churn probability
- Features reducing churn probability
- Individual customer explanations
- Global model explanations

This improves transparency and trust in the machine learning model.

---

### 📥 Export Predictions

Prediction results can be downloaded as:

```

customer_churn_predictions.csv

```

Including:

- Prediction
- Churn Probability
- Risk Level

---

### 💡 Business Recommendations

Based on predicted risk levels, the dashboard provides actionable retention strategies.

Example:

High Risk Customers

- Offer loyalty discounts
- Encourage annual contracts
- Review monthly pricing
- Provide proactive technical support

Medium Risk Customers

- Personalized marketing campaigns
- Customer engagement programs

Low Risk Customers

- Referral programs
- Premium service upgrades


Users can download:


```
customer_churn_predictions.csv
```


Containing:


```
Customer Information

Prediction

Churn Probability

Risk Level
```
---
# 🧠 Explainable AI

Machine learning predictions alone are often insufficient for business decision-making.

This project integrates SHAP (SHapley Additive Explanations) to explain model predictions.

Benefits include:

- Improved transparency
- Easier business interpretation
- Trustworthy AI predictions
- Individual customer-level explanations
- Identification of key churn drivers
---

---
# 📈 Business Impact

This solution enables organizations to:

- Predict customer churn before it occurs
- Identify high-value customers at risk
- Improve customer retention strategies
- Reduce revenue loss
- Support data-driven business decisions
- Prioritize retention campaigns using risk scores
---

---
# ⭐ Key Features

- End-to-End Machine Learning Pipeline
- Customer Churn Prediction
- Explainable AI using SHAP
- Interactive Streamlit Dashboard
- Manual Customer Prediction
- Batch CSV Prediction
- Smart Dataset Validation
- Business KPI Dashboard
- Customer Risk Segmentation
- Feature Importance Visualization
- Prediction Probability Analysis
- Downloadable Prediction Reports
- Business Retention Recommendations
- Production-Ready Deployment
---

---
# ☁ Deployment

The application is designed for deployment on Streamlit Community Cloud.

Deployment includes:

- Cloud-hosted Streamlit dashboard
- GitHub integration
- Automatic model loading
- Interactive customer predictions
- CSV batch prediction support

---

---

# ⚙ Installation Guide


## Clone Repository

```bash
git clone <repository-url>
```


## Navigate Project Folder

```bash
cd Customer-Churn-Prediction
```


## Install Dependencies


```bash
pip install -r requirements.txt
```


---

# ▶ Running the Project


## Train Model


```bash
python src/train.py
```


This generates:

```
best_model.pkl

feature_names.pkl

scaler.pkl

encoders
```


---

## Launch Dashboard

Run:


```bash
streamlit run app.py
```


---

# 📦 Requirements


```
pandas

numpy

scikit-learn

streamlit

shap

matplotlib

joblib

xgboost
```

---

# 📸 Dashboard Screenshots


Add screenshots:


```
screenshots/

│
├── executive_overview.png
│
├── prediction_results.png
│
├── risk_analysis.png
│
└── shap_explanation.png
```

---

# 🔮 Future Improvements


Possible enhancements:


- Deploy using Streamlit Cloud
- Create REST API using FastAPI
- Add automated model retraining pipeline
- Add customer segmentation
- Add database integration
- Add real-time prediction
- Add MLOps monitoring
- Add AI-powered retention recommendations


---

# 🎓 Skills Demonstrated

This project demonstrates proficiency in:

- Python Programming
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Machine Learning Classification
- Hyperparameter Tuning
- Model Evaluation
- Explainable AI (SHAP)
- Business Intelligence
- Interactive Dashboard Development
- Streamlit Deployment
- Data Validation
- Batch Prediction Systems
- Business KPI Reporting
- Git & GitHub

---

# 👨‍💻 Author


## Yash Prajapati

Data Science | Machine Learning | Analytics


---

# ⭐ Project Summary


This project demonstrates how machine learning can transform customer data into actionable business intelligence.

The final solution does not only predict churn but also explains customer behaviour and recommends strategies to improve retention.
