-- =====================================================
-- Drop Existing Indexes (Optional)
-- =====================================================

DROP INDEX IF EXISTS idx_customer_churn_customer_id;
DROP INDEX IF EXISTS idx_customer_churn_churn_label;
DROP INDEX IF EXISTS idx_customer_churn_contract;
DROP INDEX IF EXISTS idx_customer_churn_state;
DROP INDEX IF EXISTS idx_customer_churn_city;
DROP INDEX IF EXISTS idx_customer_churn_payment_method;
DROP INDEX IF EXISTS idx_customer_churn_internet_type;
DROP INDEX IF EXISTS idx_customer_churn_customer_status;
DROP INDEX IF EXISTS idx_customer_churn_tenure;
DROP INDEX IF EXISTS idx_customer_churn_total_revenue;
DROP INDEX IF EXISTS idx_customer_churn_cltv;
DROP INDEX IF EXISTS idx_customer_churn_churn_contract;
DROP INDEX IF EXISTS idx_customer_churn_state_contract;

-- =====================================================
-- Primary Search Index
-- =====================================================

CREATE INDEX idx_customer_churn_customer_id
ON customer_churn(customer_id);

-- =====================================================
-- Churn Analysis
-- =====================================================

CREATE INDEX idx_customer_churn_churn_label
ON customer_churn(churn_label);

-- =====================================================
-- Contract Analysis
-- =====================================================

CREATE INDEX idx_customer_churn_contract
ON customer_churn(contract);

-- =====================================================
-- Geographic Analysis
-- =====================================================

CREATE INDEX idx_customer_churn_state
ON customer_churn(state);

CREATE INDEX idx_customer_churn_city
ON customer_churn(city);

-- =====================================================
-- Payment Analysis
-- =====================================================

CREATE INDEX idx_customer_churn_payment_method
ON customer_churn(payment_method);

-- =====================================================
-- Internet Service Analysis
-- =====================================================

CREATE INDEX idx_customer_churn_internet_type
ON customer_churn(internet_type);

-- =====================================================
-- Customer Status
-- =====================================================

CREATE INDEX idx_customer_churn_customer_status
ON customer_churn(customer_status);

-- =====================================================
-- Tenure Analysis
-- =====================================================

CREATE INDEX idx_customer_churn_tenure
ON customer_churn(tenure_in_months);

-- =====================================================
-- Revenue Analysis
-- =====================================================

CREATE INDEX idx_customer_churn_total_revenue
ON customer_churn(total_revenue);

-- =====================================================
-- CLTV Analysis
-- =====================================================

CREATE INDEX idx_customer_churn_cltv
ON customer_churn(cltv);

-- =====================================================
-- Composite Indexes
-- =====================================================

CREATE INDEX idx_customer_churn_churn_contract
ON customer_churn(churn_label, contract);

CREATE INDEX idx_customer_churn_state_contract
ON customer_churn(state, contract);

-- =====================================================
-- Verify Indexes
-- =====================================================

SELECT
    indexname,
    indexdef
FROM pg_indexes
WHERE tablename = 'customer_churn'
ORDER BY indexname;