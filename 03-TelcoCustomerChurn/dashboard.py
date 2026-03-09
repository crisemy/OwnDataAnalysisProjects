import streamlit as st
import pandas as pd
import sqlite3

from src.queries import (
    TOTAL_CUSTOMERS,
    CHURN_RATE,
    CHURN_BY_CONTRACT,
    AVG_TENURE,
    AVG_MONTHLY_CHARGES
)

# -------------------------
# Page configuration
# -------------------------
st.set_page_config(
    page_title="Telco Customer Churn Dashboard",
    layout="wide"
)

st.title("Telco Customer Churn Dashboard")

# -------------------------
# Database connection
# -------------------------
conn = sqlite3.connect("data/telco_customer_churn.db")

# -------------------------
# Sidebar filters
# -------------------------
st.sidebar.header("Filters")

contract_options = pd.read_sql_query(
    "SELECT DISTINCT Contract FROM customers;",
    conn
)["Contract"].tolist()
contract_options.insert(0, "All")

selected_contract = st.sidebar.selectbox(
    "Contract Type",
    contract_options
)

selected_churn = st.sidebar.selectbox(
    "Churn Status",
    ["All", "Yes", "No"]
)

# -------------------------
# Build dynamic WHERE clause
# -------------------------
filters = []

if selected_contract != "All":
    filters.append(f"Contract = '{selected_contract}'")

if selected_churn != "All":
    filters.append(f"Churn = '{selected_churn}'")

where_clause = ""
if filters:
    where_clause = " WHERE " + " AND ".join(filters)

# -------------------------
# Load KPI values (using existing queries)
# -------------------------
total_customers = pd.read_sql_query(
    TOTAL_CUSTOMERS + where_clause,
    conn
).iloc[0, 0]

churn_rate = pd.read_sql_query(
    CHURN_RATE + where_clause,
    conn
).iloc[0, 0]

avg_tenure = pd.read_sql_query(
    AVG_TENURE + where_clause,
    conn
).iloc[0, 0]

avg_monthly_charges = pd.read_sql_query(
    AVG_MONTHLY_CHARGES + where_clause,
    conn
).iloc[0, 0]

# -------------------------
# KPI Cards
# -------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Customers", f"{total_customers:,}")
col2.metric("Churn Rate (%)", f"{churn_rate}%")
col3.metric("Average Tenure (months)", avg_tenure)
col4.metric("Avg Monthly Charges ($)", avg_monthly_charges)

st.divider()

# -------------------------
# Churn by Contract Type
# -------------------------
st.subheader("Churn Rate by Contract Type")

if selected_churn == "All":
    # Consulta sin filtro (la de queries.py)
    churn_by_contract_df = pd.read_sql_query(CHURN_BY_CONTRACT, conn)
else:
    # Consulta con filtro correcto (WHERE antes de GROUP BY)
    query_churn_by_contract = """
    SELECT
        Contract,
        ROUND(
            100.0 * AVG(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END),
            2
        ) AS churn_rate_pct
    FROM customers
    WHERE Churn = ?
    GROUP BY Contract
    ORDER BY churn_rate_pct DESC
    """
    churn_by_contract_df = pd.read_sql_query(
        query_churn_by_contract,
        conn,
        params=[selected_churn]
    )

st.dataframe(churn_by_contract_df, use_container_width=True)
st.bar_chart(churn_by_contract_df.set_index("Contract"))

conn.close()
