import streamlit as st
import pandas as pd
from datetime import date

# ----------------------------------------------------
# App configuration
# ----------------------------------------------------
st.set_page_config(
    page_title="Expense Tracker",
    layout="wide"
)

st.title("Expense Tracker")
st.write("Track your daily expenses easily.")

st.divider()

# ----------------------------------------------------
# Session State Initialization
# ----------------------------------------------------
if "expenses" not in st.session_state:
    st.session_state.expenses = []

# ----------------------------------------------------
# Expense Input Form
# ----------------------------------------------------
st.header("Add a New Expense")

with st.form("expense_form"):
    name = st.text_input("Expense Name")
    amount = st.number_input("Amount", min_value=0.0, step=1.0)
    expense_date = st.date_input("Date", value=date.today())
    category = st.selectbox(
        "Category",
        ["Food", "Travel", "Shopping", "Bills", "Other"]
    )

    submitted = st.form_submit_button("Add Expense")

if submitted:
    if name.strip() == "":
        st.error("Expense name cannot be empty.")
    else:
        st.session_state.expenses.append({
            "Name": name,
            "Amount": amount,
            "Date": expense_date,
            "Category": category
        })
        st.success("Expense added successfully!")

st.divider()

# ----------------------------------------------------
# Display Expenses
# ----------------------------------------------------
st.header("All Expenses")

if len(st.session_state.expenses) == 0:
    st.info("No expenses added yet.")
else:
    df = pd.DataFrame(st.session_state.expenses)

    # Convert Date column to datetime (important for grouping)
    df["Date"] = pd.to_datetime(df["Date"])

    st.dataframe(df, use_container_width=True)

    st.divider()

    # ------------------------------------------------
    # Summary Section
    # ------------------------------------------------
    st.header("Summary")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Total Spending")
        total_spent = df["Amount"].sum()
        st.write(f"₹ {total_spent:.2f}")

        st.subheader("Category-wise Spending")
        category_sum = df.groupby("Category")["Amount"].sum()
        st.bar_chart(category_sum)

    with col2:
        st.subheader("Daily Spending")
        daily_sum = df.groupby("Date")["Amount"].sum()
        st.line_chart(daily_sum)

# ----------------------------------------------------
# Optional: Clear All Expenses
# ----------------------------------------------------
st.divider()

if st.button("Clear All Expenses"):
    st.session_state.expenses = []
    st.warning("All expenses have been cleared.")
