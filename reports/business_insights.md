# Business Insights

## Project: Credit Risk & Loan Default Analytics

This report summarizes the main findings from the credit risk and loan default analytics project.

The analysis is based on a cleaned and enriched loan dataset containing borrower information, loan characteristics, credit risk indicators, and loan default status.

---

## 1. Overall Portfolio Performance

The analyzed loan portfolio contains **32,411 loans**.

Key portfolio metrics:

- Total loans: **32,411**
- Total loan amount: **310.94M**
- Defaulted loans: **7,089**
- Defaulted loan amount: **76.97M**
- Overall default rate: **21.87%**
- Average loan amount: **9.59K**
- Average interest rate: **11.02%**
- Average risk score: **33.84**

The overall default rate shows that approximately **one out of five loans resulted in default**.

This indicates a significant credit risk exposure and highlights the importance of identifying high-risk borrower segments before loan approval.

---

## 2. Risk Level Analysis

A rule-based risk score was created using loan grade, interest rate, loan-to-income ratio, previous default status, and income level.

The risk segmentation shows a strong relationship between calculated risk level and actual default rate:

| Risk Level | Total Loans | Default Rate |
|---|---:|---:|
| Low Risk | 17,151 | 5.57% |
| Medium Risk | 9,685 | 30.62% |
| High Risk | 4,242 | 51.37% |
| Very High Risk | 1,333 | 74.19% |

The default rate increases sharply across risk levels.

Very High Risk borrowers defaulted at a rate of **74.19%**, compared with only **5.57%** for Low Risk borrowers.

This confirms that the risk score provides a meaningful segmentation of borrower risk.

---

## 3. Loan Grade and Default Risk

Loan grade is one of the strongest indicators of default risk.

Default rates by loan grade:

| Loan Grade | Default Rate |
|---|---:|
| A | 9.96% |
| B | 16.32% |
| C | 20.76% |
| D | 59.06% |
| E | 64.49% |
| F | 70.54% |
| G | 98.44% |

Loans with grades **D, E, F, and G** show extremely high default rates.

Grade G loans defaulted in almost all cases, with a default rate of **98.44%**.

This suggests that low-grade loans should require stricter approval rules, additional verification, or manual review.

---

## 4. Interest Rate Segment Analysis

Interest rate is also strongly connected with default risk.

Borrowers with very high interest rates show the highest default probability.

This is expected because higher interest rates usually reflect higher perceived credit risk.

The dashboard shows that:

- Very High Rate loans have the highest default rate.
- High Rate loans also show elevated default risk.
- Very Low Rate and Low Rate loans are significantly safer.

This supports the conclusion that interest rate is not only a pricing variable but also a strong risk signal.

---

## 5. Loan-to-Income Risk

Loan-to-income ratio is another important risk driver.

Borrowers with higher loan-to-income ratios show much higher default rates.

The analysis shows that:

- Very High DTI borrowers have the highest default rate.
- High DTI borrowers also represent a risky segment.
- Very Low DTI borrowers are significantly safer.

This means that the relationship between loan size and borrower income should be a key part of loan approval decisions.

---

## 6. Income Segment Analysis

Income level has a clear relationship with default risk.

Default rates by income segment:

| Income Segment | Default Rate |
|---|---:|
| Low Income | 45.59% |
| Lower-Mid Income | 23.76% |
| Mid Income | 13.38% |
| High Income | 11.96% |
| Upper-Mid Income | 9.27% |

Low Income borrowers show the highest default rate at **45.59%**.

This suggests that lower-income borrowers require more careful credit assessment, especially when combined with high DTI, poor loan grade, or previous default history.

---

## 7. Home Ownership Analysis

Home ownership is another meaningful borrower characteristic.

Default rates by home ownership status show that:

- Renters have significantly higher default risk.
- Borrowers with mortgages are safer.
- Borrowers who own property show the lowest default risk.

This suggests that home ownership status can be used as a supporting risk indicator in credit decision-making.

---

## 8. Employment Length Analysis

Employment length also shows a clear pattern.

Borrowers with shorter employment history have higher default rates.

The highest default rate is observed among borrowers with **0–1 years** of employment history.

As employment length increases, default risk generally decreases.

This indicates that job stability is an important borrower quality indicator.

---

## 9. Loan Purpose Analysis

Default risk also varies by loan purpose.

The highest-risk purposes are:

- Debt Consolidation
- Medical
- Home Improvement

Debt Consolidation loans show the highest default rate among loan purposes.

This may indicate that borrowers taking debt consolidation loans already have financial stress or existing debt burden.

---

## 10. Business Recommendations

Based on the analysis, the following actions are recommended:

### 1. Apply strict manual review for Very High Risk borrowers

Borrowers classified as Very High Risk show a default rate of **74.19%**.

Recommended action:

- Reject automatically in many cases
- Require manual credit review
- Request additional documentation
- Reduce approved loan amount
- Apply stricter DTI limits

---

### 2. Add stronger controls for High Risk borrowers

High Risk borrowers show a default rate of **51.37%**.

Recommended action:

- Approve only with stronger controls
- Review income stability
- Check previous default history
- Limit loan size
- Monitor repayment behavior more closely

---

### 3. Prioritize Low Risk borrowers

Low Risk borrowers show a default rate of only **5.57%**.

Recommended action:

- Treat as preferred lending segment
- Offer faster approval
- Use for portfolio growth
- Consider better pricing or cross-sell opportunities

---

### 4. Use loan grade and DTI as key approval signals

Loan grade and loan-to-income ratio are among the strongest risk indicators.

Recommended action:

- Tighten approval rules for grades D–G
- Apply maximum DTI thresholds
- Combine grade, income, and DTI in risk policy

---

### 5. Monitor risky loan purposes

Debt Consolidation, Medical, and Home Improvement loans show higher default risk.

Recommended action:

- Add additional checks for risky purposes
- Monitor these loan categories separately
- Adjust approval rules based on purpose-level risk

---

## Final Conclusion

The analysis shows that credit default risk is strongly connected with borrower income, loan grade, interest rate, loan-to-income ratio, previous default history, home ownership, and employment length.

The created risk score successfully separates borrowers into meaningful risk groups.

The most important finding is that Very High Risk borrowers default at **74.19%**, while Low Risk borrowers default at only **5.57%**.

This project demonstrates how Python, SQL, and Power BI can be used together to clean financial data, create analytical risk segments, identify high-risk borrowers, and support data-driven credit decision-making.