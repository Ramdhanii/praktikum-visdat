import streamlit as st
import pandas as pd
import numpy as np


st.title("Praktikum 2 - Visualisasi Data")
st.caption("Bagian 4: Map")
st.markdown("""
Kelompok 4 :
- Erina Nurul Hodijah - 0110112113
- Hanin Salwa Salsabila Hidayati Nurrohman - 0110122294
- Mohammad Ramdhani - 0110122083
""")

df = pd.DataFrame(
    np.random.randn(50, 2)/[18,10] + [15.4589, 75.0078],
    columns=["latitude", "longitude"]
)

st.map(df)