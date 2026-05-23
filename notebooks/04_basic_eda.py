import pandas as pd
import os

# =========================
# 1. Load featured dataset
# =========================

loans = pd.read_csv('../data/processed/loans_featured.csv')

output_dir = '../reports/eda_outputs'
os.makedirs(output_dir, exist_ok=True)


# =========================
# 2. Helper function
# =========================

def default_analysis(df, group_col):
    result = (
        df
        .groupby(group_col, observed=True)
        .agg(
            total_loans=('loan_id', 'count'),
            defaulted_loans=('default_flag', 'sum'),
            total_loan_amount=('loan_amount', 'sum'),
            defaulted_loan_amount=('loan_amount', lambda x: x[df.loc[x.index, 'default_flag'] == 1].sum()),
            avg_loan_amount=('loan_amount', 'mean'),
            avg_interest_rate=('interest_rate', 'mean'),
            avg_risk_score=('risk_score', 'mean'),
            default_rate=('default_flag', 'mean')
        )
        .reset_index()
    )

    result['default_rate'] = (result['default_rate'] * 100).round(2)
    result['avg_loan_amount'] = result['avg_loan_amount'].round(2)
    result['avg_interest_rate'] = result['avg_interest_rate'].round(2)
    result['avg_risk_score'] = result['avg_risk_score'].round(2)

    return result.sort_values('default_rate', ascending=False)


# =========================
# 3. Portfolio overview
# =========================

portfolio_overview = pd.DataFrame({
    'metric': [
        'total_loans',
        'total_loan_amount',
        'defaulted_loans',
        'defaulted_loan_amount',
        'default_rate_pct',
        'average_loan_amount',
        'average_interest_rate',
        'average_risk_score'
    ],
    'value': [
        loans['loan_id'].count(),
        loans['loan_amount'].sum(),
        loans['default_flag'].sum(),
        loans.loc[loans['default_flag'] == 1, 'loan_amount'].sum(),
        round(loans['default_flag'].mean() * 100, 2),
        round(loans['loan_amount'].mean(), 2),
        round(loans['interest_rate'].mean(), 2),
        round(loans['risk_score'].mean(), 2)
    ]
})

portfolio_overview.to_csv(f'{output_dir}/portfolio_overview.csv', index=False)


# =========================
# 4. Default analysis by key segments
# =========================

analysis_map = {
    'risk_level': 'default_by_risk_level.csv',
    'loan_grade': 'default_by_loan_grade.csv',
    'income_segment': 'default_by_income_segment.csv',
    'loan_purpose': 'default_by_loan_purpose.csv',
    'interest_rate_segment': 'default_by_interest_rate_segment.csv',
    'loan_to_income_segment': 'default_by_loan_to_income_segment.csv',
    'home_ownership': 'default_by_home_ownership.csv',
    'age_group': 'default_by_age_group.csv',
    'credit_history_segment': 'default_by_credit_history_segment.csv',
    'employment_length_segment': 'default_by_employment_length_segment.csv',
    'previous_default_status': 'default_by_previous_default_status.csv'
}

for group_col, file_name in analysis_map.items():
    result = default_analysis(loans, group_col)
    result.to_csv(f'{output_dir}/{file_name}', index=False)


# =========================
# 5. Loan amount by purpose
# =========================

loan_amount_by_purpose = (
    loans
    .groupby('loan_purpose', observed=True)
    .agg(
        total_loans=('loan_id', 'count'),
        total_loan_amount=('loan_amount', 'sum'),
        avg_loan_amount=('loan_amount', 'mean'),
        default_rate=('default_flag', 'mean')
    )
    .reset_index()
)

loan_amount_by_purpose['avg_loan_amount'] = loan_amount_by_purpose['avg_loan_amount'].round(2)
loan_amount_by_purpose['default_rate'] = (loan_amount_by_purpose['default_rate'] * 100).round(2)

loan_amount_by_purpose = loan_amount_by_purpose.sort_values(
    'total_loan_amount',
    ascending=False
)

loan_amount_by_purpose.to_csv(f'{output_dir}/loan_amount_by_purpose.csv', index=False)


# =========================
# 6. Print key outputs
# =========================

print('PORTFOLIO OVERVIEW:')
print(portfolio_overview)

print('\nDEFAULT BY RISK LEVEL:')
print(default_analysis(loans, 'risk_level'))

print('\nDEFAULT BY LOAN GRADE:')
print(default_analysis(loans, 'loan_grade'))

print('\nDEFAULT BY INCOME SEGMENT:')
print(default_analysis(loans, 'income_segment'))

print('\nDEFAULT BY LOAN PURPOSE:')
print(default_analysis(loans, 'loan_purpose'))

print('\nEDA files saved to:')
print(output_dir)