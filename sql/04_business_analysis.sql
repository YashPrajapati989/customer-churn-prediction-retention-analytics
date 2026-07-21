-- =====================================================
-- Query 1: Customer Segmentation by Age
-- =====================================================

SELECT
    CASE
        WHEN age < 30 THEN 'Under 30'
        WHEN age BETWEEN 30 AND 50 THEN '30-50'
        ELSE 'Above 50'
    END AS age_group,
    COUNT(*) AS customers
FROM customer_churn
GROUP BY age_group
ORDER BY customers DESC;


-- =====================================================
-- Query 2: Revenue Contribution by Contract Type
-- =====================================================

SELECT
    contract,
    ROUND(SUM(total_revenue),2) AS total_revenue,
    ROUND(
        100.0 * SUM(total_revenue) /
        SUM(SUM(total_revenue)) OVER (),2
    ) AS revenue_percentage
FROM customer_churn
GROUP BY contract
ORDER BY total_revenue DESC;


-- =====================================================
-- Query 3: Top 10 Customers by Revenue
-- =====================================================

SELECT
    customer_id,
    total_revenue
FROM customer_churn
ORDER BY total_revenue DESC
LIMIT 10;


-- =====================================================
-- Query 4: Top 10 Customers by CLTV
-- =====================================================

SELECT
    customer_id,
    cltv
FROM customer_churn
ORDER BY cltv DESC
LIMIT 10;


-- =====================================================
-- Query 5: Average Revenue by State
-- =====================================================

SELECT
    state,
    ROUND(AVG(total_revenue),2) AS avg_revenue
FROM customer_churn
GROUP BY state
ORDER BY avg_revenue DESC;


-- =====================================================
-- Query 6: Churn Rate by Contract
-- =====================================================

SELECT
    contract,
    ROUND(
        100.0 * SUM(CASE WHEN churn_label='Yes' THEN 1 ELSE 0 END)
        / COUNT(*),2
    ) AS churn_rate
FROM customer_churn
GROUP BY contract
ORDER BY churn_rate DESC;


-- =====================================================
-- Query 7: Churn Rate by Internet Type
-- =====================================================

SELECT
    internet_type,
    ROUND(
        100.0 * SUM(CASE WHEN churn_label='Yes' THEN 1 ELSE 0 END)
        / COUNT(*),2
    ) AS churn_rate
FROM customer_churn
GROUP BY internet_type
ORDER BY churn_rate DESC;


-- =====================================================
-- Query 8: Average Satisfaction by Customer Status
-- =====================================================

SELECT
    customer_status,
    ROUND(AVG(satisfaction_score),2) AS avg_satisfaction
FROM customer_churn
GROUP BY customer_status
ORDER BY avg_satisfaction DESC;


-- =====================================================
-- Query 9: Monthly Charge Categories
-- =====================================================

SELECT
    CASE
        WHEN monthly_charge < 40 THEN 'Low'
        WHEN monthly_charge BETWEEN 40 AND 80 THEN 'Medium'
        ELSE 'High'
    END AS charge_band,
    COUNT(*) AS customers
FROM customer_churn
GROUP BY charge_band
ORDER BY customers DESC;


-- =====================================================
-- Query 10: CLTV Categories
-- =====================================================

SELECT
    CASE
        WHEN cltv < 3000 THEN 'Low CLTV'
        WHEN cltv BETWEEN 3000 AND 5000 THEN 'Medium CLTV'
        ELSE 'High CLTV'
    END AS cltv_segment,
    COUNT(*) AS customers
FROM customer_churn
GROUP BY cltv_segment;


-- =====================================================
-- Query 11: Top 5 States by Revenue
-- =====================================================

SELECT
    state,
    SUM(total_revenue) AS revenue
FROM customer_churn
GROUP BY state
ORDER BY revenue DESC
LIMIT 5;


-- =====================================================
-- Query 12: Revenue Rank by State
-- =====================================================

SELECT
    state,
    SUM(total_revenue) AS revenue,
    RANK() OVER (ORDER BY SUM(total_revenue) DESC) AS revenue_rank
FROM customer_churn
GROUP BY state;


-- =====================================================
-- Query 13: Dense Rank by CLTV
-- =====================================================

SELECT
    customer_id,
    cltv,
    DENSE_RANK() OVER (ORDER BY cltv DESC) AS cltv_rank
FROM customer_churn;


-- =====================================================
-- Query 14: Revenue Quartiles
-- =====================================================

SELECT
    customer_id,
    total_revenue,
    NTILE(4) OVER (ORDER BY total_revenue DESC) AS revenue_quartile
FROM customer_churn;


-- =====================================================
-- Query 15: Average Revenue by Payment Method
-- =====================================================

SELECT
    payment_method,
    ROUND(AVG(total_revenue),2) AS avg_revenue
FROM customer_churn
GROUP BY payment_method
ORDER BY avg_revenue DESC;


-- =====================================================
-- Query 16: Churn by Satisfaction Score
-- =====================================================

SELECT
    satisfaction_score,
    COUNT(*) FILTER (WHERE churn_label='Yes') AS churned_customers,
    COUNT(*) AS total_customers
FROM customer_churn
GROUP BY satisfaction_score
ORDER BY satisfaction_score;


-- =====================================================
-- Query 17: Top Revenue Cities
-- =====================================================

SELECT
    city,
    SUM(total_revenue) AS revenue
FROM customer_churn
GROUP BY city
ORDER BY revenue DESC
LIMIT 10;


-- =====================================================
-- Query 18: Customer Count by Offer
-- =====================================================

SELECT
    offer,
    COUNT(*) AS customers
FROM customer_churn
GROUP BY offer
ORDER BY customers DESC;


-- =====================================================
-- Query 19: Customers with Premium Tech Support
-- =====================================================

SELECT
    premium_tech_support,
    COUNT(*) AS customers
FROM customer_churn
GROUP BY premium_tech_support;


-- =====================================================
-- Query 20: Customers with Streaming Services
-- =====================================================

SELECT
    streaming_tv,
    streaming_movies,
    COUNT(*) AS customers
FROM customer_churn
GROUP BY streaming_tv, streaming_movies;


-- =====================================================
-- Query 21: Longest Tenure Customers
-- =====================================================

SELECT
    customer_id,
    tenure_in_months
FROM customer_churn
ORDER BY tenure_in_months DESC
LIMIT 20;


-- =====================================================
-- Query 22: Lowest Satisfaction Customers
-- =====================================================

SELECT
    customer_id,
    satisfaction_score
FROM customer_churn
ORDER BY satisfaction_score ASC
LIMIT 20;


-- =====================================================
-- Query 23: High Revenue & High CLTV Customers
-- =====================================================

SELECT
    customer_id,
    total_revenue,
    cltv
FROM customer_churn
WHERE total_revenue > (
    SELECT AVG(total_revenue)
    FROM customer_churn
)
AND cltv > (
    SELECT AVG(cltv)
    FROM customer_churn
);


-- =====================================================
-- Query 24: High-Risk Customer Segment
-- =====================================================

SELECT
    customer_id,
    contract,
    monthly_charge,
    satisfaction_score
FROM customer_churn
WHERE
    churn_label='Yes'
ORDER BY monthly_charge DESC;


-- =====================================================
-- Query 25: Executive KPI Summary
-- =====================================================

SELECT
    COUNT(*) AS total_customers,

    COUNT(*) FILTER (WHERE churn_label = 'Yes') AS churned_customers,

    ROUND(
        100.0 * COUNT(*) FILTER (WHERE churn_label = 'Yes') / COUNT(*),
        2
    ) AS churn_rate,

    ROUND(SUM(total_revenue), 2) AS total_revenue,

    ROUND(AVG(monthly_charge), 2) AS avg_monthly_charge,

    ROUND(AVG(cltv), 2) AS avg_cltv,

    ROUND(AVG(satisfaction_score), 2) AS avg_satisfaction
FROM customer_churn;