-- =====================================================
-- 02_default_analysis.sql
-- Credit Risk & Loan Default Analytics
-- Purpose: Analyze loan default rates by key credit risk factors
-- =====================================================


-- 1. Overall default rate

SELECT
    COUNT(*) AS total_loans,
    SUM(default_flag) AS defaulted_loans,
    ROUND(AVG(default_flag) * 100, 2) AS default_rate_pct,
    SUM(loan_amount) AS total_loan_amount,
    SUM(CASE WHEN default_flag = 1 THEN loan_amount ELSE 0 END) AS defaulted_loan_amount
FROM loans;


-- 2. Default rate by risk level

SELECT
    risk_level,
    COUNT(*) AS total_loans,
    SUM(default_flag) AS defaulted_loans,
    ROUND(AVG(default_flag) * 100, 2) AS default_rate_pct,
    ROUND(AVG(risk_score), 2) AS avg_risk_score,
    SUM(CASE WHEN default_flag = 1 THEN loan_amount ELSE 0 END) AS defaulted_loan_amount
FROM loans
GROUP BY risk_level
ORDER BY 4 DESC;


-- 3. Default rate by loan grade

SELECT
    loan_grade,
    COUNT(*) AS total_loans,
    SUM(default_flag) AS defaulted_loans,
    ROUND(AVG(default_flag) * 100, 2) AS default_rate_pct,
    ROUND(AVG(interest_rate), 2) AS avg_interest_rate,
    ROUND(AVG(risk_score), 2) AS avg_risk_score
FROM loans
GROUP BY loan_grade
ORDER BY default_rate_pct DESC;


-- 4. Default rate by interest rate segment

SELECT
    interest_rate_segment,
    COUNT(*) AS total_loans,
    SUM(default_flag) AS defaulted_loans,
    ROUND(AVG(default_flag) * 100, 2) AS default_rate_pct,
    ROUND(AVG(interest_rate), 2) AS avg_interest_rate,
    ROUND(AVG(risk_score), 2) AS avg_risk_score
FROM loans
GROUP BY interest_rate_segment
ORDER BY default_rate_pct DESC;


-- 5. Default rate by loan-to-income segment

SELECT
    loan_to_income_segment,
    COUNT(*) AS total_loans,
    SUM(default_flag) AS defaulted_loans,
    ROUND(AVG(default_flag) * 100, 2) AS default_rate_pct,
    ROUND(AVG(loan_to_income_ratio), 2) AS avg_loan_to_income_ratio,
    ROUND(AVG(risk_score), 2) AS avg_risk_score
FROM loans
GROUP BY loan_to_income_segment
ORDER BY default_rate_pct DESC;


-- 6. Default rate by loan amount segment

SELECT
    loan_amount_segment,
    COUNT(*) AS total_loans,
    SUM(default_flag) AS defaulted_loans,
    ROUND(AVG(default_flag) * 100, 2) AS default_rate_pct,
    ROUND(AVG(loan_amount), 2) AS avg_loan_amount,
    SUM(loan_amount) AS total_loan_amount
FROM loans
GROUP BY loan_amount_segment
ORDER BY default_rate_pct DESC;


-- 7. Default rate by loan purpose

SELECT
    loan_purpose,
    COUNT(*) AS total_loans,
    SUM(default_flag) AS defaulted_loans,
    ROUND(AVG(default_flag) * 100, 2) AS default_rate_pct,
    ROUND(AVG(loan_amount), 2) AS avg_loan_amount,
    ROUND(AVG(interest_rate), 2) AS avg_interest_rate,
    SUM(CASE WHEN default_flag = 1 THEN loan_amount ELSE 0 END) AS defaulted_loan_amount
FROM loans
GROUP BY loan_purpose
ORDER BY default_rate_pct DESC;


-- 8. Default rate by previous default status

SELECT
    previous_default_status,
    COUNT(*) AS total_loans,
    SUM(default_flag) AS defaulted_loans,
    ROUND(AVG(default_flag) * 100, 2) AS default_rate_pct,
    ROUND(AVG(risk_score), 2) AS avg_risk_score
FROM loans
GROUP BY previous_default_status
ORDER BY default_rate_pct DESC;


-- 9. High-risk loans sample

SELECT
    loan_id,
    age,
    annual_income,
    loan_amount,
    interest_rate,
    loan_grade,
    loan_purpose,
    loan_to_income_ratio,
    previous_default_status,
    risk_score,
    risk_level,
    default_status
FROM loans
WHERE risk_level IN ('High Risk', 'Very High Risk')
ORDER BY risk_score DESC
LIMIT 20;