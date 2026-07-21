-- =====================================================
-- Drop Existing Views (Optional)
-- =====================================================

DROP VIEW IF EXISTS vw_customer_summary CASCADE;
DROP VIEW IF EXISTS vw_churn_analysis CASCADE;
DROP VIEW IF EXISTS vw_revenue_analysis CASCADE;
DROP VIEW IF EXISTS vw_customer_segmentation CASCADE;
DROP VIEW IF EXISTS vw_high_risk_customers CASCADE;


-- =====================================================
-- View 1 : Customer Summary
-- =====================================================

CREATE VIEW vw_customer_summary AS

SELECT
    customer_id,
    gender,
    age,
    married,
    state,
    city,
    tenure_in_months,
    contract,
    payment_method,
    monthly_charge,
    total_revenue,
    cltv,
    satisfaction_score,
    customer_status,
    churn_label
FROM customer_churn;


-- =====================================================
-- View 2 : Churn Analysis
-- =====================================================

CREATE VIEW vw_churn_analysis AS

SELECT
    churn_label,
    contract,
    internet_type,
    payment_method,
    COUNT(*) AS total_customers,
    ROUND(AVG(monthly_charge),2) AS avg_monthly_charge,
    ROUND(AVG(total_revenue),2) AS avg_total_revenue,
    ROUND(AVG(cltv),2) AS avg_cltv
FROM customer_churn
GROUP BY
    churn_label,
    contract,
    internet_type,
    payment_method;


-- =====================================================
-- View 3 : Revenue Analysis
-- =====================================================

CREATE VIEW vw_revenue_analysis AS

SELECT
    state,
    contract,
    payment_method,
    COUNT(*) AS customers,
    ROUND(SUM(total_revenue),2) AS total_revenue,
    ROUND(AVG(total_revenue),2) AS avg_revenue
FROM customer_churn
GROUP BY
    state,
    contract,
    payment_method;


-- =====================================================
-- View 4 : Customer Segmentation
-- =====================================================

CREATE VIEW vw_customer_segmentation AS

SELECT
    customer_id,

    CASE
        WHEN age < 30 THEN 'Under 30'
        WHEN age BETWEEN 30 AND 50 THEN '30-50'
        ELSE 'Above 50'
    END AS age_group,

    CASE
        WHEN monthly_charge < 40 THEN 'Low'
        WHEN monthly_charge BETWEEN 40 AND 80 THEN 'Medium'
        ELSE 'High'
    END AS monthly_charge_band,

    CASE
        WHEN cltv < 3000 THEN 'Low CLTV'
        WHEN cltv BETWEEN 3000 AND 5000 THEN 'Medium CLTV'
        ELSE 'High CLTV'
    END AS cltv_segment,

    tenure_in_months,
    contract,
    churn_label
FROM customer_churn;


-- =====================================================
-- View 5 : High Risk Customers
-- =====================================================

CREATE VIEW vw_high_risk_customers AS

SELECT
    customer_id,
    age,
    contract,
    payment_method,
    monthly_charge,
    total_revenue,
    cltv,
    satisfaction_score,
    churn_score,
    churn_category,
    churn_reason
FROM customer_churn
WHERE
    churn_label = 'Yes'
ORDER BY
    churn_score DESC,
    satisfaction_score ASC;


-- =====================================================
-- Verify Views
-- =====================================================

SELECT table_name
FROM information_schema.views
WHERE table_schema = 'public'
ORDER BY table_name;