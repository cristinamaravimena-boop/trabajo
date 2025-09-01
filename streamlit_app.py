import streamlit as st
import pandas as pd
import numpy as np

st.title("Mi primer dashboard con Streamlit")
st.write("Hola, esto corre desde GitHub + Streamlit Cloud 🙂")

n = st.slider("Filas aleatorias", 5, 100, 25)
chart_data = pd.DataFrame(np.random.randn(n), columns=["data"])
st.line_chart(chart_data)
