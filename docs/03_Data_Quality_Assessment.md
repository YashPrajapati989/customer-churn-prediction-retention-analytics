# Data Quality Assessment

## Overview

Before performing exploratory data analysis and building machine learning models, a comprehensive data quality assessment was conducted to evaluate the completeness, consistency, accuracy, and reliability of the Telco Customer Churn dataset.

The assessment identifies potential data quality issues that may impact analysis and outlines the actions required to prepare the dataset for modeling.

---

# Data Quality Checklist

| Assessment | Status |
|------------|--------|
| Dataset Loaded Successfully | ✅ |
| Duplicate Records Checked | ⏳ |
| Missing Values Checked | ⏳ |
| Data Types Validated | ⏳ |
| Outliers Identified | ⏳ |
| Target Variable Verified | ⏳ |
| Data Leakage Identified | ✅ |

---

# 1. Dataset Summary

| Metric | Value |
|--------|------|
| Total Records | 7,043 |
| Total Columns | 50 |
| Numerical Columns | To be evaluated |
| Categorical Columns | To be evaluated |
| Target Variable | Churn Label |

---

# 2. Missing Values Assessment

## Objective

Identify columns containing null or missing values that could negatively affect analysis and machine learning performance.

### Checks

- Missing values per column
- Missing value percentage
- Missing value patterns

### Expected Action

- Remove columns with excessive missing values (if applicable).
- Impute numerical values using Median or Mean.
- Impute categorical values using Mode or create an "Unknown" category where appropriate.

---

# 3. Duplicate Records Assessment

## Objective

Identify duplicate customer records.

### Checks

- Duplicate rows
- Duplicate Customer IDs

### Expected Action

- Remove exact duplicate records.
- Ensure Customer ID remains unique.

---

# 4. Data Type Validation

## Objective

Ensure every column has the correct data type.

### Validation

| Data Type | Examples |
|-----------|----------|
| Integer | Age, Population, Tenure in Months |
| Float | Monthly Charge, Total Charges, CLTV |
| Categorical | Gender, Contract, Payment Method |
| Text | Churn Reason |

### Expected Action

Convert incorrect data types before analysis.

---

# 5. Categorical Data Validation

## Objective

Validate categorical values for consistency.

### Checks

- Unexpected categories
- Typographical errors
- Case sensitivity
- Extra spaces

Example:

Correct

Yes
No

Incorrect

YES
yes
 No

---

# 6. Numerical Data Validation

## Objective

Validate numerical columns.

### Checks

- Negative values
- Impossible values
- Extremely large values
- Invalid revenue amounts

Example

Age cannot be negative.

Monthly charges should not be negative.

---

# 7. Outlier Assessment

## Objective

Detect unusual observations.

Potential columns

- Monthly Charge
- Total Charges
- Total Revenue
- Avg Monthly GB Download
- CLTV

Methods

- Box Plot
- IQR Method
- Z-score (optional)

Expected Action

Investigate whether outliers are genuine customer behavior or data entry errors.

---

# 8. Target Variable Assessment

Target Column

Churn Label

Expected Classes

- Yes
- No

Checks

- Class distribution
- Class imbalance

If imbalance exists, techniques such as class weighting or SMOTE may be considered during model development.

---

# 9. Data Leakage Assessment

The following variables contain information unavailable at prediction time and will be excluded from model training.

| Column | Reason |
|---------|--------|
| Customer Status | Reveals final customer outcome |
| Churn Score | Derived from churn outcome |
| Churn Category | Available only after churn |
| Churn Reason | Available only after churn |

These variables are retained only for business analysis and visualization.

---

# 10. Feature Selection Readiness

Columns will be categorized as:

- Predictive Features
- Target Variable
- Identifiers
- Leakage Variables

Only predictive features will be used during model development.

---

# Data Quality Summary

The dataset is expected to be of high quality with comprehensive customer demographic, service usage, billing, and satisfaction information.

Before machine learning, the following preprocessing tasks will be completed:

- Validate missing values.
- Remove duplicate records.
- Correct data types.
- Handle outliers where necessary.
- Exclude identifier columns.
- Remove leakage variables.
- Prepare features for modeling.

Following these steps, the dataset will be suitable for exploratory data analysis, feature engineering, and predictive modeling.