import streamlit as st
import pandas as pd
st.title("Titanic Dataset") 

data = pd.read_csv("https://raw.githubusercontent.com/adsoftsito/ciencia-datos/refs/heads/main/titanic.csv")
st.dataframe(data)
selected_sex = st.selectbox("Select Sex", data['sex'].unique())