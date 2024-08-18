import streamlit as st
import pandas as pd
import requests

# URL of the raw JSON file
url = 'https://raw.githubusercontent.com/FinnedAI/sportsbookreview-scraper/main/data/nfl_archive_10Y.json'

# Fetch the JSON data from GitHub
response = requests.get(url)
data = response.json()

# Convert the JSON data to a pandas DataFrame
df = pd.json_normalize(data)

# Display the title of the app
st.title("NFL Archive Data")

# Create a scrollable table in the UI
st.dataframe(df)

# Optionally, add a slider to control the number of rows displayed
num_rows = st.slider("Select number of rows to view", min_value=10, max_value=100, value=20)
st.dataframe(df.head(num_rows))

# Display a summary of the DataFrame
if st.checkbox("Show DataFrame Summary"):
    st.write(df.describe())
