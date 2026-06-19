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
# SESSION STATE RESET LOGIC
# =========================
def reset_app():
    for k in list(st.session_state.keys()):
        del st.session_state[k]
    st.rerun()

if "step" not in st.session_state:
    st.session_state.step = 1

# =========================
# LOGOUT BUTTON (TOP RIGHT)
# =========================
col1, col2 = st.columns([9, 1])

with col2:
    if st.button("🚪 Logout"):
        reset_app()

# =========================
# SIDEBAR NAVIGATION
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

def go(step):
    st.session_state.step = step
    st.rerun()

for i, s in enumerate(steps, 1):

    # restrict jumping to first 2 steps
    if i <= 2:
        st.sidebar.markdown(f"🔒 {s}")
    else:
        if st.sidebar.button(s):
            go(i)

st.sidebar.progress(st.session_state.step / len(steps))

# =========================
# HEADER
# =========================
st.title("🏦 Smart Loan Application Portal")

st.progress(st.session_state.step / len(steps))

# =========================
# VALIDATORS
# =========================
def valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email)

# =========================
# STEP 1 - PERSONAL INFO
# =========================
if st.session_state.step == 1:

    st.subheader("Step 1: Personal Information")

    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")

    dob = st.date_input(
        "Date of Birth",
        min_value=date(1920, 1, 1),
        max_value=date.today(),
        value=date(1995, 1, 1)        # default safe value
    )

    today = date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

    show_error = False

    if st.button("Next ➜"):

        if age < 18:
            st.error("Applicant must be at least 18 years old")
            show_error = True
        else:
            st.session_state.first_name = first_name
            st.session_state.last_name = last_name
            st.session_state.age = age
            st.session_state.step = 2
            st.rerun()
    col1, col2 = st.columns(2)

# =========================
# STEP 2 - EMAIL OTP
# =========================
elif st.session_state.step == 2:

    st.subheader("Step 2: Email Verification")

    email = st.text_input("Email Address")

    if st.button("Send OTP"):

        if not valid_email(email):
            st.error("Invalid email format")
        else:
            st.session_state.email = email
            st.session_state.otp = str(random.randint(100000, 999999))
            st.success("OTP sent (demo mode)")
            st.info(f"DEMO OTP: {st.session_state.otp}")

    otp_input = st.text_input("Enter OTP")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Verify Email"):

            if otp_input == st.session_state.get("otp"):
                st.session_state.email_verified = True
                st.success("Email Verified ✔")

                # AUTO MOVE NEXT
                st.session_state.step = 3
                st.rerun()

            else:
                st.error("Invalid OTP")

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
    annual_income = st.number_input("Annual Income", 0.0, 1000000.0, 80000.0)

    employment_type = st.selectbox(
        "Employment Type",
        ["salaried", "self_employed", "contract"]
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Back"):
            st.session_state.step = 2
            st.rerun()

    with col2:
        if st.button("Next"):
            st.session_state.years_employed = years_employed
            st.session_state.annual_income = annual_income
            st.session_state.employment_type = employment_type
            st.session_state.step = 4
            st.rerun()

# =========================
# STEP 4 - CREDIT
# =========================
elif st.session_state.step == 4:

    st.subheader("Step 4: Credit Profile")

    credit_score = st.text_input("Credit Score (300–850)")
    dti_ratio = st.text_input("DTI Ratio (0.0, 1.0, 0.3)")
    existing_debt = st.number_input("Existing Debt", 0.0, 1000000.0, 10000.0)

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
                st.error("Credit score must be numeric")
            else:
                credit_score = int(credit_score)

                if credit_score < 300 or credit_score > 850:
                    st.error("Credit score must be 300–850")
                else:
                    st.session_state.credit_score = credit_score
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

    monthly_expenses = st.number_input("Monthly Expenses", 0.0, 100000.0, 3000.0)
    savings_balance = st.number_input("Savings Balance", 0.0, 1000000.0, 50000.0)

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
# STEP 6 - LOAN DETAILS
# =========================
elif st.session_state.step == 6:

    st.subheader("Step 6: Loan Details")

    loan_term_months = st.selectbox("Loan Term", [36, 60, 120, 180])

    if st.button("Next"):
        st.session_state.loan_term_months = loan_term_months
        st.session_state.step = 7
        st.rerun()

# =========================
# STEP 7 - REVIEW + PREDICT
# =========================
elif st.session_state.step == 7:

    st.subheader("Step 7: Review & Predict")

    if st.button("Generate Loan Recommendation"):

        input_df = pd.DataFrame([{
            "age": st.session_state.age,
            "years_employed": st.session_state.years_employed,
            "annual_income": st.session_state.annual_income,
            "credit_score": st.session_state.credit_score,
            "dti_ratio": st.session_state.dti_ratio,
            "existing_debt": st.session_state.existing_debt,
            "monthly_expenses": st.session_state.monthly_expenses,
            "savings_balance": st.session_state.savings_balance,
            "num_open_credit_lines": st.session_state.num_open_credit_lines,
            "num_previous_defaults": st.session_state.num_previous_defaults,
            "property_owned": 1 if st.session_state.property_owned == "Yes" else 0,
            "loan_term_months": st.session_state.loan_term_months
        }])

        input_df = input_df.reindex(columns=FEATURES)

        prediction = model.predict(input_df)[0]

        st.success(
            f"Hello {st.session_state.first_name} {st.session_state.last_name}"
        )

        st.metric("Recommended Loan Amount", f"${prediction:,.2f}")