import pandas as pd
import os

# =========================
# 1. Load raw dataset
# =========================

loans = pd.read_csv('../data/raw/loans_raw.csv')

print('RAW SHAPE:')
print(loans.shape)

print('\nRAW MISSING VALUES:')
print(loans.isna().sum())

print('\nRAW DUPLICATES:')
print(loans.duplicated().sum())


# =========================
# 2. Remove duplicates
# =========================

loans = loans.drop_duplicates()

print('\nSHAPE AFTER REMOVING DUPLICATES:')
print(loans.shape)


# =========================
# 3. Rename columns
# =========================

loans = loans.rename(columns={
    'person_age': 'age',
    'person_income': 'annual_income',
    'person_home_ownership': 'home_ownership',
    'person_emp_length': 'employment_length',
    'loan_intent': 'loan_purpose',
    'loan_grade': 'loan_grade',
    'loan_amnt': 'loan_amount',
    'loan_int_rate': 'interest_rate',
    'loan_status': 'default_flag',
    'loan_percent_income': 'loan_to_income_ratio',
    'cb_person_default_on_file': 'previous_default_flag',
    'cb_person_cred_hist_length': 'credit_history_length'
})


# =========================
# 4. Clean text columns
# =========================

text_columns = [
    'home_ownership',
    'loan_purpose',
    'loan_grade',
    'previous_default_flag'
]

for col in text_columns:
    loans[col] = loans[col].astype(str).str.strip()


loans['loan_grade'] = loans['loan_grade'].str.upper()
loans['home_ownership'] = loans['home_ownership'].str.title()
loans['loan_purpose'] = loans['loan_purpose'].str.title()
loans['previous_default_flag'] = loans['previous_default_flag'].str.upper()


# =========================
# 5. Handle missing values
# =========================

# Fill employment length with median
employment_median = loans['employment_length'].median()
loans['employment_length'] = loans['employment_length'].fillna(employment_median)

# Fill interest rate by median interest rate within each loan grade
loans['interest_rate'] = loans.groupby('loan_grade')['interest_rate'].transform(
    lambda x: x.fillna(x.median())
)

# If any interest_rate values are still missing, fill with overall median
loans['interest_rate'] = loans['interest_rate'].fillna(loans['interest_rate'].median())


# =========================
# 6. Basic data validation / outlier handling
# =========================

# Remove unrealistic age values
loans = loans[(loans['age'] >= 18) & (loans['age'] <= 100)]

# Remove unrealistic income values
loans = loans[loans['annual_income'] > 0]

# Remove unrealistic loan amount values
loans = loans[loans['loan_amount'] > 0]

# Cap employment length if it is unrealistically high
loans['employment_length'] = loans['employment_length'].clip(lower=0, upper=50)


# =========================
# 7. Create readable status columns
# =========================

loans['default_status'] = loans['default_flag'].map({
    1: 'Default',
    0: 'Non-Default'
})

loans['previous_default_status'] = loans['previous_default_flag'].map({
    'Y': 'Previous Default',
    'N': 'No Previous Default'
})


# =========================
# 8. Create loan_id
# =========================

loans = loans.reset_index(drop=True)
loans.insert(0, 'loan_id', range(1, len(loans) + 1))


# =========================
# 9. Final checks
# =========================

print('\nCLEANED SHAPE:')
print(loans.shape)

print('\nCLEANED COLUMNS:')
print(loans.columns)

print('\nCLEANED HEAD:')
print(loans.head())

print('\nCLEANED MISSING VALUES:')
print(loans.isna().sum())

print('\nCLEANED DUPLICATES:')
print(loans.duplicated().sum())

print('\nDEFAULT FLAG DISTRIBUTION:')
print(loans['default_flag'].value_counts())

print('\nDEFAULT RATE:')
print(round(loans['default_flag'].mean() * 100, 2), '%')


# =========================
# 10. Save cleaned dataset
# =========================

output_dir = '../data/processed'
os.makedirs(output_dir, exist_ok=True)

output_path = f'{output_dir}/loans_cleaned.csv'

loans.to_csv(output_path, index=False)

print('\nSaved cleaned file:')
print(output_path)