-- =====================================================
-- 03_segment_analysis.sql
-- Credit Risk & Loan Default Analytics
-- Purpose: Analyze borrower segments and default patterns
-- =====================================================


-- 1. Default rate by income segment

SELECT
    income_segment,
    COUNT(*) AS total_loans,
    SUM(default_flag) AS defaulted_loans,
    ROUND(AVG(default_flag) * 100, 2) AS default_rate_pct,
    ROUND(AVG(annual_income), 2) AS avg_annual_income,
    ROUND(AVG(loan_amount), 2) AS avg_loan_amount,
    ROUND(AVG(risk_score), 2) AS avg_risk_score
FROM loans
GROUP BY income_segment
ORDER BY 4 DESC;


-- 2. Default rate by age group

SELECT
    age_group,
    COUNT(*) AS total_loans,
    SUM(default_flag) AS defaulted_loans,
    ROUND(AVG(default_flag) * 100, 2) AS default_rate_pct,
    ROUND(AVG(age), 2) AS avg_age,
    ROUND(AVG(loan_amount), 2) AS avg_loan_amount,
    ROUND(AVG(risk_score), 2) AS avg_risk_score
FROM loans
GROUP BY age_group
ORDER BY 4 DESC;


-- 3. Default rate by home ownership

SELECT
    home_ownership,
    COUNT(*) AS total_loans,
    SUM(default_flag) AS defaulted_loans,
    ROUND(AVG(default_flag) * 100, 2) AS default_rate_pct,
    ROUND(AVG(annual_income), 2) AS avg_annual_income,
    ROUND(AVG(loan_amount), 2) AS avg_loan_amount,
    ROUND(AVG(risk_score), 2) AS avg_risk_score
FROM loans
GROUP BY home_ownership
ORDER BY 4 DESC;


-- 4. Default rate by employment length segment

SELECT
    employment_length_segment,
    COUNT(*) AS total_loans,
    SUM(default_flag) AS defaulted_loans,
    ROUND(AVG(default_flag) * 100, 2) AS default_rate_pct,
    ROUND(AVG(employment_length), 2) AS avg_employment_length,
    ROUND(AVG(annual_income), 2) AS avg_annual_income,
    ROUND(AVG(risk_score), 2) AS avg_risk_score
FROM loans
GROUP BY employment_length_segment
ORDER BY 4 DESC;


-- 5. Default rate by credit history segment

SELECT
    credit_history_segment,
    COUNT(*) AS total_loans,
    SUM(default_flag) AS defaulted_loans,
    ROUND(AVG(default_flag) * 100, 2) AS default_rate_pct,
    ROUND(AVG(credit_history_length), 2) AS avg_credit_history_length,
    ROUND(AVG(loan_amount), 2) AS avg_loan_amount,
    ROUND(AVG(risk_score), 2) AS avg_risk_score
FROM loans
GROUP BY credit_history_segment
ORDER BY 4 DESC;


-- 6. Default rate by loan-to-income segment

SELECT
    loan_to_income_segment,
    COUNT(*) AS total_loans,
    SUM(default_flag) AS defaulted_loans,
    ROUND(AVG(default_flag) * 100, 2) AS default_rate_pct,
    ROUND(AVG(loan_to_income_ratio), 2) AS avg_loan_to_income_ratio,
    ROUND(AVG(loan_amount), 2) AS avg_loan_amount,
    ROUND(AVG(risk_score), 2) AS avg_risk_score
FROM loans
GROUP BY loan_to_income_segment
ORDER BY 4 DESC;


-- 7. Combined risk: income segment + loan grade

SELECT
    income_segment,
    loan_grade,
    COUNT(*) AS total_loans,
    SUM(default_flag) AS defaulted_loans,
    ROUND(AVG(default_flag) * 100, 2) AS default_rate_pct,
    ROUND(AVG(interest_rate), 2) AS avg_interest_rate,
    ROUND(AVG(risk_score), 2) AS avg_risk_score
FROM loans
GROUP BY
    income_segment,
    loan_grade
HAVING COUNT(*) >= 50
ORDER BY default_rate_pct DESC;


-- 8. Combined risk: loan purpose + risk level

SELECT
    loan_purpose,
    risk_level,
    COUNT(*) AS total_loans,
    SUM(default_flag) AS defaulted_loans,
    ROUND(AVG(default_flag) * 100, 2) AS default_rate_pct,
    SUM(CASE WHEN default_flag = 1 THEN loan_amount ELSE 0 END) AS defaulted_loan_amount,
    ROUND(AVG(risk_score), 2) AS avg_risk_score
FROM loans
GROUP BY
    loan_purpose,
    risk_level
HAVING COUNT(*) >= 50
ORDER BY default_rate_pct DESC;


-- 9. Highest default amount segments

SELECT
    income_segment,
    loan_purpose,
    risk_level,
    COUNT(*) AS total_loans,
    SUM(default_flag) AS defaulted_loans,
    ROUND(AVG(default_flag) * 100, 2) AS default_rate_pct,
    SUM(loan_amount) AS total_loan_amount,
    SUM(CASE WHEN default_flag = 1 THEN loan_amount ELSE 0 END) AS defaulted_loan_amount
FROM loans
GROUP BY
    income_segment,
    loan_purpose,
    risk_level
HAVING COUNT(*) >= 50
ORDER BY defaulted_loan_amount DESC
LIMIT 20;