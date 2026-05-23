-- =====================================================
-- 01_portfolio_overview.sql
-- Credit Risk & Loan Default Analytics
-- Purpose: Analyze overall loan portfolio performance
-- =====================================================


-- 1. Portfolio overview

SELECT
    COUNT(*) AS total_loans,
    SUM(loan_amount) AS total_loan_amount,
    SUM(default_flag) AS defaulted_loans,
    SUM(CASE WHEN default_flag = 1 THEN loan_amount ELSE 0 END) AS defaulted_loan_amount,
    ROUND(AVG(default_flag) * 100, 2) AS default_rate_pct,
    ROUND(AVG(loan_amount), 2) AS average_loan_amount,
    ROUND(AVG(interest_rate), 2) AS average_interest_rate,
    ROUND(AVG(risk_score), 2) AS average_risk_score
FROM loans;


-- 2. Portfolio by risk level

SELECT
    risk_level,
    COUNT(*) AS total_loans,
    SUM(loan_amount) AS total_loan_amount,
    SUM(default_flag) AS defaulted_loans,
    SUM(CASE WHEN default_flag = 1 THEN loan_amount ELSE 0 END) AS defaulted_loan_amount,
    ROUND(AVG(default_flag) * 100, 2) AS default_rate_pct,
    ROUND(AVG(risk_score), 2) AS average_risk_score
FROM loans
GROUP BY risk_level
ORDER BY 6 DESC;


-- 3. Portfolio by loan grade

SELECT
    loan_grade,
    COUNT(*) AS total_loans,
    SUM(loan_amount) AS total_loan_amount,
    SUM(default_flag) AS defaulted_loans,
    SUM(CASE WHEN default_flag = 1 THEN loan_amount ELSE 0 END) AS defaulted_loan_amount,
    ROUND(AVG(default_flag) * 100, 2) AS default_rate_pct,
    ROUND(AVG(loan_amount), 2) AS average_loan_amount,
    ROUND(AVG(interest_rate), 2) AS average_interest_rate,
    ROUND(AVG(risk_score), 2) AS average_risk_score
FROM loans
GROUP BY loan_grade
ORDER BY loan_grade;


-- 4. Portfolio by loan purpose

SELECT
    loan_purpose,
    COUNT(*) AS total_loans,
    SUM(loan_amount) AS total_loan_amount,
    SUM(default_flag) AS defaulted_loans,
    ROUND(AVG(default_flag) * 100, 2) AS default_rate_pct,
    ROUND(AVG(loan_amount), 2) AS average_loan_amount,
    ROUND(AVG(interest_rate), 2) AS average_interest_rate
FROM loans
GROUP BY loan_purpose
ORDER BY total_loan_amount DESC;


-- 5. Portfolio by home ownership

SELECT
    home_ownership,
    COUNT(*) AS total_loans,
    SUM(loan_amount) AS total_loan_amount,
    SUM(default_flag) AS defaulted_loans,
    ROUND(AVG(default_flag) * 100, 2) AS default_rate_pct,
    ROUND(AVG(loan_amount), 2) AS average_loan_amount
FROM loans
GROUP BY home_ownership
ORDER BY 5 DESC;