import streamlit as st
import pandas as pd
import random
import re
import joblib
from datetime import date
from pathlib import Path

# =========================
# CONFIG
# =========================
st.set_page_config(page_title="Loan Portal", layout="wide")

model = joblib.load("project1/loan_amount_xgb.pkl")

FEATURES = [
    "age",
    "years_employed",
    "annual_income",
    "credit_score",
    "dti_ratio",
    "existing_debt",
    "monthly_expenses",
    "savings_balance",
    "num_open_credit_lines",
    "num_previous_defaults",
    "property_owned",
    "loan_term_months"
]

# =========================
# RESET APP
# =========================
def reset_app():
    for k in list(st.session_state.keys()):
        del st.session_state[k]
    st.rerun()

if "step" not in st.session_state:
    st.session_state.step = 1

# =========================
# LOGOUT
# =========================
col1, col2 = st.columns([9, 1])
with col2:
    if st.button("🚪 Logout"):
        reset_app()

# =========================
# SIDEBAR NAV
# =========================
st.sidebar.title("🏦 Navigation")

steps = [
    "Personal",
    "Email Verification",
    "Employment",
    "Credit",
    "Financials",
    "Loan Details",
    "Review"
]

for i, s in enumerate(steps, 1):
    if i <= st.session_state.step:
        if st.sidebar.button(s, key=f"nav_{i}"):
            st.session_state.step = i
            st.rerun()
    else:
        st.sidebar.markdown(f"🔒 {s}")

st.sidebar.progress(st.session_state.step / len(steps))

st.title("🏦 Smart Loan Application Portal")
st.progress(st.session_state.step / len(steps))

# =========================
# EMAIL VALIDATION
# =========================
def valid_email(email):
    return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email)

# =========================
# STEP 1 - PERSONAL
# =========================
if st.session_state.step == 1:

    st.subheader("Step 1: Personal Information")

    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")

    dob = st.date_input(
        "Date of Birth",
        min_value=date(1920, 1, 1),
        max_value=date.today(),
        value=date(1995, 1, 1)
    )

    age = date.today().year - dob.year - (
        (date.today().month, date.today().day) < (dob.month, dob.day)
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Next ➜"):
            if age < 18:
                st.error("Must be 18+")
            else:
                st.session_state.first_name = first_name
                st.session_state.last_name = last_name
                st.session_state.age = age
                st.session_state.step = 2
                st.rerun()

    with col2:
        if st.button("Reset"):
            reset_app()

# =========================
# STEP 2 - EMAIL
# =========================
elif st.session_state.step == 2:

    st.subheader("Step 2: Email Verification")

    email = st.text_input("Email")

    if st.button("Send OTP"):

        if not valid_email(email):
            st.error("Invalid email")
        else:
            st.session_state.email = email
            st.session_state.otp = str(random.randint(100000, 999999))
            st.success(f"OTP Sent (demo): {st.session_state.otp}")

    otp_input = st.text_input("Enter OTP")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Verify"):
            if otp_input == st.session_state.get("otp"):
                st.session_state.step = 3
                st.success("Verified ✔")
                st.rerun()
            else:
                st.error("Wrong OTP")

    with col2:
        if st.button("Back"):
            st.session_state.step = 1
            st.rerun()

# =========================
# STEP 3 - EMPLOYMENT
# =========================
elif st.session_state.step == 3:

    st.subheader("Step 3: Employment")

    years_employed = st.number_input("Years Employed", 0, 50, 5)
    annual_income = st.number_input("Annual Income", 0.0, 1_000_000.0, 80000.0)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Back"):
            st.session_state.step = 2
            st.rerun()

    with col2:
        if st.button("Next"):
            st.session_state.years_employed = years_employed
            st.session_state.annual_income = annual_income
            st.session_state.step = 4
            st.rerun()

# =========================
# STEP 4 - CREDIT
# =========================
elif st.session_state.step == 4:

    st.subheader("Step 4: Credit Profile")

    credit_score = st.text_input("Credit Score (300-850)")
    dti_ratio = st.number_input("DTI Ratio", 0.0, 1.0, 0.3)
    existing_debt = st.number_input("Existing Debt", 0.0, 1_000_000.0, 10000.0)

    num_open_credit_lines = st.number_input("Open Credit Lines", 0, 20, 5)
    num_previous_defaults = st.number_input("Previous Defaults", 0, 10, 0)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Back"):
            st.session_state.step = 3
            st.rerun()

    with col2:
        if st.button("Next"):

            if not credit_score.isdigit():
                st.error("Invalid credit score")
            else:
                cs = int(credit_score)

                if cs < 300 or cs > 850:
                    st.error("Range 300-850")
                else:
                    st.session_state.credit_score = cs
                    st.session_state.dti_ratio = dti_ratio
                    st.session_state.existing_debt = existing_debt
                    st.session_state.num_open_credit_lines = num_open_credit_lines
                    st.session_state.num_previous_defaults = num_previous_defaults
                    st.session_state.step = 5
                    st.rerun()

# =========================
# STEP 5 - FINANCIALS
# =========================
elif st.session_state.step == 5:

    st.subheader("Step 5: Financials")

    monthly_expenses = st.number_input("Monthly Expenses", 0.0, 1_000_000.0, 3000.0)
    savings_balance = st.number_input("Savings Balance", 0.0, 1_000_000.0, 50000.0)

    property_owned = st.selectbox("Property Owned", ["No", "Yes"])

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Back"):
            st.session_state.step = 4
            st.rerun()

    with col2:
        if st.button("Next"):
            st.session_state.monthly_expenses = monthly_expenses
            st.session_state.savings_balance = savings_balance
            st.session_state.property_owned = property_owned
            st.session_state.step = 6
            st.rerun()

# =========================
# STEP 6 - LOAN
# =========================
elif st.session_state.step == 6:

    st.subheader("Step 6: Loan Details")

    loan_term_months = st.selectbox("Loan Term", [36, 60, 120, 180])

    if st.button("Next"):
        st.session_state.loan_term_months = loan_term_months
        st.session_state.step = 7
        st.rerun()

# =========================
# STEP 7 - PREDICTION
# =========================
elif st.session_state.step == 7:

    st.subheader("Review & Predict")

    if st.button("Generate Prediction"):

        input_df = pd.DataFrame([{
            "age": float(st.session_state.age),
            "years_employed": float(st.session_state.years_employed),
            "annual_income": float(st.session_state.annual_income),
            "credit_score": float(st.session_state.credit_score),
            "dti_ratio": float(st.session_state.dti_ratio),
            "existing_debt": float(st.session_state.existing_debt),
            "monthly_expenses": float(st.session_state.monthly_expenses),
            "savings_balance": float(st.session_state.savings_balance),
            "num_open_credit_lines": float(st.session_state.num_open_credit_lines),
            "num_previous_defaults": float(st.session_state.num_previous_defaults),
            "property_owned": float(st.session_state.property_owned == "Yes"),
            "loan_term_months": float(st.session_state.loan_term_months)
        }])

        input_df = input_df.reindex(columns=FEATURES)

        prediction = model.predict(input_df)[0]

        st.success(
            f"Hello {st.session_state.first_name} {st.session_state.last_name}"
        )

        st.metric("Recommended Loan Amount", f"${prediction:,.2f}")