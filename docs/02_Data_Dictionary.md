# Data Dictionary

## Dataset Information

| Attribute | Value |
|-----------|-------|
| Dataset | Telco Customer Churn |
| Industry | Telecommunications |
| Rows | 7,043 |
| Columns | 50 |
| Target Variable | Churn Label |

---

# Column Definitions

| Column Name | Data Type | Description | Usage |
|-------------|----------|-------------|-------|
| Customer ID | String | Unique identifier for each customer | Ignore (Identifier) |
| Gender | Categorical | Customer gender | Feature |
| Age | Integer | Customer age | Feature |
| Under 30 | Categorical | Indicates whether customer is below 30 | Feature |
| Senior Citizen | Categorical | Indicates senior citizen status | Feature |
| Married | Categorical | Marital status | Feature |
| Dependents | Categorical | Whether customer has dependents | Feature |
| Number of Dependents | Integer | Number of dependents | Feature |
| Country | Categorical | Customer country | Feature |
| State | Categorical | Customer state | Feature |
| City | Categorical | Customer city | Feature |
| Zip Code | Integer | Customer ZIP code | Ignore |
| Latitude | Float | Customer latitude | Ignore |
| Longitude | Float | Customer longitude | Ignore |
| Population | Integer | Population of customer's city | Feature |
| Quarter | Categorical | Quarter when customer joined | Feature |
| Referred a Friend | Categorical | Whether customer was referred | Feature |
| Number of Referrals | Integer | Number of referrals made | Feature |
| Tenure in Months | Integer | Customer tenure | Feature |
| Offer | Categorical | Marketing offer accepted | Feature |
| Phone Service | Categorical | Phone service subscription | Feature |
| Avg Monthly Long Distance Charges | Float | Average monthly long-distance charges | Feature |
| Multiple Lines | Categorical | Multiple phone lines | Feature |
| Internet Service | Categorical | Internet service availability | Feature |
| Internet Type | Categorical | Internet connection type | Feature |
| Avg Monthly GB Download | Float | Average monthly download usage | Feature |
| Online Security | Categorical | Online security service | Feature |
| Online Backup | Categorical | Online backup service | Feature |
| Device Protection Plan | Categorical | Device protection subscription | Feature |
| Premium Tech Support | Categorical | Premium technical support | Feature |
| Streaming TV | Categorical | Streaming TV subscription | Feature |
| Streaming Movies | Categorical | Streaming movie subscription | Feature |
| Streaming Music | Categorical | Streaming music subscription | Feature |
| Unlimited Data | Categorical | Unlimited data plan | Feature |
| Contract | Categorical | Contract type | Feature |
| Paperless Billing | Categorical | Paperless billing status | Feature |
| Payment Method | Categorical | Customer payment method | Feature |
| Monthly Charge | Float | Monthly bill amount | Feature |
| Total Charges | Float | Total amount charged | Feature |
| Total Refunds | Float | Total refunds issued | Feature |
| Total Extra Data Charges | Float | Additional data usage charges | Feature |
| Total Long Distance Charges | Float | Total long-distance charges | Feature |
| Total Revenue | Float | Total customer revenue | Feature |
| Satisfaction Score | Integer | Customer satisfaction rating | Feature |
| Customer Status | Categorical | Current customer status | Ignore (Data Leakage) |
| Churn Label | Categorical | Indicates whether customer churned | **Target** |
| Churn Score | Integer | Internal churn risk score | Ignore (Data Leakage) |
| CLTV | Float | Customer Lifetime Value | Feature |
| Churn Category | Categorical | High-level churn category | Ignore (Data Leakage) |
| Churn Reason | Text | Detailed reason for churn | Ignore (Data Leakage) |

---

# Target Variable

**Churn Label**

- Yes → Customer churned
- No → Customer retained

This is the dependent variable used for binary classification.

---

# Features Used for Machine Learning

The model will use customer demographic, account, service usage, billing, and satisfaction attributes to predict customer churn.

---

# Excluded Columns

The following columns will not be used during model training:

| Column | Reason |
|---------|--------|
| Customer ID | Unique identifier |
| Zip Code | Identifier / High cardinality |
| Latitude | Geographic coordinate |
| Longitude | Geographic coordinate |
| Customer Status | Data leakage |
| Churn Score | Data leakage |
| Churn Category | Available only after churn |
| Churn Reason | Available only after churn |

These columns either uniquely identify customers or reveal information that would not be available at the time of prediction, leading to data leakage.