import streamlit as st
import pandas as pd
import os

st.title("📊 Personal Expense Tracker")

file = "data.csv"

if os.path.exists(file):
    df = pd.read_csv(file)
else:
    df = pd.DataFrame(columns=["Date", "Description", "Amount", "Type"])

st.header("Add Transaction")

date = st.date_input("Date")
desc = st.text_input("Description")
amount = st.number_input("Amount", min_value=0.0)
type_option = st.selectbox("Type", ["Income", "Expense"])

if st.button("Add"):
    new_row = {
        "Date": date,
        "Description": desc,
        "Amount": amount,
        "Type": type_option
    }

    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_csv(file, index=False)
    st.success("Added Successfully")

st.header("All Transactions")

if not df.empty:
    st.dataframe(df)

    index = st.number_input("Enter Row Number to Delete", min_value=0, max_value=len(df)-1, step=1)

    if st.button("Delete"):
        df = df.drop(index)
        df.to_csv(file, index=False)
        st.success("Deleted Successfully")

if not df.empty:
    income = df[df["Type"] == "Income"]["Amount"].sum()
    expense = df[df["Type"] == "Expense"]["Amount"].sum()

    st.header("Summary")
    st.write("Total Income:", income)
    st.write("Total Expense:", expense)
    st.write("Balance:", income - expense)
