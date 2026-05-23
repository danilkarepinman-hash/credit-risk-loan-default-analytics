import pandas as pd

# =========================
# 1. Load featured dataset
# =========================

loans = pd.read_csv('../data/processed/loans_featured.csv')

print('TABLE SHAPE:')
print(loans.shape)


# =========================
# 2. Missing values check
# =========================

print('\nMISSING VALUES:')
print(loans.isna().sum())


# =========================
# 3. Duplicate checks
# =========================

print('\nDUPLICATES:')
print('Full row duplicates:', loans.duplicated().sum())
print('Duplicate loan_id:', loans['loan_id'].duplicated().sum())


# =========================
# 4. Primary key check
# =========================

print('\nPRIMARY KEY CHECK:')
print('Unique loan_id:', loans['loan_id'].nunique())
print('Total rows:', len(loans))


# =========================
# 5. Default flag validation
# =========================

print('\nDEFAULT FLAG DISTRIBUTION:')
print(loans['default_flag'].value_counts())

print('\nDEFAULT STATUS DISTRIBUTION:')
print(loans['default_status'].value_counts())


# =========================
# 6. Risk level validation
# =========================

print('\nRISK LEVEL DISTRIBUTION:')
print(loans['risk_level'].value_counts())

risk_validation = (
    loans
    .groupby('risk_level', observed=True)
    .agg(
        total_loans=('loan_id', 'count'),
        defaulted_loans=('default_flag', 'sum'),
        default_rate=('default_flag', 'mean'),
        avg_risk_score=('risk_score', 'mean')
    )
    .reset_index()
)

risk_validation['default_rate'] = (risk_validation['default_rate'] * 100).round(2)
risk_validation['avg_risk_score'] = risk_validation['avg_risk_score'].round(2)

print('\nRISK LEVEL VALIDATION:')
print(risk_validation)


# =========================
# 7. Segment checks
# =========================

segment_columns = [
    'age_group',
    'income_segment',
    'loan_amount_segment',
    'interest_rate_segment',
    'loan_to_income_segment',
    'credit_history_segment',
    'employment_length_segment'
]

print('\nSEGMENT VALUE COUNTS:')

for col in segment_columns:
    print(f'\n{col.upper()}:')
    print(loans[col].value_counts())


# =========================
# 8. Numeric sanity checks
# =========================

print('\nNUMERIC SUMMARY:')
print(
    loans[
        [
            'age',
            'annual_income',
            'employment_length',
            'loan_amount',
            'interest_rate',
            'loan_to_income_ratio',
            'credit_history_length',
            'risk_score'
        ]
    ].describe()
)


# =========================
# 9. Final validation result
# =========================

if (
    loans.isna().sum().sum() == 0
    and loans.duplicated().sum() == 0
    and loans['loan_id'].duplicated().sum() == 0
):
    print('\nVALIDATION RESULT: Dataset is clean and ready for analysis.')
else:
    print('\nVALIDATION RESULT: Dataset requires additional checks.')