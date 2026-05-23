-- =====================================================
-- 04_risk_recommendations.sql
-- Credit Risk & Loan Default Analytics
-- Purpose: Identify high-risk and low-risk lending segments
-- =====================================================


-- 1. High-risk borrower segments

SELECT
    risk_level,
    loan_grade,
    income_segment,
    loan_to_income_segment,
    COUNT(*) AS total_loans,
    SUM(default_flag) AS defaulted_loans,
    ROUND(AVG(default_flag) * 100, 2) AS default_rate_pct,
    SUM(loan_amount) AS total_loan_amount,
    SUM(CASE WHEN default_flag = 1 THEN loan_amount ELSE 0 END) AS defaulted_loan_amount,
    ROUND(AVG(risk_score), 2) AS avg_risk_score
FROM loans
GROUP BY
    risk_level,
    loan_grade,
    income_segment,
    loan_to_income_segment
HAVING COUNT(*) >= 30
ORDER BY default_rate_pct DESC
LIMIT 20;


-- 2. Low-risk borrower segments

SELECT
    risk_level,
    loan_grade,
    income_segment,
    loan_to_income_segment,
    COUNT(*) AS total_loans,
    SUM(default_flag) AS defaulted_loans,
    ROUND(AVG(default_flag) * 100, 2) AS default_rate_pct,
    SUM(loan_amount) AS total_loan_amount,
    ROUND(AVG(interest_rate), 2) AS avg_interest_rate,
    ROUND(AVG(risk_score), 2) AS avg_risk_score
FROM loans
WHERE risk_level = 'Low Risk'
GROUP BY
    risk_level,
    loan_grade,
    income_segment,
    loan_to_income_segment
HAVING COUNT(*) >= 30
ORDER BY default_rate_pct ASC
LIMIT 20;


-- 3. Risky loan purposes

SELECT
    loan_purpose,
    COUNT(*) AS total_loans,
    SUM(default_flag) AS defaulted_loans,
    ROUND(AVG(default_flag) * 100, 2) AS default_rate_pct,
    SUM(loan_amount) AS total_loan_amount,
    SUM(CASE WHEN default_flag = 1 THEN loan_amount ELSE 0 END) AS defaulted_loan_amount,
    ROUND(AVG(interest_rate), 2) AS avg_interest_rate,
    ROUND(AVG(risk_score), 2) AS avg_risk_score
FROM loans
GROUP BY loan_purpose
ORDER BY default_rate_pct DESC;


-- 4. Segments with high defaulted loan amount

SELECT
    risk_level,
    loan_purpose,
    income_segment,
    COUNT(*) AS total_loans,
    SUM(default_flag) AS defaulted_loans,
    ROUND(AVG(default_flag) * 100, 2) AS default_rate_pct,
    SUM(loan_amount) AS total_loan_amount,
    SUM(CASE WHEN default_flag = 1 THEN loan_amount ELSE 0 END) AS defaulted_loan_amount
FROM loans
GROUP BY
    risk_level,
    loan_purpose,
    income_segment
HAVING COUNT(*) >= 50
ORDER BY defaulted_loan_amount DESC
LIMIT 20;


-- 5. Borrowers requiring stricter approval rules

SELECT
    loan_id,
    age,
    annual_income,
    home_ownership,
    employment_length,
    loan_purpose,
    loan_grade,
    loan_amount,
    interest_rate,
    loan_to_income_ratio,
    previous_default_status,
    risk_score,
    risk_level,
    default_status
FROM loans
WHERE
    risk_level IN ('High Risk', 'Very High Risk')
    AND loan_to_income_segment IN ('High DTI', 'Very High DTI')
ORDER BY risk_score DESC
LIMIT 50;


-- 6. Safer lending segments

SELECT
    loan_grade,
    income_segment,
    home_ownership,
    employment_length_segment,
    COUNT(*) AS total_loans,
    SUM(default_flag) AS defaulted_loans,
    ROUND(AVG(default_flag) * 100, 2) AS default_rate_pct,
    ROUND(AVG(loan_amount), 2) AS avg_loan_amount,
    ROUND(AVG(interest_rate), 2) AS avg_interest_rate,
    ROUND(AVG(risk_score), 2) AS avg_risk_score
FROM loans
WHERE
    risk_level = 'Low Risk'
    AND loan_grade IN ('A', 'B')
GROUP BY
    loan_grade,
    income_segment,
    home_ownership,
    employment_length_segment
HAVING COUNT(*) >= 50
ORDER BY default_rate_pct ASC
LIMIT 20;


-- 7. Recommendation summary by risk level

SELECT
    risk_level,
    COUNT(*) AS total_loans,
    SUM(default_flag) AS defaulted_loans,
    ROUND(AVG(default_flag) * 100, 2) AS default_rate_pct,
    SUM(loan_amount) AS total_loan_amount,
    SUM(CASE WHEN default_flag = 1 THEN loan_amount ELSE 0 END) AS defaulted_loan_amount,
    ROUND(AVG(interest_rate), 2) AS avg_interest_rate,
    ROUND(AVG(risk_score), 2) AS avg_risk_score,
    CASE
        WHEN risk_level = 'Very High Risk' THEN 'Reject or require strict manual review'
        WHEN risk_level = 'High Risk' THEN 'Approve only with stronger controls'
        WHEN risk_level = 'Medium Risk' THEN 'Standard review with additional monitoring'
        WHEN risk_level = 'Low Risk' THEN 'Preferred segment for lending'
        ELSE 'Review required'
    END AS recommended_action
FROM loans
GROUP BY risk_level
ORDER BY default_rate_pct DESC;