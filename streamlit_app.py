import streamlit as st
import pandas as pd

# Set up Streamlit page configuration
st.set_page_config(
    page_title='Claims Dashboard',
    page_icon=':clipboard:',  # Dashboard icon
)

# Title of the dashboard
st.title(':clipboard: Claims Dashboard')
st.markdown("""
Analyze claim data and injury types. Use the filters below to explore the dataset interactively.
""")

# Load the dataset
@st.cache_data
def load_data():
    file_path = '/workspaces/gdp-dashboard-2/data/submission_2 (Autosaved).csv'  # Update the file path if needed
    data = pd.read_csv(file_path)
    return data

data = load_data()

# Show a preview of the data
if st.checkbox('Show dataset preview'):
    st.write(data.head())

# Dropdown for filtering by injury type
injury_types = data['Claim Injury Type'].unique()
selected_injury_types = st.multiselect(
    'Select Injury Types to Analyze',
    options=injury_types,
    default=injury_types[:3]  # Preselect the first three options
)

# Filter dataset based on selection
filtered_data = data[data['Claim Injury Type'].isin(selected_injury_types)]

# Display summary statistics
st.subheader('Summary Statistics')
st.write(f"Total Claims in Dataset: {len(data)}")
st.write(f"Filtered Claims: {len(filtered_data)}")

# Line chart of claim counts over time
st.subheader('Claim Trends Over Time')

# Check if there is a date or year column for plotting
if 'Year' in data.columns:  # Replace 'Year' with your actual time column if different
    # Group by year and count claims
    trend_data = filtered_data.groupby('Year').size().reset_index(name='Claim Count')
    st.line_chart(trend_data.set_index('Year'))
else:
    st.error("The dataset does not contain a 'Year' column. Please ensure your dataset has a time-related column for trends.")

# Bar chart of claim counts by injury type
st.subheader('Claim Counts by Injury Type')
claim_counts = filtered_data['Claim Injury Type'].value_counts()
st.bar_chart(claim_counts)

# Downloadable filtered dataset
st.subheader('Download Filtered Dataset')
csv = filtered_data.to_csv(index=False)
st.download_button(
    label="Download as CSV",
    data=csv,
    file_name='filtered_claims.csv',
    mime='text/csv'
)

# Additional notes
st.markdown("""
This dashboard is designed to provide insights into the claims data, focusing on injury types. Use the filter and download options to customize your analysis.
""")





























# import streamlit as st
# import pandas as pd

# # Set up Streamlit page configuration
# st.set_page_config(
#     page_title='Claims Dashboard',
#     page_icon=':clipboard:',  # Dashboard icon
# )

# # Title of the dashboard
# st.title(':clipboard: Claims Dashboard')
# st.markdown("""
# Analyze claim data and injury types. Use the filters below to explore the dataset interactively.
# """)

# # Load the dataset
# @st.cache_data
# def load_data():
#     file_path = '/workspaces/gdp-dashboard-2/data/submission_2 (Autosaved).csv'
#     data = pd.read_csv(file_path)
#     return data

# data = load_data()

# # Show a preview of the data
# if st.checkbox('Show dataset preview'):
#     st.write(data.head())

# # Dropdown for filtering by injury type
# injury_types = data['Claim Injury Type'].unique()
# selected_injury_types = st.multiselect(
#     'Select Injury Types to Analyze',
#     options=injury_types,
#     default=injury_types[:3]  # Preselect the first three options
# )

# # Filter dataset based on selection
# filtered_data = data[data['Claim Injury Type'].isin(selected_injury_types)]

# # Display summary statistics
# st.subheader('Summary Statistics')
# st.write(f"Total Claims in Dataset: {len(data)}")
# st.write(f"Filtered Claims: {len(filtered_data)}")

# # Bar chart of claim counts by injury type
# st.subheader('Claim Counts by Injury Type')
# claim_counts = filtered_data['Claim Injury Type'].value_counts()
# st.bar_chart(claim_counts)

# # Downloadable filtered dataset
# st.subheader('Download Filtered Dataset')
# csv = filtered_data.to_csv(index=False)
# st.download_button(
#     label="Download as CSV",
#     data=csv,
#     file_name='filtered_claims.csv',
#     mime='text/csv'
# )

# # Additional notes
# st.markdown("""
# This dashboard is designed to provide insights into the claims data, focusing on injury types. Use the filter and download options to customize your analysis.
# """)
