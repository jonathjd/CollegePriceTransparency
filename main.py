import streamlit as st
import pandas as pd
import plotly_express as px

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("data/CleanInstitutionalData.csv")
    return df

df = load_data()

st.title("US Colleges Information Dashboard")

# Add a selectbox to sidebar
state = st.sidebar.selectbox(
    'Select a state',
    df['STABBR'].unique()
)

filtered_df = df[df["STABBR"] == state]

st.subheader(f"Data for colleges in {state}")

mean_cost = round(filtered_df["TUITIONFEE_IN"].mean())
median_cost = filtered_df["TUITIONFEE_IN"].median()
median_expenditure = filtered_df['INEXPFTE'].median()

# cards for metrics
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Mean Tuition", mean_cost)

with col2:
    st.metric("Median Tuition", median_cost)

with col3:
    st.metric("Student Expenditure", median_expenditure)

st.dataframe(filtered_df)

# Histogram for 'In-state tuition'
fig = px.histogram(filtered_df, 
                   x='TUITIONFEE_IN', 
                   nbins=20, 
                   title='Distribution of In-state Tuition', 
                   labels={'TUITIONFEE_IN':'In-state Tuition', 'count': 'Number of Schools'},
                   template="plotly_white"
                   )

st.plotly_chart(fig)

budget = st.sidebar.number_input("Input your budget")

# suggestions
suggested_schools = filtered_df[filtered_df["TUITIONFEE_IN"] <= budget]
if not suggested_schools.empty:
    st.subheader("Suggested schools based on budget:")
    st.dataframe(suggested_schools[["INSTNM", "ZIP", "TUITIONFEE_IN"]], use_container_width=True)

else:
    st.subheader("No schools found within the budget")








