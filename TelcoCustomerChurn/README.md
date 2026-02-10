# Telco Customer Churn Analysis

## Project Overview
This project analyzes customer churn behavior in a telecommunications company.
The goal is to identify key churn drivers and present actionable KPIs through an
interactive dashboard.

## Business Questions
- What is the overall churn rate?
- Which contract types are most affected by churn?
- How do tenure and monthly charges relate to customer retention?

## Key KPIs
- Total Customers
- Churn Rate (%)
- Churn Rate by Contract Type
- Average Customer Tenure
- Average Monthly Charges

## Tech Stack
- Python (Pandas, SQLite)
- SQL
- Streamlit
- Jupyter Notebook

## Project Structure
- Exploratory analysis and KPI validation in Jupyter Notebook
- KPI computation using SQL (SQLite)
- Interactive dashboard built with Streamlit

## How to Run
```bash
streamlit run dashboard.py
```
## Dashboard Features
- Interactive filters (Contract Type, Churn Status)
- KPI cards for quick insights
- Churn distribution by contract type

## Key Takeaways
- Month-to-month contracts show significantly higher churn rates
- Longer tenure correlates with lower churn
- Higher monthly charges tend to increase churn probability