# Useful SQL queries for analyzing the Telco Customer Churn dataset plus getting the Dashboard KPIs.

TOTAL_CUSTOMERS = """
SELECT COUNT(*) AS total_customers
FROM customers
"""

CHURN_RATE = """
SELECT
    ROUND(
        100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS churn_rate_pct
FROM customers
"""

CHURN_BY_CONTRACT = """
SELECT
    Contract,
    ROUND(
        100.0 * AVG(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END),
        2
    ) AS churn_rate_pct
FROM customers
GROUP BY Contract
ORDER BY churn_rate_pct DESC
"""

AVG_TENURE = """
SELECT ROUND(AVG(tenure), 2) AS average_tenure
FROM customers
"""

AVG_MONTHLY_CHARGES = """
SELECT ROUND(AVG(MonthlyCharges), 2) AS average_monthly_charges
FROM customers
"""
