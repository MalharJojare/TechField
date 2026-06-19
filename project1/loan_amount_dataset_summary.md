# Loan Amount Recommendation — Dataset Summary

## About the Dataset

This dataset contains 15,000 records of borrower financial profiles designed for predicting a recommended loan amount. It covers a range of personal, employment, and credit attributes commonly used in retail lending decisions. The dataset includes realistic data quality issues such as missing values and outliers to reflect real-world conditions.

| Property | Value |
|---|---|
| Rows | 15,000 |
| Columns | 17 |
| Domain | Finance |
| Problem Type | Regression |
| Target Variable | `recommended_loan_amount` |

---

## Column Descriptions

| Column | Type | Description |
|---|---|---|
| `age` | int | Age of the borrower in years |
| `years_employed` | int | Number of years the borrower has been employed |
| `annual_income` | float | Borrower's gross annual income in USD |
| `credit_score` | int | Borrower's credit score (300–850) |
| `dti_ratio` | float | Debt-to-income ratio |
| `existing_debt` | float | Total existing debt outstanding in USD |
| `loan_purpose` | categorical | The stated purpose of the loan (e.g. home_purchase, auto, education) |
| `employment_type` | categorical | Nature of employment (salaried, self_employed, contract, part_time) |
| `monthly_expenses` | float | Borrower's estimated monthly expenses in USD |
| `num_dependents` | int | Number of financial dependents |
| `savings_balance` | float | Total savings balance in USD |
| `num_open_credit_lines` | int | Number of currently open credit lines |
| `num_previous_defaults` | int | Number of previous loan defaults |
| `property_owned` | binary | Whether the borrower owns property (1 = yes, 0 = no) |
| `loan_term_months` | int | Requested loan repayment term in months |
| `market_rate` | float | Prevailing market interest rate at time of application |
| `recommended_loan_amount` | float | **Target** — the recommended loan amount in USD |
