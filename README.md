# 🤖 Customer Churn Prediction & Retention Analytics Platform

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
- Explainable AI
- Business Analytics Dashboard

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


## Model Management

- Joblib

---

# 🏗 Project Structure

```
Customer-Churn-Prediction/

│
├── data/
│   │
│   ├── raw/
│   │
│   └── processed/
│
│
├── notebooks/
│
│
├── src/
│   │
│   ├── data_cleaning.py
│   │
│   ├── feature_engineering.py
│   │
│   └── train.py
│
│
├── models/
│   │
│   ├── best_model.pkl
│   ├── scaler.pkl
│   ├── feature_names.pkl
│   ├── label_encoders.pkl
│   ├── categorical_columns.pkl
│   └── numeric_columns.pkl
│
│
├── dashboard/
│   │
│   └── app.py
│
│
├── reports/
│   │
│   └── model_results/
│       │
│       └── feature_importance.csv
│
│
├── requirements.txt
│
└── README.md

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

# 🚀 Streamlit Dashboard

The trained model was deployed as an interactive analytics dashboard.


## Dashboard Features


# 📊 Executive Overview

Displays business KPIs:


```
👥 Total Customers

⚠ Churn Customers

✅ Retained Customers

📉 Churn Rate
```


---

# 🔮 Prediction Engine

Users can upload customer data and generate:


```
Customer Prediction

Churn Probability

Risk Category
```


---

# ⚠ Customer Risk Analysis

Customers are grouped into:


| Risk Category | Probability |
|-|-|
| Low Risk | 0-30% |
| Medium Risk | 30-70% |
| High Risk | 70-100% |


This helps businesses prioritize retention efforts.

---

# 🧠 Model Insights


The dashboard provides:


## Feature Importance

Identifies major churn drivers.


Example:


```
1. Tenure in Months

2. Monthly Charges

3. Contract Type

4. Internet Service

5. CLTV
```

---

# 🔍 Explainable AI Using SHAP


SHAP explains individual predictions.


Instead of only showing:

```
Customer will churn
```

the system explains:


```
Why will this customer churn?
```


Example:


```
Customer ID:

7590-VHVEG


Prediction:

High Risk


Probability:

87%


Main Reasons:

↑ Month-to-month contract

↑ High monthly charges

↑ Low customer tenure

```


---

# 💡 Retention Strategy Recommendations


The dashboard converts predictions into business actions.


## High Risk Customers


Recommended actions:


✅ Offer loyalty discounts

✅ Promote annual contracts

✅ Provide proactive support

✅ Review pricing plans


---

## Medium Risk Customers


Actions:


- Personalized offers

- Customer engagement campaigns

- Monitor behaviour patterns


---

## Low Risk Customers


Actions:


- Maintain relationship

- Encourage referrals

- Upsell services

---

# 📥 Dashboard Output


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


Navigate to dashboard folder:


```bash
cd dashboard
```


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


This project demonstrates:


✅ Data Cleaning

✅ Exploratory Data Analysis

✅ Feature Engineering

✅ Machine Learning Classification

✅ Model Evaluation

✅ Hyperparameter Optimization

✅ Model Deployment

✅ Explainable AI

✅ Business Analytics

✅ Streamlit Application Development


---

# 👨‍💻 Author


## Yash Prajapati

Data Science | Machine Learning | Analytics


---

# ⭐ Project Summary


This project demonstrates how machine learning can transform customer data into actionable business intelligence.

The final solution does not only predict churn but also explains customer behaviour and recommends strategies to improve retention.
