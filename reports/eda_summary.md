# Customer Churn Prediction & Retention Analytics

## Exploratory Data Analysis (EDA) Summary

---

## Project Overview

The purpose of this Exploratory Data Analysis (EDA) was to understand customer behavior, identify factors contributing to customer churn, and uncover business opportunities for improving customer retention.

The analysis was performed using Python, Pandas, Matplotlib, and Seaborn.

---

# Dataset Summary

| Metric | Value |
|----------|---------|
| Dataset | Telco Customer Churn |
| Total Records | 7,043 Customers |
| Total Features | 50 |
| Target Variable | Churn Label |
| Project Type | Binary Classification |
| Objective | Predict Customer Churn |

---

# Data Quality Assessment

The dataset was evaluated before analysis.

### Missing Values

- Missing values were identified.
- Numerical variables were imputed using the median.
- Categorical variables were imputed using the mode.

### Duplicate Records

- Duplicate records were checked.
- Duplicate rows were removed where necessary.

### Data Types

The dataset contains:

- Numerical variables
- Categorical variables
- Binary variables

All variables were validated before further analysis.

---

# Univariate Analysis

The following variables were explored individually:

- Customer Churn
- Gender
- Age
- Contract Type
- Internet Type
- Payment Method
- Monthly Charges
- Total Revenue
- Customer Lifetime Value (CLTV)
- Customer Status

Key visualizations included:

- Count Plots
- Histograms
- Distribution Plots

---

# Bivariate Analysis

Relationships between customer churn and business variables were explored.

Variables analysed include:

- Gender vs Churn
- Contract vs Churn
- Payment Method vs Churn
- Internet Type vs Churn
- Satisfaction Score vs Churn
- Monthly Charges vs Churn
- Total Revenue vs Churn
- Customer Lifetime Value vs Churn

Visualizations included:

- Count Plots
- Box Plots
- Bar Charts

---

# Correlation Analysis

A correlation heatmap was created to examine relationships between numerical variables.

The analysis highlighted:

- Positive relationships between revenue-related variables.
- Strong relationship between tenure and customer value.
- Several variables suitable for machine learning.

---

# Outlier Analysis

Boxplots were used to detect potential outliers in:

- Age
- Monthly Charges
- Total Charges
- Total Revenue
- Customer Lifetime Value

Outliers were retained because they represent genuine customer behaviour rather than data entry errors.

---

# Key Business Insights

## 1. Contract Type

Customers with month-to-month contracts exhibit a significantly higher churn rate compared to customers on long-term contracts.

Business Recommendation:

- Encourage customers to migrate to annual or multi-year contracts using targeted incentives.

---

## 2. Customer Satisfaction

Lower customer satisfaction scores are strongly associated with higher churn rates.

Business Recommendation:

- Improve customer support quality.
- Introduce proactive customer engagement programmes.

---

## 3. Revenue

Customers generating higher revenue contribute significantly to business profitability.

Business Recommendation:

- Prioritise retention strategies for high-value customers.

---

## 4. Customer Lifetime Value (CLTV)

High CLTV customers should be considered strategic assets.

Business Recommendation:

- Develop personalised loyalty programmes.
- Offer premium services and exclusive benefits.

---

## 5. Payment Method

Certain payment methods demonstrate higher churn rates.

Business Recommendation:

- Encourage customers to adopt automated payment methods.

---

## 6. Internet Service

Customer churn varies across internet service types.

Business Recommendation:

- Review service quality for customer segments experiencing elevated churn.

---

## 7. Monthly Charges

Customers paying higher monthly charges tend to exhibit higher churn risk.

Business Recommendation:

- Introduce personalised pricing plans.
- Offer retention discounts for high-risk customers.

---

# Business Opportunities

The analysis identified several opportunities:

- Improve customer retention programmes.
- Increase customer satisfaction.
- Reduce churn among month-to-month customers.
- Expand loyalty programmes.
- Focus retention efforts on high-value customers.
- Optimise pricing strategies.
- Improve customer service quality.

---

# Machine Learning Readiness

Following exploratory analysis, the dataset is considered suitable for machine learning.

The next phase includes:

- Feature Engineering
- Feature Selection
- Encoding Categorical Variables
- Scaling Numerical Variables
- Train-Test Split
- Model Training
- Model Evaluation

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- PostgreSQL
- SQL
- Scikit-learn
- Power BI

---

# Deliverables

The exploratory analysis produced:

- 20+ Visualisations
- Business Insights
- Correlation Analysis
- Outlier Detection
- Customer Behaviour Analysis
- Data Quality Assessment

---

# Conclusion

The exploratory analysis provides valuable insights into customer behaviour and identifies key drivers of customer churn.

The findings establish a strong foundation for predictive modelling and support data-driven business decisions aimed at improving customer retention, increasing customer lifetime value, and reducing revenue loss.

The cleaned and analysed dataset is now ready for feature engineering and machine learning model development.