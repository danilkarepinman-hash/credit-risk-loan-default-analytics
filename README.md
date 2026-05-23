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