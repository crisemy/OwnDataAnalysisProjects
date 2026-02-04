import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

# ── Page config
st.set_page_config(page_title="Superstore Sales Dashboard", layout="wide")

# ── Custom styling (light background, better spacing)
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .block-container { padding-top: 1rem !important; }
    h1, h2, h3 { color: #2c3e50; }
    </style>
""", unsafe_allow_html=True)

# ── Title & intro
st.title("🛒 Superstore Sales Dashboard")
st.markdown("Interactive exploration of sales, regions, categories & key metrics — powered by SQLite + Pandas + Streamlit + Plotly")

# ── Database connection (cached)
@st.cache_resource
def get_connection():
    return sqlite3.connect("superstore.db")  # ← change to absolute path if needed

conn = get_connection()

# ── Helper function to run SQL and format
@st.cache_data
def run_query(sql):
    df = pd.read_sql_query(sql, conn)
    if 'total_sales' in df.columns:
        df['total_sales'] = df['total_sales'].round(2)
    return df

# ── Load main data: Sales by Region
region_query = """
SELECT "Region", SUM("Sales") AS total_sales
FROM orders
GROUP BY "Region"
ORDER BY total_sales DESC;
"""
df_region = run_query(region_query)

# ── Load category data
category_query = """
SELECT "Category", SUM("Sales") AS total_sales
FROM orders
GROUP BY "Category"
ORDER BY total_sales DESC;
"""
df_category = run_query(category_query)

# ── Sidebar filters
with st.sidebar:
    st.header("Filters")
    regions = ["All"] + df_region["Region"].unique().tolist()
    selected_region = st.selectbox("Region", regions, index=0)

# ── Apply region filter (if not All)
if selected_region != "All":
    filtered_region = df_region[df_region["Region"] == selected_region]
else:
    filtered_region = df_region.copy()

# ── Layout: two columns for main content
col_left, col_right = st.columns([3, 2])

with col_left:
    # ── KPI cards
    st.subheader("Key Metrics")
    kpi1, kpi2 = st.columns(2)

    total_sales_all = df_region["total_sales"].sum()
    with kpi1:
        st.metric("Total Sales", f"${total_sales_all:,.0f}")

    if not filtered_region.empty:
        top_reg = filtered_region.iloc[0]["Region"]
        top_reg_sales = filtered_region.iloc[0]["total_sales"]
        with kpi2:
            st.metric("Top Region", top_reg, f"${top_reg_sales:,.0f}")
    else:
        st.warning("No data for selected region")

    # ── Region bar chart
    st.subheader("Sales by Region")
    fig_region = px.bar(
        filtered_region,
        x="Region",
        y="total_sales",
        title=f"Sales by Region {'' if selected_region == 'All' else f'— {selected_region}'}",
        labels={"Region": "Region", "total_sales": "Total Sales (USD)"},
        color="total_sales",
        color_continuous_scale="Viridis",
        text_auto=True
    )
    fig_region.update_layout(
        xaxis_title="Region",
        yaxis_title="Total Sales",
        bargap=0.25,
        height=480
    )
    st.plotly_chart(fig_region, width="stretch")

with col_right:
    # ── Category bar chart
    st.subheader("Sales by Category")
    fig_cat = px.bar(
        df_category,
        x="Category",
        y="total_sales",
        title="Sales Breakdown by Category",
        labels={"Category": "Category", "total_sales": "Total Sales"},
        color="total_sales",
        color_continuous_scale="Plasma",
        text_auto=True
    )
    fig_cat.update_layout(
        xaxis_title="Category",
        yaxis_title="Total Sales",
        bargap=0.3,
        height=480
    )
    st.plotly_chart(fig_cat, width="stretch")

    # ── Raw region data table
    st.subheader("Region Data")
    st.dataframe(
        df_region.style.format({"total_sales": "${:,.2f}"}),
        use_container_width=True
    )

# ── Footer
st.markdown("---")
st.caption("Data: Superstore dataset | Built it using Python, Streamlit & Plotly | Feb 2026 | by crisemy (@gmail.com)")

# Optional: uncomment if you want to see raw columns during debugging
# st.write("Debug columns (region):", df_region.columns.tolist())
# st.write("Debug columns (category):", df_category.columns.tolist())

# conn.close()  # usually not needed with @cache_resource