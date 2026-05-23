import pandas as pd
import sqlite3
import os

# =========================
# 1. Load featured dataset
# =========================

loans = pd.read_csv('../data/processed/loans_featured.csv')

# =========================
# 2. Create SQLite database
# =========================

db_path = '../data/processed/credit_risk.db'

# Recreate database if it already exists
if os.path.exists(db_path):
    os.remove(db_path)

conn = sqlite3.connect(db_path)

# =========================
# 3. Save DataFrame as SQL table
# =========================

loans.to_sql('loans', conn, index=False, if_exists='replace')

# =========================
# 4. Check tables
# =========================

tables_query = """
SELECT name
FROM sqlite_master
WHERE type = 'table';
"""

tables = pd.read_sql_query(tables_query, conn)

print('TABLES IN DATABASE:')
print(tables)

print('\nROW COUNT:')

row_count_query = """
SELECT COUNT(*) AS row_count
FROM loans;
"""

row_count = pd.read_sql_query(row_count_query, conn)
print(row_count)

# =========================
# 5. Test analytical SQL query
# =========================

test_query = """
SELECT
    risk_level,
    COUNT(*) AS total_loans,
    SUM(default_flag) AS defaulted_loans,
    ROUND(AVG(default_flag) * 100, 2) AS default_rate_pct,
    ROUND(AVG(risk_score), 2) AS avg_risk_score
FROM loans
GROUP BY risk_level
ORDER BY default_rate_pct DESC;
"""

test_result = pd.read_sql_query(test_query, conn)

print('\nTEST QUERY RESULT:')
print(test_result)

conn.close()

print('\nSQLite database created successfully:')
print(db_path)