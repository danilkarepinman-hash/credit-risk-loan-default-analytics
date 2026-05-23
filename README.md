# Retail Banking Churn & Sales Analytics

## Project Overview

This project analyzes customer churn, sales performance, product performance, channel conversion, and branch/manager performance in a simulated retail banking environment.

The main goal of the project is to identify customer segments with high churn risk and evaluate sales performance across banking products, sales channels, branches, and managers.

---

## Business Problem

Retail banks need to reduce customer churn, improve sales conversion, and identify profitable customer segments.

This project answers the following business questions:

- What is the overall customer churn rate?
- Which customer segments have the highest churn rate?
- Which regions have the highest churn risk?
- Which products generate the highest sales amount?
- Which sales channels have the best conversion rate?
- Which branches and managers perform best?

---

## Dataset

The main customer churn dataset was taken from a public banking churn dataset.

Additional tables were synthetically generated to simulate a realistic retail banking analytics environment:

- `customers`
- `products`
- `managers`
- `sales`

The synthetic tables were used to analyze sales, products, channels, branches, and manager performance.

---

## Tools Used

- Python
- pandas
- SQLite
- DBeaver
- SQL
- Power BI
- DAX
- GitHub

---

## Project Structure

```text
banking-churn-sales-analytics/
│
├── data/
│   ├── raw/
│   │   └── customers_raw.csv
│   │
│   └── processed/
│       ├── customers_cleaned.csv
│       ├── products.csv
│       ├── managers.csv
│       ├── sales.csv
│       └── banking_analytics.db
│
├── notebooks/
│   ├── 01_data_cleaning.py
│   ├── 02_create_support_tables.py
│   ├── 03_validate_tables.py
│   ├── 04_basic_eda.py
│   ├── 05_create_sqlite_database.py
│   └── 06_run_sql_checks.py
│
├── sql/
│   ├── 01_data_quality_checks.sql
│   ├── 02_churn_analysis.sql
│   ├── 03_sales_analysis.sql
│   └── 04_manager_analysis.sql
│
├── powerbi/
│   ├── banking_churn_sales_dashboard.pbix
│   └── screenshots/
│       ├── 01_executive_overview.png
│       ├── 02_churn_analysis.png
│       └── 03_sales_performance.png
│
├── reports/
│   ├── business_insights.md
│   └── eda_outputs/
│
└── README.md
```

---

## Data Model

The Power BI model uses a simple star schema:

```text
customers 1 → * sales
products  1 → * sales
managers  1 → * sales
```

- `sales` is the fact table.
- `customers`, `products`, and `managers` are dimension tables.

---

## SQL Analysis

The SQL part of the project includes several analytical blocks.

### 1. Data Quality Checks

File:

```text
sql/01_data_quality_checks.sql
```

Includes:

- row counts
- duplicate checks
- missing value checks
- relationship checks between tables

### 2. Customer Churn Analysis

File:

```text
sql/02_churn_analysis.sql
```

Includes:

- overall churn rate
- churn by age group
- churn by region
- churn by balance segment
- churn by activity status
- churn by number of products
- churn by credit score segment

### 3. Sales Analysis

File:

```text
sql/03_sales_analysis.sql
```

Includes:

- sales overview
- sales by product
- sales by channel
- sales by month
- sales by region
- sales by branch

### 4. Manager Analysis

File:

```text
sql/04_manager_analysis.sql
```

Includes:

- manager performance ranking
- branch performance
- city performance
- ranking using SQL window functions

---

## Power BI Dashboard

The dashboard contains 3 pages.

### 1. Executive Overview

Shows high-level KPIs:

- Total Customers
- Churn Rate
- Total Sales Amount
- Conversion Rate
- Average Ticket

![Executive Overview](powerbi/screenshots/01_executive_overview.png)

---

### 2. Churn Analysis

Shows customer churn by:

- Region
- Activity Status
- Balance Segment
- Number of Products
- Credit Score Segment

![Churn Analysis](powerbi/screenshots/02_churn_analysis.png)

---

### 3. Sales Performance

Shows sales performance by:

- Product
- Channel
- Branch
- Manager

![Sales Performance](powerbi/screenshots/03_sales_performance.png)

---

## Key Insights

1. The overall customer churn rate is **20.37%**.
2. Germany has the highest churn rate among all regions.
3. Inactive customers are more likely to churn than active customers.
4. Premium balance customers show high churn risk.
5. Customers with 3–4 products show unusually high churn and require deeper investigation.
6. The Online channel has the highest conversion rate.
7. Credit Card and Deposit products generate strong sales volume.
8. Branch performance differs across cities.

---

## Business Recommendations

1. Focus retention campaigns on high-risk churn segments.
2. Investigate the reasons behind high churn in Germany.
3. Launch reactivation campaigns for inactive customers.
4. Create personalized retention offers for premium balance customers.
5. Analyze multi-product customers to identify possible overselling or product mismatch.
6. Scale digital sales campaigns because the Online channel shows strong conversion.
7. Transfer best practices from high-performing branches to lower-performing branches.

---

## Final Result

This project demonstrates an end-to-end data analytics workflow:

```text
Raw Data → Data Cleaning → Data Modeling → SQL Analysis → Power BI Dashboard → Business Insights
```

The project combines technical skills with business thinking in the retail banking domain.
