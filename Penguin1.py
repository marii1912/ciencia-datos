import pandas as pd
import streamlit as st 

Penguin_data = pd.read_csv("https://raw.githubusercontent.com/marii1912/ciencia-datos/refs/heads/main/Penguin%20Species.csv")

st.sidebar.title("Controles")
agree = st.checkbox("show DataSet Overview ? ")
if agree:
    st.dataframe(Penguin_data)