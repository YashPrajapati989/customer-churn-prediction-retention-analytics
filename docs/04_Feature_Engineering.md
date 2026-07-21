# Feature Engineering

## Overview

Feature engineering is the process of transforming raw data into meaningful input variables that improve the performance of machine learning models.

The objective is to create a clean, consistent, and informative feature set while preventing data leakage and ensuring the model generalizes well to unseen data.

---

# Feature Engineering Workflow

```
Raw Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Missing Value Treatment
      │
      ▼
Duplicate Removal
      │
      ▼
Data Type Conversion
      │
      ▼
Categorical Encoding
      │
      ▼
Feature Scaling
      │
      ▼
Feature Selection
      │
      ▼
Machine Learning Dataset
```

---

# 1. Identifier Removal

The following columns uniquely identify customers and do not contribute to prediction.

| Column | Action | Reason |
|---------|--------|--------|
| Customer ID | Remove | Unique Identifier |
| Zip Code | Remove | High Cardinality |
| Latitude | Remove | Geographic Coordinate |
| Longitude | Remove | Geographic Coordinate |

---

# 2. Data Leakage Removal

The following variables contain information that becomes available only after customer churn has occurred.

Including these variables would produce unrealistic model performance.

| Column | Reason |
|---------|--------|
| Customer Status | Reveals final customer outcome |
| Churn Score | Derived using churn information |
| Churn Category | Known only after churn |
| Churn Reason | Available after churn |

These columns will only be used for business reporting and dashboard visualization.

---

# 3. Missing Value Treatment

### Numerical Variables

Missing numerical values will be imputed using:

- Median (preferred)
- Mean (where appropriate)

---

### Categorical Variables

Missing categorical values will be handled using:

- Mode
- "Unknown" category (if required)

---

# 4. Duplicate Removal

Duplicate customer records will be removed before model training to ensure data integrity.

Validation includes:

- Duplicate rows
- Duplicate Customer IDs

---

# 5. Data Type Conversion

Incorrect data types will be converted before analysis.

Examples

| Column | Expected Type |
|---------|---------------|
| Age | Integer |
| Monthly Charge | Float |
| Total Charges | Float |
| CLTV | Float |
| Churn Label | Category |

---

# 6. Categorical Encoding

Machine learning algorithms require numerical input.

Categorical variables will be converted using encoding techniques.

### Binary Encoding

Applicable columns

- Gender
- Married
- Dependents
- Paperless Billing
- Phone Service
- Streaming TV
- Streaming Movies
- Unlimited Data

Example

Yes → 1

No → 0

---

### One-Hot Encoding

Applied to multi-category variables.

Examples

- Contract
- Payment Method
- Internet Type
- Offer
- State
- City

---

# 7. Feature Scaling

Numerical variables will be standardized before training algorithms that are sensitive to feature magnitude.

Methods

- StandardScaler
- MinMaxScaler (if required)

Potential columns

- Age
- Monthly Charge
- Total Charges
- CLTV
- Population
- Avg Monthly GB Download
- Avg Monthly Long Distance Charges

---

# 8. Feature Selection

Only meaningful predictors will be retained.

Selection methods include:

- Correlation Analysis
- Feature Importance
- Recursive Feature Elimination (RFE)
- Mutual Information
- Business Knowledge

---

# 9. Target Variable Encoding

Target Column

Churn Label

Encoding

| Original | Encoded |
|----------|---------|
| No | 0 |
| Yes | 1 |

This converts the target into a binary variable suitable for classification algorithms.

---

# 10. Final Feature Set

The final dataset will contain:

- Customer Demographics
- Account Information
- Service Usage
- Billing Information
- Customer Satisfaction
- Revenue Metrics

Excluded:

- Identifiers
- Leakage Variables

---

# Feature Engineering Summary

The following preprocessing steps will be completed before model development:

- Remove identifier columns.
- Remove leakage variables.
- Handle missing values.
- Remove duplicate records.
- Validate data types.
- Encode categorical variables.
- Scale numerical variables where necessary.
- Encode the target variable.
- Select the most relevant predictive features.

The resulting dataset will be optimized for training robust and interpretable machine learning models.