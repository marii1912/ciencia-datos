import pandas as pd
import streamlit as st

names_link = "https://raw.githubusercontent.com/marii1912/ciencia-datos/refs/heads/main/action_movies_data.csv" 

names_data = pd.read_csv (names_link)


# Create the title for the web app
st.title("Streamlit and pandas")

st.dataframe(names_data)