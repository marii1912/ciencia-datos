import pandas as pd
import numpy as np
import streamlit as st



map_data = pd.DataFrame(
np.random.randn(1000, 2) / [50, 50] + [18.8747, -97.0640],
columns=['lat', 'lon'])

# Create the title for the web app
st.title("Universidad Veracruzana - Campus Ixtaczoquitlán")
st.header("Using Streamlit and Mapbox")

st.map(map_data)