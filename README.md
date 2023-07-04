# US Colleges Information Dashboard

This is a Streamlit application that provides an interactive dashboard for exploring data from US colleges. It uses data from the CollegeScorecard API, including information like tuition fees, state, and student expenditure. Users can select a state to see specific data for that area, as well as get suggestions for schools based on a specified budget.

## Data Preprocessing

The dataset used for this application underwent a preprocessing step to handle missing values. This involved using the IterativeImputer function from the scikit-learn library, which models each feature with missing values as a function of other features and uses that estimate for imputation. This method allows us to use the entire dataset when generating our dashboard.

## Running the Application

To run the application, navigate to the project directory in your terminal and type:
```
streamlit run app.py
```

## Features

- **State Selection**: Use the sidebar to select a state and view specific data for that area.
- **College Metrics**: View cards for Mean Tuition, Median Tuition, and Student Expenditure metrics for the selected state.
- **Tuition Histogram**: An interactive histogram that visualizes the distribution of in-state tuition costs for the selected state.
- **School Suggestions**: Input your budget in the sidebar, and the app will suggest schools within your budget in the selected state. 

Feel free to explore the code, make changes, and use this application as a basis for your own data-driven Streamlit apps!