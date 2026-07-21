-- =====================================================
-- Query 1 : Overall Customer Summary
-- =====================================================

SELECT
    COUNT(*) AS total_customers,
    ROUND(AVG(age),2) AS average_age,
    ROUND(AVG(monthly_charge),2) AS average_monthly_charge,
    ROUND(AVG(total_revenue),2) AS average_total_revenue
FROM customer_churn;


-- =====================================================
-- Query 2 : Churn Rate
-- =====================================================

SELECT
    churn_label,
    COUNT(*) AS customers,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (),2) AS churn_percentage
FROM customer_churn
GROUP BY churn_label;


-- =====================================================
-- Query 3 : Churn by Gender
-- =====================================================

SELECT
    gender,
    churn_label,
    COUNT(*) AS customers
FROM customer_churn
GROUP BY gender, churn_label
ORDER BY gender;


-- =====================================================
-- Query 4 : Churn by Age Group
-- =====================================================

SELECT
CASE
    WHEN age < 30 THEN 'Under 30'
    WHEN age BETWEEN 30 AND 50 THEN '30-50'
    ELSE 'Above 50'
END AS age_group,
churn_label,
COUNT(*) AS customers
FROM customer_churn
GROUP BY age_group, churn_label
ORDER BY age_group;


-- =====================================================
-- Query 5 : Churn by Contract Type
-- =====================================================

SELECT
    contract,
    churn_label,
    COUNT(*) AS customers
FROM customer_churn
GROUP BY contract, churn_label
ORDER BY contract;


-- =====================================================
-- Query 6 : Churn by Internet Service
-- =====================================================

SELECT
    internet_type,
    churn_label,
    COUNT(*) AS customers
FROM customer_churn
GROUP BY internet_type, churn_label
ORDER BY internet_type;


-- =====================================================
-- Query 7 : Churn by Payment Method
-- =====================================================

SELECT
    payment_method,
    churn_label,
    COUNT(*) AS customers
FROM customer_churn
GROUP BY payment_method, churn_label
ORDER BY payment_method;


-- =====================================================
-- Query 8 : Average Monthly Charge by Churn
-- =====================================================

SELECT
    churn_label,
    ROUND(AVG(monthly_charge),2) AS avg_monthly_charge
FROM customer_churn
GROUP BY churn_label;


-- =====================================================
-- Query 9 : Average Total Revenue by Churn
-- =====================================================

SELECT
    churn_label,
    ROUND(AVG(total_revenue),2) AS avg_total_revenue
FROM customer_churn
GROUP BY churn_label;


-- =====================================================
-- Query 10 : Average CLTV by Churn
-- =====================================================

SELECT
    churn_label,
    ROUND(AVG(cltv),2) AS avg_cltv
FROM customer_churn
GROUP BY churn_label;


-- =====================================================
-- Query 11 : Customer Satisfaction vs Churn
-- =====================================================

SELECT
    satisfaction_score,
    churn_label,
    COUNT(*) AS customers
FROM customer_churn
GROUP BY satisfaction_score, churn_label
ORDER BY satisfaction_score;


-- =====================================================
-- Query 12 : Top 10 States by Customers
-- =====================================================

SELECT
    state,
    COUNT(*) AS customers
FROM customer_churn
GROUP BY state
ORDER BY customers DESC
LIMIT 10;


-- =====================================================
-- Query 13 : Top 10 Cities by Customers
-- =====================================================

SELECT
    city,
    COUNT(*) AS customers
FROM customer_churn
GROUP BY city
ORDER BY customers DESC
LIMIT 10;


-- =====================================================
-- Query 14 : Revenue by Contract Type
-- =====================================================

SELECT
    contract,
    ROUND(SUM(total_revenue),2) AS revenue
FROM customer_churn
GROUP BY contract
ORDER BY revenue DESC;


-- =====================================================
-- Query 15 : Revenue by Payment Method
-- =====================================================

SELECT
    payment_method,
    ROUND(SUM(total_revenue),2) AS revenue
FROM customer_churn
GROUP BY payment_method
ORDER BY revenue DESC;


-- =====================================================
-- Query 16 : Average Tenure by Churn
-- =====================================================

SELECT
    churn_label,
    ROUND(AVG(tenure_in_months),2) AS average_tenure
FROM customer_churn
GROUP BY churn_label;


-- =====================================================
-- Query 17 : Customers with Highest CLTV
-- =====================================================

SELECT
    customer_id,
    cltv,
    total_revenue
FROM customer_churn
ORDER BY cltv DESC
LIMIT 10;


-- =====================================================
-- Query 18 : Senior Citizens Churn Analysis
-- =====================================================

SELECT
    senior_citizen,
    churn_label,
    COUNT(*) AS customers
FROM customer_churn
GROUP BY senior_citizen, churn_label;


-- =====================================================
-- Query 19 : Married Customers Churn Analysis
-- =====================================================

SELECT
    married,
    churn_label,
    COUNT(*) AS customers
FROM customer_churn
GROUP BY married, churn_label;


-- =====================================================
-- Query 20 : Customers by Internet Type
-- =====================================================

SELECT
    internet_type,
    COUNT(*) AS customers
FROM customer_churn
GROUP BY internet_type
ORDER BY customers DESC;


-- =====================================================
-- Query 21 : Revenue by State
-- =====================================================

SELECT
    state,
    ROUND(SUM(total_revenue),2) AS total_revenue
FROM customer_churn
GROUP BY state
ORDER BY total_revenue DESC
LIMIT 10;


-- =====================================================
-- Query 22 : Churn by Offer
-- =====================================================

SELECT
    offer,
    churn_label,
    COUNT(*) AS customers
FROM customer_churn
GROUP BY offer, churn_label
ORDER BY offer;


-- =====================================================
-- Query 23 : Churn by Paperless Billing
-- =====================================================

SELECT
    paperless_billing,
    churn_label,
    COUNT(*) AS customers
FROM customer_churn
GROUP BY paperless_billing, churn_label;


-- =====================================================
-- Query 24 : Churn by Unlimited Data
-- =====================================================

SELECT
    unlimited_data,
    churn_label,
    COUNT(*) AS customers
FROM customer_churn
GROUP BY unlimited_data, churn_label;


-- =====================================================
-- Query 25 : Executive KPI Summary
-- =====================================================

SELECT
    COUNT(*) AS total_customers,
    SUM(total_revenue) AS total_revenue,
    ROUND(AVG(monthly_charge),2) AS avg_monthly_charge,
    ROUND(AVG(cltv), 2) AS avg_cltv,
    AVG(satisfaction_score) AS avg_satisfaction_score
FROM customer_churn;