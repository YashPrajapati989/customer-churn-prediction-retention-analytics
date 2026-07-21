-- ============================================
-- Drop Table (Optional)
-- ============================================

DROP TABLE IF EXISTS customer_churn;

-- ============================================
-- Create Main Table
-- ============================================

CREATE TABLE customer_churn (

    customer_id                         VARCHAR(20) PRIMARY KEY,

    gender                              VARCHAR(10),
    age                                 INT,
    under_30                            VARCHAR(5),
    senior_citizen                      VARCHAR(5),
    married                             VARCHAR(5),
    dependents                          VARCHAR(5),
    number_of_dependents                INT,

    country                             VARCHAR(50),
    state                               VARCHAR(100),
    city                                VARCHAR(100),
    zip_code                            INT,
    latitude                            DECIMAL(10,6),
    longitude                           DECIMAL(10,6),
    population                          INT,

    quarter                             VARCHAR(10),
    referred_a_friend                   VARCHAR(5),
    number_of_referrals                 INT,

    tenure_in_months                    INT,

    offer                               VARCHAR(50),

    phone_service                       VARCHAR(5),
    avg_monthly_long_distance_charges   DECIMAL(10,2),
    multiple_lines                      VARCHAR(20),

    internet_service                    VARCHAR(5),
    internet_type                       VARCHAR(50),
    avg_monthly_gb_download             DECIMAL(10,2),

    online_security                     VARCHAR(20),
    online_backup                       VARCHAR(20),
    device_protection_plan              VARCHAR(20),
    premium_tech_support                VARCHAR(20),

    streaming_tv                        VARCHAR(20),
    streaming_movies                    VARCHAR(20),
    streaming_music                     VARCHAR(20),
    unlimited_data                      VARCHAR(20),

    contract                            VARCHAR(30),
    paperless_billing                   VARCHAR(5),
    payment_method                      VARCHAR(50),

    monthly_charge                      DECIMAL(10,2),
    total_charges                       DECIMAL(12,2),
    total_refunds                       DECIMAL(12,2),
    total_extra_data_charges            DECIMAL(12,2),
    total_long_distance_charges         DECIMAL(12,2),
    total_revenue                       DECIMAL(12,2),

    satisfaction_score                  INT,

    customer_status                     VARCHAR(30),
    churn_label                         VARCHAR(5),
    churn_score                         INT,

    cltv                                DECIMAL(12,2),

    churn_category                      VARCHAR(100),
    churn_reason                        TEXT
);

-- ============================================
-- Verify Table Structure
-- ============================================

SELECT *
FROM information_schema.columns
WHERE table_name = 'customer_churn'
ORDER BY ordinal_position;