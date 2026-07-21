-- ============================================
-- 1. Total Number of Records
-- ============================================

SELECT COUNT(*) AS total_records
FROM customer_churn;


-- ============================================
-- 2. Preview Dataset
-- ============================================

SELECT *
FROM customer_churn
LIMIT 10;


-- ============================================
-- 3. Check Total Columns
-- ============================================

SELECT COUNT(*) AS total_columns
FROM information_schema.columns
WHERE table_name = 'customer_churn';


-- ============================================
-- 4. Check Duplicate Customer IDs
-- ============================================

SELECT
    customer_id,
    COUNT(*) AS duplicate_count
FROM customer_churn
GROUP BY customer_id
HAVING COUNT(*) > 1;


-- ============================================
-- 5. Check NULL Values (Important Columns)
-- ============================================

SELECT
    COUNT(*) FILTER (WHERE customer_id IS NULL) AS customer_id_nulls,
    COUNT(*) FILTER (WHERE gender IS NULL) AS gender_nulls,
    COUNT(*) FILTER (WHERE age IS NULL) AS age_nulls,
    COUNT(*) FILTER (WHERE tenure_in_months IS NULL) AS tenure_nulls,
    COUNT(*) FILTER (WHERE monthly_charge IS NULL) AS monthly_charge_nulls,
    COUNT(*) FILTER (WHERE total_charges IS NULL) AS total_charges_nulls,
    COUNT(*) FILTER (WHERE churn_label IS NULL) AS churn_label_nulls
FROM customer_churn;


-- ============================================
-- 6. Distinct Values - Churn Label
-- ============================================

SELECT DISTINCT churn_label
FROM customer_churn;


-- ============================================
-- 7. Churn Distribution
-- ============================================

SELECT
    churn_label,
    COUNT(*) AS customers,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (),2) AS percentage
FROM customer_churn
GROUP BY churn_label
ORDER BY customers DESC;


-- ============================================
-- 8. Gender Distribution
-- ============================================

SELECT
    gender,
    COUNT(*) AS customers
FROM customer_churn
GROUP BY gender
ORDER BY customers DESC;


-- ============================================
-- 9. Contract Distribution
-- ============================================

SELECT
    contract,
    COUNT(*) AS customers
FROM customer_churn
GROUP BY contract
ORDER BY customers DESC;


-- ============================================
-- 10. Payment Method Distribution
-- ============================================

SELECT
    payment_method,
    COUNT(*) AS customers
FROM customer_churn
GROUP BY payment_method
ORDER BY customers DESC;


-- ============================================
-- 11. Internet Service Distribution
-- ============================================

SELECT
    internet_service,
    COUNT(*) AS customers
FROM customer_churn
GROUP BY internet_service
ORDER BY customers DESC;


-- ============================================
-- 12. Numerical Summary
-- ============================================

SELECT
    MIN(age) AS min_age,
    MAX(age) AS max_age,
    AVG(age) AS avg_age,
    MIN(monthly_charge) AS min_monthly_charge,
    MAX(monthly_charge) AS max_monthly_charge,
    AVG(monthly_charge) AS avg_monthly_charge,
    MIN(total_charges) AS min_total_charges,
    MAX(total_charges) AS max_total_charges,
    AVG(total_charges) AS avg_total_charges
FROM customer_churn;


-- ============================================
-- 13. Tenure Statistics
-- ============================================

SELECT
    MIN(tenure_in_months) AS minimum_tenure,
    MAX(tenure_in_months) AS maximum_tenure,
    AVG(tenure_in_months) AS average_tenure
FROM customer_churn;


-- ============================================
-- 14. Satisfaction Score Distribution
-- ============================================

SELECT
    satisfaction_score,
    COUNT(*) AS customers
FROM customer_churn
GROUP BY satisfaction_score
ORDER BY satisfaction_score;


-- ============================================
-- 15. Customer Status Distribution
-- ============================================

SELECT
    customer_status,
    COUNT(*) AS customers
FROM customer_churn
GROUP BY customer_status
ORDER BY customers DESC;


-- ============================================
-- 16. Check for Negative Values
-- ============================================

SELECT *
FROM customer_churn
WHERE
    age < 0
    OR monthly_charge < 0
    OR total_charges < 0
    OR total_revenue < 0;


-- ============================================
-- 17. Verify Primary Key Uniqueness
-- ============================================

SELECT
    COUNT(*) AS total_rows,
    COUNT(DISTINCT customer_id) AS unique_customers
FROM customer_churn;


-- ============================================
-- 18. Dataset Successfully Loaded
-- ============================================

SELECT
    'Validation Completed Successfully' AS status;