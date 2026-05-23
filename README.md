# Credit Risk & Loan Default Analytics

## Project Overview

This project analyzes credit risk and loan default patterns using Python, SQL, SQLite, and Power BI.

The main goal is to identify high-risk borrower segments, understand the key drivers of loan default, and create a dashboard that supports data-driven credit risk decisions.

The project includes the full analytical workflow:

- Data cleaning and preprocessing with Python
- Feature engineering and risk score creation
- Data validation
- Exploratory data analysis
- SQLite database creation
- SQL-based business analysis
- Power BI dashboard development
- Business insights and recommendations

---

## Business Problem

Credit institutions need to reduce loan default risk, identify risky borrower segments, and improve loan approval decisions.

This project answers the following business questions:

- What is the overall default rate in the loan portfolio?
- Which borrower segments have the highest default risk?
- How do loan grade, income, interest rate, and loan-to-income ratio affect default probability?
- Which loan purposes are associated with higher default rates?
- Can a rule-based risk score separate low-risk and high-risk borrowers?
- What actions should be recommended for each risk group?

---

## Tools Used

- Python
- pandas
- NumPy
- SQLite
- SQL
- DBeaver
- Power BI
- Markdown
- PyCharm
- GitHub

---

## Dataset

The dataset contains loan and borrower information, including:

- Borrower age
- Annual income
- Home ownership status
- Employment length
- Loan purpose
- Loan grade
- Loan amount
- Interest rate
- Loan-to-income ratio
- Previous default status
- Credit history length
- Loan default status

Raw dataset:

```text
data/raw/loans_raw.csv
```

Processed datasets:

```text
data/processed/loans_cleaned.csv
data/processed/loans_featured.csv
data/processed/credit_risk.db
```

---

## Project Structure

```text
credit-risk-loan-default-analytics/
│
├── data/
│   ├── raw/
│   │   └── loans_raw.csv
│   │
│   └── processed/
│       ├── loans_cleaned.csv
│       ├── loans_featured.csv
│       └── credit_risk.db
│
├── notebooks/
│   ├── 01_data_cleaning.py
│   ├── 02_feature_engineering.py
│   ├── 03_validate_dataset.py
│   ├── 04_basic_eda.py
│   └── 05_create_sqlite_database.py
│
├── sql/
│   ├── 01_portfolio_overview.sql
│   ├── 02_default_analysis.sql
│   ├── 03_segment_analysis.sql
│   └── 04_risk_recommendations.sql
│
├── reports/
│   ├── business_insights.md
│   ├── data_dictionary.md
│   └── eda_outputs/
│
├── powerbi/
│   ├── credit_risk_dashboard.pbix
│   └── screenshots/
│       ├── 01_credit_portfolio_overview.png
│       ├── 02_default_risk_analysis.png
│       ├── 03_borrower_segments.png
│       └── 04_high_risk_borrowers.png
│
├── requirements.txt
└── README.md
```

---

## Data Cleaning

Data cleaning was performed in Python using pandas.

Main cleaning steps:

- Loaded raw loan dataset
- Removed duplicate rows
- Renamed columns into readable business names
- Filled missing employment length values
- Filled missing interest rate values
- Removed unrealistic values
- Created unique `loan_id`
- Created readable default status fields
- Validated missing values and duplicates

Final cleaned dataset:

```text
data/processed/loans_cleaned.csv
```

---

## Feature Engineering

Several analytical features were created to support credit risk analysis.

Created segments:

- Age group
- Income segment
- Loan amount segment
- Interest rate segment
- Loan-to-income segment
- Credit history segment
- Employment length segment

A rule-based risk score was created using:

- Loan grade
- Interest rate
- Loan-to-income ratio
- Previous default history
- Income level

The final risk score was grouped into four risk levels:

| Risk Level | Description |
|---|---|
| Low Risk | Safer borrowers |
| Medium Risk | Moderate risk borrowers |
| High Risk | Risky borrowers |
| Very High Risk | Highest-risk borrowers |

Final featured dataset:

```text
data/processed/loans_featured.csv
```

---

## Key Metrics

| Metric | Value |
|---|---:|
| Total Loans | 32,411 |
| Total Loan Amount | 310.94M |
| Defaulted Loans | 7,089 |
| Defaulted Loan Amount | 76.97M |
| Default Rate | 21.87% |
| Average Loan Amount | 9.59K |
| Average Interest Rate | 11.02% |
| Average Risk Score | 33.84 |

---

## Main Findings

### 1. Overall Default Rate

The overall portfolio default rate is **21.87%**.

This means that approximately one out of five loans resulted in default.

---

### 2. Risk Level Strongly Separates Borrowers

Default rate by risk level:

| Risk Level | Default Rate |
|---|---:|
| Low Risk | 5.57% |
| Medium Risk | 30.62% |
| High Risk | 51.37% |
| Very High Risk | 74.19% |

Very High Risk borrowers defaulted at a rate of **74.19%**, while Low Risk borrowers defaulted at only **5.57%**.

This confirms that the rule-based risk score successfully separates safer and riskier borrower groups.

---

### 3. Loan Grade Is a Strong Risk Indicator

Default rate increases sharply for lower loan grades.

| Loan Grade | Default Rate |
|---|---:|
| A | 9.96% |
| B | 16.32% |
| C | 20.76% |
| D | 59.06% |
| E | 64.49% |
| F | 70.54% |
| G | 98.44% |

Grades D, E, F, and G represent very high-risk loan categories.

---

### 4. Low Income Borrowers Have Higher Default Risk

Low Income borrowers show the highest default rate.

| Income Segment | Default Rate |
|---|---:|
| Low Income | 45.59% |
| Lower-Mid Income | 23.76% |
| Mid Income | 13.38% |
| High Income | 11.96% |
| Upper-Mid Income | 9.27% |

This suggests that lower-income borrowers require more careful credit assessment, especially when combined with high DTI, poor loan grade, or previous default history.

---

### 5. Loan-to-Income Ratio Is a Key Risk Driver

Borrowers with higher loan-to-income ratios have significantly higher default rates.

Very High DTI and High DTI segments are the riskiest groups.

This means that the relationship between loan size and borrower income should be a key part of loan approval decisions.

---

### 6. Previous Default History Matters

Borrowers with previous defaults show much higher default risk compared with borrowers without previous default records.

Previous default history should be used as an important risk indicator in credit decision-making.

---

### 7. Home Ownership Shows Clear Risk Differences

Renters show higher default risk than borrowers with mortgage or owned property.

Home ownership status can be used as a supporting risk indicator in borrower assessment.

---

### 8. Employment Length Affects Default Risk

Borrowers with shorter employment history have higher default rates.

The highest risk is observed among borrowers with 0–1 years of employment history.

This indicates that job stability is an important borrower quality indicator.

---

## SQL Analysis

SQL analysis was performed using SQLite and DBeaver.

SQL files:

```text
sql/01_portfolio_overview.sql
sql/02_default_analysis.sql
sql/03_segment_analysis.sql
sql/04_risk_recommendations.sql
```

The SQL analysis covers:

- Portfolio overview
- Default rate analysis
- Borrower segment analysis
- Risk level analysis
- Loan grade analysis
- Risk-based recommendations
- High-risk borrower identification

---

## Power BI Dashboard

The Power BI dashboard contains four pages:

1. Credit Portfolio Overview
2. Default Risk Analysis
3. Borrower Segments
4. High Risk Borrowers

Power BI file:

```text
powerbi/credit_risk_dashboard.pbix
```

---

## Dashboard Screenshots

### 1. Credit Portfolio Overview

![Credit Portfolio Overview](./powerbi/screenshots/01_credit_portfolio_overview.png)

---

### 2. Default Risk Analysis

![Default Risk Analysis](./powerbi/screenshots/02_default_risk_analysis.png)

---

### 3. Borrower Segments

![Borrower Segments](./powerbi/screenshots/03_borrower_segments.png)

---

### 4. High Risk Borrowers

![High Risk Borrowers](./powerbi/screenshots/04_high_risk_borrowers.png)

---

## Business Recommendations

### 1. Apply strict manual review for Very High Risk borrowers

Very High Risk borrowers have a default rate of **74.19%**.

Recommended actions:

- Reject automatically in many cases
- Require manual credit review
- Request additional documentation
- Reduce approved loan amount
- Apply stricter DTI limits

---

### 2. Add stronger controls for High Risk borrowers

High Risk borrowers have a default rate of **51.37%**.

Recommended actions:

- Approve only with stronger controls
- Review income stability
- Check previous default history
- Limit loan size
- Monitor repayment behavior more closely

---

### 3. Prioritize Low Risk borrowers

Low Risk borrowers have a default rate of only **5.57%**.

Recommended actions:

- Treat as preferred lending segment
- Offer faster approval
- Use for portfolio growth
- Consider better pricing or cross-sell opportunities

---

### 4. Use loan grade and DTI as key approval signals

Loan grade and loan-to-income ratio are among the strongest default risk indicators.

Recommended actions:

- Tighten approval rules for grades D–G
- Apply maximum DTI thresholds
- Combine grade, income, and DTI in risk policy

---

### 5. Monitor risky loan purposes

Some loan purposes show higher default risk than others.

Recommended actions:

- Monitor risky loan categories separately
- Apply additional checks for high-risk purposes
- Adjust approval rules based on purpose-level risk

---

## Final Conclusion

This project demonstrates an end-to-end credit risk analytics workflow.

The analysis shows that loan default risk is strongly connected with:

- Loan grade
- Borrower income
- Interest rate
- Loan-to-income ratio
- Previous default history
- Home ownership
- Employment length

The rule-based risk score successfully separates borrowers into meaningful risk groups.

The most important finding is that Very High Risk borrowers default at **74.19%**, while Low Risk borrowers default at only **5.57%**.

This project shows how Python, SQL, and Power BI can be used together to clean financial data, create analytical risk segments, identify high-risk borrowers, and support data-driven credit decision-making.
