import pandas as pd
import streamlit as st 
import matplotlib.pyplot as plt
import numpy as np 


Penguin_data = pd.read_csv("https://raw.githubusercontent.com/marii1912/ciencia-datos/refs/heads/main/Penguin%20Species.csv")

st.sidebar.title("Controles")
 ##prueba

agree = st.sidebar.checkbox("show DataSet Overview ?")

if agree:
    st.dataframe(Penguin_data)

species = st.sidebar.radio("species", Penguin_data['species'].unique())
st.sidebar.write("Select:", species)



optionals = st.sidebar.expander("Optional Configurations", True)
fare_min = optionals.slider(
"Minimum Fare",
min_value= (Penguin_data['culmen_length_mm'].min()),
max_value= (Penguin_data['culmen_length_mm'].max())
)


Species = st.sidebar.text_input("species")
st.sidebar.title("MONTALVO LOPEZ MARIA DE JESUS")
st.sidebar.title("Matricula: zS26004572")


Penguin_data = pd.read_csv("https://raw.githubusercontent.com/marii1912/ciencia-datos/refs/heads/main/Penguin%20Species.csv")
fig, ax = plt.subplots()
ax.hist(Penguin_data.species)
st.header("Grafica")
st.pyplot(fig)
st.markdown("___")


Penguin_data = pd.read_csv(
    "https://raw.githubusercontent.com/marii1912/ciencia-datos/refs/heads/main/Penguin%20Species.csv"
)

fig, ax = plt.subplots()

ax.scatter(
    Penguin_data["culmen_length_mm"],
    Penguin_data["culmen_depth_mm"],
    color="blue"
)

ax.set_xlabel("Largo del pico (mm)")
ax.set_ylabel("Profundidad del pico (mm)")
ax.set_title("Largo vs profundidad del pico")

st.header("Gráfica de dispersión")
st.pyplot(fig)
st.markdown("___")


# Gráfica de pastel: largo de la aleta
fig, ax = plt.subplots()

flipper_categories = pd.cut(
    Penguin_data["flipper_length_mm"],
    bins=4,
    labels=["Aletas cortas", "Aletas medianas", "Aletas largas", "Aletas muy largas"]
)

flipper_categories.value_counts().plot.pie(
    autopct="%1.1f%%",
    colors=["lightblue", "skyblue", "royalblue", "navy"],
    ax=ax
)

ax.set_title("Distribución del largo de las aletas")
ax.set_ylabel("")

st.header("Gráfica de pastel")
st.pyplot(fig)
st.markdown("___")



map_data = pd.DataFrame(
np.random.randn(1000, 2) / [50, 50] + [18.8942, -96.9347],
columns=['lat', 'lon'])

st.title("Cordoba 🙂")
st.header("Using Streamlit and Mapbox")

st.map(map_data)


