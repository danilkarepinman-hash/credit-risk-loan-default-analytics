import pandas as pd
import numpy as np
import os

# =========================
# 1. Load cleaned dataset
# =========================

loans = pd.read_csv('../data/processed/loans_cleaned.csv')

print('INPUT SHAPE:')
print(loans.shape)

print('\nINPUT COLUMNS:')
print(loans.columns)


# =========================
# 2. Age groups
# =========================

loans['age_group'] = pd.cut(
    loans['age'],
    bins=[17, 25, 35, 45, 60, 100],
    labels=['18-25', '26-35', '36-45', '46-60', '60+']
)


# =========================
# 3. Income segments
# =========================

loans['income_segment'] = pd.cut(
    loans['annual_income'],
    bins=[0, 30000, 60000, 100000, 200000, np.inf],
    labels=['Low Income', 'Lower-Mid Income', 'Mid Income', 'Upper-Mid Income', 'High Income']
)


# =========================
# 4. Loan amount segments
# =========================

loans['loan_amount_segment'] = pd.cut(
    loans['loan_amount'],
    bins=[0, 5000, 10000, 15000, 25000, np.inf],
    labels=['Very Small Loan', 'Small Loan', 'Medium Loan', 'Large Loan', 'Very Large Loan']
)


# =========================
# 5. Interest rate segments
# =========================

loans['interest_rate_segment'] = pd.cut(
    loans['interest_rate'],
    bins=[0, 8, 12, 16, 20, np.inf],
    labels=['Very Low Rate', 'Low Rate', 'Medium Rate', 'High Rate', 'Very High Rate']
)


# =========================
# 6. Loan-to-income ratio segments
# =========================

loans['loan_to_income_segment'] = pd.cut(
    loans['loan_to_income_ratio'],
    bins=[0, 0.10, 0.20, 0.30, 0.50, np.inf],
    labels=['Very Low DTI', 'Low DTI', 'Medium DTI', 'High DTI', 'Very High DTI'],
    include_lowest=True
)


# =========================
# 7. Credit history segments
# =========================

loans['credit_history_segment'] = pd.cut(
    loans['credit_history_length'],
    bins=[0, 3, 6, 10, 20, np.inf],
    labels=['Very Short History', 'Short History', 'Medium History', 'Long History', 'Very Long History'],
    include_lowest=True
)


# =========================
# 8. Employment length segments
# =========================

loans['employment_length_segment'] = pd.cut(
    loans['employment_length'],
    bins=[-1, 1, 3, 5, 10, 50],
    labels=['0-1 Years', '2-3 Years', '4-5 Years', '6-10 Years', '10+ Years']
)


# =========================
# 9. Risk score logic
# =========================
# Important: this is a rule-based analytical score.
# It does not use default_flag directly to avoid target leakage.

grade_score_map = {
    'A': 5,
    'B': 10,
    'C': 20,
    'D': 35,
    'E': 50,
    'F': 65,
    'G': 80
}

loans['grade_risk_score'] = loans['loan_grade'].map(grade_score_map).fillna(20)

loans['interest_risk_score'] = np.where(
    loans['interest_rate'] >= 20, 20,
    np.where(loans['interest_rate'] >= 16, 15,
    np.where(loans['interest_rate'] >= 12, 10, 5))
)

loans['dti_risk_score'] = np.where(
    loans['loan_to_income_ratio'] >= 0.50, 25,
    np.where(loans['loan_to_income_ratio'] >= 0.30, 20,
    np.where(loans['loan_to_income_ratio'] >= 0.20, 10, 5))
)

loans['previous_default_risk_score'] = np.where(
    loans['previous_default_flag'] == 'Y',
    15,
    0
)

loans['income_risk_score'] = np.where(
    loans['annual_income'] < 30000,
    10,
    0
)

loans['risk_score'] = (
    loans['grade_risk_score'] +
    loans['interest_risk_score'] +
    loans['dti_risk_score'] +
    loans['previous_default_risk_score'] +
    loans['income_risk_score']
)

loans['risk_score'] = loans['risk_score'].clip(lower=0, upper=100)


# =========================
# 10. Risk level
# =========================

loans['risk_level'] = pd.cut(
    loans['risk_score'],
    bins=[0, 25, 50, 75, 100],
    labels=['Low Risk', 'Medium Risk', 'High Risk', 'Very High Risk'],
    include_lowest=True
)


# =========================
# 11. Final checks
# =========================

print('\nOUTPUT SHAPE:')
print(loans.shape)

print('\nNEW COLUMNS:')
new_columns = [
    'age_group',
    'income_segment',
    'loan_amount_segment',
    'interest_rate_segment',
    'loan_to_income_segment',
    'credit_history_segment',
    'employment_length_segment',
    'risk_score',
    'risk_level'
]
print(loans[new_columns].head())

print('\nMISSING VALUES IN NEW COLUMNS:')
print(loans[new_columns].isna().sum())

print('\nRISK LEVEL DISTRIBUTION:')
print(loans['risk_level'].value_counts())

print('\nDEFAULT RATE BY RISK LEVEL:')
default_by_risk = (
    loans
    .groupby('risk_level', observed=True)
    .agg(
        total_loans=('loan_id', 'count'),
        defaulted_loans=('default_flag', 'sum'),
        default_rate=('default_flag', 'mean')
    )
    .reset_index()
)

default_by_risk['default_rate'] = (default_by_risk['default_rate'] * 100).round(2)

print(default_by_risk)


# =========================
# 12. Save featured dataset
# =========================

output_dir = '../data/processed'
os.makedirs(output_dir, exist_ok=True)

output_path = f'{output_dir}/loans_featured.csv'

loans.to_csv(output_path, index=False)

print('\nSaved featured file:')
print(output_path)